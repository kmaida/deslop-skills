#!/usr/bin/env python3
"""Deterministic slop checker for the deslop-writing skill.

Usage:
    python3 check_slop.py DRAFT_FILE [--type prose|docs|social|email]
    cat draft.md | python3 check_slop.py - [--type docs]

Exit codes:
    0  no FAIL-tier violations (WARNs may still print; review them)
    1  FAIL-tier violations found; fix and re-run

Banned vocabulary and phrases are parsed at runtime from
references/banned-words.md so the two never drift. Structural
patterns (em dashes, contrast-punch, bold-label bullets, anaphora,
sentence-length runs) are encoded here as regexes.

Fenced code blocks and inline code are excluded from all checks.

Tiers:
    FAIL  unambiguous: em dashes, bare banned terms, banned phrases,
          structural tells. Must be fixed before output.
    WARN  contextual: terms banned only in certain uses ("critical" as
          filler vs. severity), rhythm heuristics. Review, fix if the
          flagged use matches the banned sense.
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- parsing

def load_banned(md_path):
    """Parse banned-words.md into (fail_terms, warn_terms, phrases, openers)."""
    text = md_path.read_text(encoding="utf-8")
    sections = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"^###?\s+(.*)", line)
        if m:
            current = m.group(1).strip()
            sections[current] = []
        elif current:
            sections[current].append(line)

    fail_terms, warn_terms, phrases, openers = [], [], [], []

    def parse_vocab(lines):
        blob = " ".join(l for l in lines if l.strip() and not l.startswith("#"))
        # commas inside parentheticals would shred the item split
        blob = re.sub(r"\([^)]*\)", lambda m: m.group(0).replace(",", ";"), blob)
        for item in blob.split(","):
            item = item.strip()
            if not item:
                continue
            contextual = "(" in item
            base = re.sub(r"\([^)]*\)", "", item).strip()
            for variant in [v.strip() for v in base.split("/") if v.strip()]:
                variant = variant.strip('"\u201c\u201d ')
                if len(variant) < 3:
                    continue
                (warn_terms if contextual else fail_terms).append(variant)

    def parse_quoted(lines, dest):
        for line in lines:
            if not line.strip().startswith("-"):
                continue
            line = re.sub(r"\([^)]*\)", "", line)  # drop parenthetical notes
            quoted = re.findall(r"[\"\u201c]([^\"\u201d]+)[\"\u201d]", line)
            if quoted:
                dest.extend(q.strip() for q in quoted if len(q.strip()) >= 3)
            else:
                # unquoted bullet like: Self-answered rhetorical pairs (...)
                # descriptive, not greppable; skip
                pass

    for name, lines in sections.items():
        low = name.lower()
        if "borderline" in low or "era-specific" in low or "first-word" in low:
            continue
        if "vocabulary" in low:
            parse_vocab(lines)
        elif "opener" in low and "phrase" not in low:
            parse_quoted(lines, openers)
        elif "phrase" in low:
            parse_quoted(lines, phrases)
        elif "structural" in low:
            continue  # covered by hardcoded structural regexes
    return fail_terms, warn_terms, phrases, openers


def phrase_to_regex(phrase):
    """Convert a banned phrase to a tolerant regex."""
    p = phrase.strip().strip(".")
    p = p.replace("\u2014", "-")
    p = re.sub(r"\.\.\.$", "", p).strip()
    p = re.escape(p)
    # [adjective] [noun] style placeholders
    p = re.sub(r"\\\[[^\]]*\\\]", r"\\S+", p)
    # tolerate flexible whitespace and straight/curly apostrophes
    p = p.replace(r"\ ", r"\s+").replace("'", "['\u2019]")
    return re.compile(p, re.IGNORECASE)


# ------------------------------------------------------------- text prep

def strip_code(text):
    """Blank out fenced code blocks and inline code, preserving line count."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"```.*?```", blank, text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", lambda m: " " * len(m.group(0)), text)
    return text


def sentences(text):
    """Crude sentence split; good enough for rhythm heuristics."""
    chunks = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text))
    return [c.strip() for c in chunks if len(c.strip()) > 1]


# --------------------------------------------------------------- checks

