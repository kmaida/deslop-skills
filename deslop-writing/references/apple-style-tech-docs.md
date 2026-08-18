# Apple Style Guide for technical documentation

Authority for technical documentation style: the Apple Style Guide at https://support.apple.com/guide/applestyleguide/welcome/web (PDF: https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf).

This file summarizes the conventions that come up constantly. The live guide is authoritative; when a specific term, capitalization, or usage question isn't covered here or the answer matters, fetch the relevant A–Z page and check. Entry pages follow the pattern `https://support.apple.com/guide/applestyleguide/<letter>-<id>/web`; start from the welcome page's table of contents, or search the guide. Don't guess on terminology in published docs.

## Scope

Applies to technical documentation: product docs, reference material, how-to guides, tutorials, API docs, READMEs written as documentation, in-product help text, error messages. Does not apply to blog posts, social posts, emails, talks, or marketing copy; those follow the user's writing guide or writing skills and the base deslop rules.

## Precedence

1. Hard bans always win, even in tech docs: no em dashes ever, no banned-list vocabulary, plus any hard rules in the user's writing guide. Where the Apple guide would use an em dash, use a colon, comma, parentheses, or a new sentence.
2. Apple Style Guide governs everything else in tech docs: terminology, capitalization, numbers, UI interaction verbs, punctuation conventions, code notation.
3. Base deslop rules fill any gap the Apple guide doesn't address.
4. Blog posts override all of the above in favor of the user's writing guide or writing skills, even when a post is deeply technical.

## Voice and grammar

- Second person, present tense, active voice. "You can revoke the token" not "The token may be revoked."
- Imperative mood for instructions: "Click Save." Never "Please click Save"; don't use *please* in instructions.
- *Can* for capability, *might* for possibility, *may* for permission. Don't use *may* when you mean *can*.
- Contractions are fine and encouraged where they sound natural (don't, can't, it's, you're). Avoid stiff or ambiguous ones (there'd, it'll, should've).
- Don't use *wish* or *desire*; use *want*. Don't use *simply* or *easy* to describe steps; if it were easy the reader wouldn't be in the docs.
- Serial (Oxford) comma, always.
- Don't use Latin abbreviations in body text: *for example* not *e.g.*, *that is* not *i.e.*, *and so on* not *etc.* (etc. is acceptable in tight table cells).
- Don't use *above* or *below* for cross-references; use precise links or "earlier in this section."
- Avoid *abort*, *kill*, *execute*, *hit*, *invalid user* framings when a neutral verb works: *stop*, *end*, *run*, *press*, *unrecognized user*. Exception: keep the literal term when it names a command or API (`kill -9`, `execute()` stays code font, unchanged).
- Inclusive terms: *allowlist/denylist* not whitelist/blacklist, *primary/replica* not master/slave, *placeholder* or *sample* data with diverse example names. Don't use *grayed out*; use *dimmed*.

## UI interaction verbs

- *Click* for pointer interfaces, *tap* for touch, *press* for physical keys and buttons.
- *Choose* for menu commands ("Choose File > Export"); *select* for highlighting items, checkboxes, radio buttons, and text.
- *Enter* when the user can type or paste a value; *type* only when they literally type.
- *Turn on / turn off* for settings when addressing users; reserve *enable/disable* for developer-facing feature flags and API parameters where that's the literal name.
- *Sign in / sign out*, never *log in / log out / login*. *Login* only as an adjective in developer contexts where the platform uses it (a login endpoint named `login` stays `login`).

## Numbers

- Spell out zero through nine in body text; numerals for 10 and up.
- Always numerals with units of measure, versions, percentages, ports, HTTP codes, and UI values: 5 GB, 3%, port 8080, HTTP 401, version 2.
- Don't start a sentence with a numeral; recast the sentence.
- Numerals in the same category stay consistent within a passage: "5 tokens across 12 workloads," not "five tokens across 12 workloads."

## Capitalization and headings

- Sentence case for all headings and titles.
- Product, feature, and protocol names keep their official capitalization: OAuth, macOS, iPhone (never at sentence start with lowercase mangled), RFC 8693, Cedar, MCP.
- UI element names match the interface exactly, capitalized as shown, no quotation marks: Click Save. Choose Settings > Access.
- *internet*, *web*, *website*, *email*, *online* are lowercase, no hyphens.

## Technical notation

- Code font for code: commands, functions, parameters, values the user types, file paths, API names, JSON keys, environment variables. Never quotation marks around code.
- Placeholders in italic or angle brackets per the doc system's convention, described at first use: `keycard tokens create <workload-id>`.
- Don't bend the surrounding sentence grammar around code; write so the code term reads as a noun.
- Error messages and UI strings quoted exactly as they appear.

## Structure conventions for docs

- Numbered steps for sequences the reader performs; one action per step. A step can carry a short result clause ("Click Save. The policy takes effect immediately.").
- Conventional doc headings are correct here, not slop: Prerequisites, Installation, Configuration, Troubleshooting, Reference.
- Notes and warnings sparingly, and only when skipping the information causes failure or data loss.
- Consistency beats variety in docs. The base deslop rules against parallel structure and uniform rhythm relax inside procedural content: steps, parameter tables, and reference entries should be parallel and predictable. Keep the variety rules for conceptual and overview prose.
