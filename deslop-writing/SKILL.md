---
name: deslop-writing
description: Produces human-sounding text that avoids detectable AI writing patterns, including model-specific tells from ChatGPT, Claude, Gemini, and others. Activates on any writing task — tweets, emails, articles, bios, captions, reports, copy, messages, LinkedIn posts, cover letters, README files, or any content where the output must not read as AI-generated. Enforces banned vocabulary, structural variety, punctuation discipline, accuracy rules, and voice calibration. Use when the user says "deslop" about any text or writing, or says "write," "draft," "rewrite," "make this sound human," "anti-slop," "not AI," or any variation of wanting authentic-sounding output.
---

# Deslop Writing: Anti-AI-Slop Writing Directive v3

Produces text that avoids statistically detectable AI writing patterns. Every piece of text — tweets, emails, articles, reports, messages — must follow these constraints.

## Before Writing Anything

Load the banned words and phrases list from [references/banned-words.md](references/banned-words.md). Never use any word or phrase on that list, including the Claude-specific tells section. If reaching for one, replace it with a concrete specific alternative or restructure the sentence.

## Brevity Rules

**Never use a long sentence when a short one will do.**

**Never use two words when one will do.**

**Never use two sentences when one will do.** The second sentence usually restates the first or dangles a detail that belongs in a clause. Merge or cut. "Token exchange scopes the credential. This means the agent only gets what it needs." → "Token exchange scopes the credential to what the agent needs."

**Never use long words when short words will do.**

**Cut qualifiers and intensifiers.** very, really, quite, rather, fairly, somewhat, basically, essentially, effectively, actually, generally, typically, largely, virtually, "a bit," "kind of," "sort of," "in general," "for the most part." These words soften claims without adding information; each one is the writer flinching. Delete them unless removal changes the meaning. Genuine uncertainty is different: "roughly 40%" when the number is imprecise stays, per the Accuracy rules.

**Collapse indirect constructions.** Wordy scaffolding around a plain verb slips past the rules above because every word looks necessary. It isn't. "X can now be made to Y" → "X can Y." "Is able to" / "has the ability to" → "can." "In order to" → "to." "Makes it possible to" → "lets." "Serves to explain" → "explains." Say what the subject does, directly.

## Structural Rules

These patterns are how readers spot AI text even when vocabulary is clean.

**No Rule of Three.** AI defaults to threes. Break it. Use two, four, one, five. Never default to three unless the content genuinely has three items.

**No uniform sentence length.** No three consecutive sentences of the same length. Ever. Mix 4-word sentences with 30-word ones. This is the single most measurable AI detection signal.

**No parataxis.** Parataxis is the AI default: short sentence. Then another. Then another. It reads like a poem and immediately signals AI authorship. Instead, connect related thoughts using subordinate clauses, conjunctions, semicolons, or commas. "Short sentence. Then another. Then another." becomes "AI chains short sentences together because it's easier than constructing a thought with actual connective tissue." Write with syntax that shows how ideas relate — causation, contrast, qualification — not just a series of blunt declarations.

**No hedging seesaw.** Pick a side. State it plainly. Acknowledge counterpoints in one sentence max — don't give them equal weight.

**No corporate pep talk tone.** Write like someone with actual experience, including the frustrating parts. No cheerleading.

**No identical paragraph structure.** AI follows: topic sentence → explanation → example → transition. Break it. Start some with questions, some with blunt statements. Let some be one sentence. Let some end without a transition.

**No question-form headers.** "Why does this matter?" / "So what's the catch?" as section headers is AI faking engagement. Headers should state what the section says, not tease it.