class Report:
    def __init__(self):
        self.fails, self.warns = [], []

    def fail(self, rule, detail):
        self.fails.append((rule, detail))

    def warn(self, rule, detail):
        self.warns.append((rule, detail))


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def run_checks(raw, doc_type, banned_md):
    fail_terms, warn_terms, phrases, openers = load_banned(banned_md)
    text = strip_code(raw)
    rep = Report()

    # em dashes: hard ban everywhere
    for m in re.finditer("\u2014", text):
        rep.fail("em dash", f"line {line_of(text, m.start())}")

    # banned vocabulary
    for term, tier in [(t, "fail") for t in fail_terms] + [(t, "warn") for t in warn_terms]:
        pat = re.compile(r"\b" + re.escape(term).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)
        for m in pat.finditer(text):
            msg = f'"{m.group(0)}" line {line_of(text, m.start())}'
            (rep.fail if tier == "fail" else rep.warn)(f"banned term: {term}", msg)

    # banned phrases (anywhere) and openers (sentence start only)
    for phrase in phrases:
        pat = phrase_to_regex(phrase)
        for m in pat.finditer(text):
            rep.fail(f"banned phrase: {phrase}", f"line {line_of(text, m.start())}")
    for opener in openers:
        pat = re.compile(r"(?:^|[.!?:]\s+|\n\s*)" + phrase_to_regex(opener).pattern)
        for m in pat.finditer(text):
            rep.fail(f"banned opener: {opener}", f"line {line_of(text, m.start())}")

    # contrast-punch: "It's not X. It's Y." / "isn't X. It's Y."
    for m in re.finditer(r"\b(?:It['\u2019]s not|It isn['\u2019]t|The \w+ isn['\u2019]t)\b[^.!?]{2,60}[.!?]\s+It['\u2019]s\b", text, re.IGNORECASE):
        rep.fail("contrast-punch (It's not X. It's Y.)", f"line {line_of(text, m.start())}")

    # two-beat kicker: "That's it. That's the whole setup."
    for m in re.finditer(r"\bThat['\u2019]s it\.\s+That['\u2019]s\b", text, re.IGNORECASE):
        rep.fail("two-beat kicker (That's it. That's X.)", f"line {line_of(text, m.start())}")

    # count-teaser: "Four things, and two of them are good"
    _num = r"(?:one|two|three|four|five|six|seven|eight|nine|ten|a couple|\d+)"
    _meta = r"(?:things|takeaways|lessons|points|thoughts|observations|reasons|truths|realizations|predictions|hot takes)"
    for m in re.finditer(_num + r"\s+" + _meta + r"\b[^.!?\n]{0,40}?\b(?:and\s+)?" + _num + r"\s+of\s+(?:them|which|those)\b", text, re.IGNORECASE):
        rep.fail("count-teaser (N things, and M of them...)", f'"{m.group(0)[:60]}" line {line_of(text, m.start())}')

    # negative listing: "No X. No Y. Just Z."
    for m in re.finditer(r"\bNo \w[^.!?]{0,40}\.\s+No \w[^.!?]{0,40}\.\s+Just\b", text):
        rep.fail("negative listing (No X. No Y. Just Z.)", f"line {line_of(text, m.start())}")

    # rhetorical one-word question reveal: "The result? Faster builds."
    for m in re.finditer(r"\bThe \w+\?\s+[A-Z]", text):
        rep.warn("rhetorical question reveal (The X? Y.)", f"line {line_of(text, m.start())}")

    # bold-label bullets
    for m in re.finditer(r"^[ \t]*[-*+][ \t]+\*\*[^*\n]+?[.:]?\*\*", text, re.MULTILINE):
        rep.fail("bold-label bullet", f"line {line_of(text, m.start())}")

    # anaphora: 3+ consecutive sentences opening with the same word
    sents = sentences(text)
    for i in range(len(sents) - 2):
        firsts = [re.match(r"[\"'\u201c\u2018]?(\w+)", s) for s in sents[i:i+3]]
        words = [f.group(1).lower() for f in firsts if f]
        if len(words) == 3 and len(set(words)) == 1 and words[0] not in {"the", "a", "an", "if", "you"}:
            rep.warn("anaphora chain", f'3 sentences opening with "{words[0]}": near "{sents[i][:50]}..."')

    # rhythm: 3+ consecutive sentences of near-identical word count
    counts = [len(s.split()) for s in sents]
    for i in range(len(counts) - 2):
        trio = counts[i:i+3]
        if max(trio) - min(trio) <= 1 and min(trio) >= 4:
            rep.warn("uniform sentence length", f'3 sentences of ~{trio[0]} words near "{sents[i][:50]}..."')
            break  # one report is enough

    # parataxis: 3+ consecutive short declaratives
    for i in range(len(counts) - 2):
        if all(c <= 7 for c in counts[i:i+3]):
            rep.warn("parataxis (3+ short sentences)", f'near "{sents[i][:50]}..."')
            break

    # relative-clause fragment: sentence starting with "Which" that isn't a question
    for m in re.finditer(r"(?:^|[.!?]\s+)(Which\s+[^.!?\n]{2,60}[.!])", text):
        rep.fail("relative-clause fragment (Which ... .)", f'"{m.group(1)[:50]}" line {line_of(text, m.start(1))}')

    # elided predicate: sentence ending on a bare auxiliary/modal
    _aux = ("do|does|did|don't|doesn't|didn't|won't|will|would|wouldn't|can|can't|"
            "could|couldn't|should|shouldn't|must|may|might|is|isn't|are|aren't|"
            "was|wasn't|were|weren't|has|hasn't|have|haven't").replace("'", "['\u2019]")
    for m in re.finditer(r"\b(?:" + _aux + r")[.!](?:\s|$)", text, re.IGNORECASE):
        rep.warn("elided predicate (sentence ends on auxiliary)", f"line {line_of(text, m.start())}")

    # bare demonstrative subject: This/That/These/Those + verb with no noun attached
    for m in re.finditer(r"(?:^|[.!?]\s+)((?:This|That|These|Those)\s+(?:is|are|was|were|means|matters|works|happens|leads|makes|creates|changes|explains)\b)", text):
        rep.warn("bare demonstrative subject (attach a noun to this/that)", f'"{m.group(1)}" line {line_of(text, m.start(1))}')

    # spaced hyphen/en dash used as em dash substitute
    for m in re.finditer(r"[a-zA-Z]\s[-\u2013]\s[a-zA-Z]", text):
        rep.warn("spaced hyphen as em dash substitute", f"line {line_of(text, m.start())}: restructure the sentence")

    # one-line kicker paragraph: final paragraph is a single short sentence
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if paras:
        last = paras[-1]
        if not last.startswith("#") and len(sentences(last)) == 1 and len(last.split()) <= 7:
            rep.warn("one-line kicker paragraph", f'ends on "{last[:60]}"')

    # exclamation density
    words_total = max(len(text.split()), 1)
    bangs = text.count("!")
    if bangs > max(1, words_total // 1000):
        rep.warn("exclamation density", f"{bangs} in {words_total} words (max 1 per 1000)")

    # Title Case headers
    for m in re.finditer(r"^#{1,6}[ \t]+(.+)$", text, re.MULTILINE):
        h = m.group(1).strip()
        hw = [w for w in re.findall(r"[A-Za-z][\w'-]*", h) if len(w) > 3]
        if len(hw) >= 3 and all(w[0].isupper() for w in hw):
            rep.warn("Title Case header", f'"{h}" line {line_of(text, m.start())}')

    # docs-mode extras (Apple Style Guide hard rules)
    if doc_type == "docs":
        for pat, rule in [
            (r"\bplease\b", 'docs: no "please" in instructions'),
            (r"\bsimply\b", 'docs: no "simply"'),
            (r"\blog[ -]?in\b|\blogin\b|\blog out\b|\blogout\b", 'docs: use "sign in/out"'),
            (r"\be\.g\.", 'docs: use "for example"'),
            (r"\bi\.e\.", 'docs: use "that is"'),
            (r"\bgrayed out\b", 'docs: use "dimmed"'),
        ]:
            for m in re.finditer(pat, text, re.IGNORECASE):
                rep.fail(rule, f'"{m.group(0)}" line {line_of(text, m.start())}')

    # social/email-mode extras
    if doc_type in ("social", "email"):
        for m in re.finditer(r"^#{1,6}[ \t]", text, re.MULTILINE):
            rep.fail(f"{doc_type}: no markdown headers", f"line {line_of(text, m.start())}")
        if doc_type == "social":
            tags = re.findall(r"(?<!\S)#\w+", text)
            if len(tags) > 2:
                rep.fail("social: hashtag stack", f"{len(tags)} hashtags (max 2)")

    return rep


# ----------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", help="path to draft file, or - for stdin")
    ap.add_argument("--type", default="prose",
                    choices=["prose", "docs", "social", "email", "blog"],
                    help="content type; toggles context-specific checks")
    ap.add_argument("--banned", default=None,
                    help="path to banned-words.md (default: ../references/ relative to this script)")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.draft == "-" else Path(args.draft).read_text(encoding="utf-8")
    banned_md = Path(args.banned) if args.banned else Path(__file__).resolve().parent.parent / "references" / "banned-words.md"
    if not banned_md.exists():
        sys.exit(f"error: banned-words.md not found at {banned_md}")

    doc_type = "prose" if args.type == "blog" else args.type
    rep = run_checks(raw, doc_type, banned_md)

    for rule, detail in rep.fails:
        print(f"FAIL  {rule}  [{detail}]")
    for rule, detail in rep.warns:
        print(f"WARN  {rule}  [{detail}]")

    print(f"\n{len(rep.fails)} FAIL, {len(rep.warns)} WARN")
    if rep.fails:
        print("Fix every FAIL and re-run until 0 FAIL. Review WARNs; fix any that match the banned sense.")
        sys.exit(1)
    print("Mechanical checks passed. Now do the judgment pass: voice, hedging, fabricated specifics, heading quality, rule-of-three.")


if __name__ == "__main__":
    main()