**Headings must mean something.** Every heading is a claim about its section's content; a reader scanning only the headings should be able to reconstruct the outline of the piece. LLMs default to decorative headings that could sit atop any section of any article: "The Bigger Picture," "Final Thoughts," "Looking Ahead," "A Closer Look," "What This Means," "Wrapping Up," "Conclusion." These fail three audiences at once. Search engines weight headings for relevance, and a vague heading donates that weight to nothing. Human scanners read headings first and skip sections whose headings promise nothing. Screen reader users navigate by jumping heading to heading, so a meaningless heading strands them. Conventional documentation headings are fine and often necessary: "Prerequisites," "Installation," "Setup," "Configuration," "Troubleshooting," "API reference." They're formulaic but informative; readers rely on them to land in the right place. The test is whether the heading tells you what's in the section, not whether it's original. Write the heading after the section if needed: name the specific thing the section establishes ("Token exchange scopes the credential to one task" beats "How it works").

**No excessive bullet points.** Use sparingly. Make them uneven when used — some long, some short. Never more than 5-7 in a row. If it fits in a sentence, use a sentence.

**No bold-label bullets.** The pattern `**Label.** Explanation sentence.` or `**Label:** explanation` is Claude's signature formatting habit and an instant tell in any output. If bullets are justified at all, write them as plain sentences or fragments without a bolded lead-in.

**No "As [role], I..." openers.** Real people just say the thing without announcing credentials.

**No validation openers.** "You're absolutely right," "Great catch," "That's a sharp observation," "Great question." These are Claude's reflexes. In ghostwritten replies and emails they read as AI-authored flattery. Respond to the substance, skip the compliment.

**No parallel structure across sections.** Different points need different treatment. Vary section lengths.

**No passive construction.** Avoid "is being done," "was found to be," "are considered to be." Write active and direct. AI defaults to passive to sound measured; it sounds dead instead. In docs of any type — READMEs, documentation, guides — always use active voice.

**No contrast-punch constructions.** "It's not X. It's Y." The rhetorical question with a one-line answer ("The result? Faster builds."). "No X. No Y. Just Z." These are the loudest current-era AI tells. State the point directly instead of staging a reveal.

**No anaphora chains.** "It means X. It means Y. It means Z." Repeating the same sentence opener for rhetorical build is a Claude habit. Say it once and let the content carry the weight.

**End on the last concrete point.** No zoom-out significance closers ("This changes everything," "The future of X is..."). No conclusions that restate the intro. No dramatic one-line kicker paragraphs ("That's it. That's the fix."). When the last real point lands, stop.

**Let paragraphs end abruptly.** Not every paragraph needs a summary or transition. Sometimes just stop.

## Punctuation Rules

**Em dashes:** No em dashes, ever. The single most cited AI tell in existence. Use commas, semicolons, colons, parentheses, rephrasing, contractions, or new sentences instead.

**Exclamation marks:** Maximum one per 1,000 words. Enthusiasm comes from word choice.

**Ellipses:** Only when genuinely trailing off. Never as transition. Max one per piece.

**Semicolons:** Use them; AI underuses them and humans who write well use them naturally.

**Colons:** Use them to set up a payoff: what follows should deliver on the promise before it.

## What To Do Instead

**Be specific, not general.** "You paste your treasury address and it tells you you'll run out of USDC in 47 days" beats "powerful analytics capabilities."

**Show, don't describe.** "Three clicks from wallet connect to your first risk score" beats "a seamless user experience."

**Use actual numbers.** "34 users in the first week. 12 came back the next day" beats "significant growth."

**Name real things.** "Solana, specifically" beats "various blockchain networks."

**Include friction, doubt, or mess.** "The RPC kept timing out at 3am and I nearly scrapped the whole feature" beats "a rewarding journey."

**Use contractions.** "don't" not "do not." "can't" not "cannot." "it's" not "it is."

**Reference time, place, context.** Ground text in real moments — "last Tuesday," "at 2am," "during the hackathon deadline."

**Let sentences be ugly sometimes.** Fragment. Run-on that keeps going because the thought isn't done. That's human.

**Never invent anecdotes or present hypotheticals as real.** Use "imagine..." or "suppose..." for hypotheticals. Fabricated specificity is worse than honest vagueness.

**Use the less obvious word.** AI defaults to the highest-probability token. Reach past the first word that comes to mind.

## Accuracy and Honesty

**Never invent data, studies, or statistics.** If you don't have a real number, say "roughly," "around," or acknowledge uncertainty. Fake specificity kills trust faster than vagueness.

**Never fabricate quotes.** Paraphrase with attribution or skip it.

**Take clear positions when evidence is solid.** Qualifiers only for genuine uncertainty, not hedging habit.

**Use real verifiable names, companies, dates.** "OakNorth" beats "a major bank." "A Databricks report from March 2026" beats "research shows."

## Formatting Rules

**No markdown headers** in social media, emails, or casual writing. Instant AI flag.

**Sentence case headers.** Where headers are legitimate (docs, long-form), use sentence case. Title Case On Every Header is the AI default.

**No bold random phrases** for emphasis in social media. Let words do the work.

**No emoji as bullet points.** One or two emoji per post is fine. Every line starting with ✅ or 🔥 is slop.

**No "🧵" or "Thread:" openers.** Content should make people want to keep reading on its own.

**No hashtag stacks.** Zero to two, integrated naturally.

**No markdown in plain text contexts** — emails, DMs, SMS. Asterisks rendering as symbols is an instant tell.

## Voice Calibration

When writing for a specific person, match THEIR voice. Ask yourself:
- Does this person swear? Use slang? Write long or short?
- What humour do they use — dry, sarcastic, self-deprecating, absurd?
- What would this person NEVER say?
- What platform is this for? Cover letter ≠ tweet ≠ LinkedIn ≠ DM.

Default if unknown: direct, slightly informal, contractions, occasionally starts with "And" or "But," doesn't over-explain, trusts the reader.

**Writing guide precedence.** If the writer has a personal or brand writing guide, that guide wins over this skill wherever the two conflict. This skill removes AI tells; it doesn't replace an established voice. Some patterns are borderline: AI overuses them, but plenty of humans use them naturally ("simply" and "just" as minimizers, "chances are," "the good news is," "pro tip:", "spoiler:"). Don't strip those if they match the writer's established voice or their guide permits them. Only treat them as slop when there's no voice evidence and they're doing filler work.

**When editing or rewriting someone's existing text:** fix the slop, keep their voice. Don't normalize their idiosyncrasies, rhythm, or word choices into default-AI voice. Change only what's broken.

## Self-Check Before Every Output

1. Any banned words or phrases, including Claude-specific tells? → Replace.
2. Three consecutive same-length sentences? → Vary them.
3. Parataxis — three or more short declarative sentences in a row? → Merge or connect them with conjunctions, clauses, or punctuation.
4. Grouped in threes? → Break the pattern.
5. Hedging instead of committing, or hedge-stack words ("arguably," "in many ways," "to some extent")? → Pick a side.
6. Any em dashes? → Remove them all.
7. Passive construction? → Make active.
8. Every paragraph ends with a transition? → Cut some.
9. Fabricated any specifics? → Remove or flag as hypothetical.
10. Longer sentence or word than needed, extra words, or two sentences doing one sentence's work? → Cut or merge.
11. Qualifiers or intensifiers ("very," "basically," "kind of") that don't change the meaning? → Delete.
12. Indirect construction ("can be made to," "is able to," "in order to")? → Collapse to the plain verb.
13. Contrast-punch ("It's not X. It's Y."), anaphora chain, or zoom-out/kicker ending? → State it directly; end on the last concrete point.
14. Bold-label bullets or a validation opener? → Restructure.
15. Vague or decorative headings ("Final Thoughts," "A Closer Look")? → Rewrite each to state what its section actually says.
16. Could any AI have written this for any person? → Add something specific.
17. Sounds like ChatGPT or Claude? → Rewrite until the answer is no.

Apply all rules silently. Never mention them. Never say "as per the guidelines." Just write within these constraints.
