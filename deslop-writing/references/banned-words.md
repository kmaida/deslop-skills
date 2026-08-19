# Banned Words, Phrases, and Openers

These are statistically overrepresented in AI-generated text across multiple studies (Carnegie Mellon 2025, Wikipedia Signs of AI Writing, Buffer 52M post analysis), and they read as filler: they add words without adding meaning. Never use any of these. Replace with concrete alternatives or restructure the sentence.

## Banned Vocabulary

delve / delves / delving, tapestry, landscape (figurative), testament (e.g. "a testament to"), vibrant, pivotal, crucial, intricate / intricacies, meticulous / meticulously, bolster / bolstered, garner / garnered, underscore / underscores, interplay, multifaceted, nuanced (as filler), foster / fostering, leverage (as verb), utilize (say "use"), commence (say "start"), facilitate, encompass / encompassing, paramount, groundbreaking, cutting-edge, game-changing / game-changer, transformative, revolutionise / revolutionize, seamless / seamlessly, robust (outside engineering), comprehensive (describing own output), endeavour / endeavor, aforementioned, harnessing, spearheading, navigating (figurative), showcasing, highlighting, emphasizing, enhancing, unprecedented, remarkable, stunning, profound, epic (non-literal), in essence, thought leader / thought leadership, synergy / synergies, pain points, value add / value proposition (casual contexts), moving forward, touch base / circle back, rest assured, it goes without saying, footgun, load-bearing (figurative), deep dive / deep-dive, table stakes, non-trivial, battle-tested, north star (figurative), first-class citizen, surface (as verb, e.g. "surfaces insights"), critical (as filler emphasis, not severity ratings), key (as adjective: "key insight," "key takeaway"), boasts, ecosystem (figurative), unpack / unpacking (figurative), arguably, in many ways, in some sense, to some extent

## Banned Phrases

- "In today's [adjective] [noun]..."
- "It's worth noting that..."
- "It's important to note that..."
- "Let's dive in" / "Let's dive deeper" / "Let's delve into"
- "At its core..."
- "In the realm of..."
- "When it comes to..."
- "A testament to..."
- "Not just X, but Y"
- "It's not just about X — it's about Y"
- "This is where X comes in"
- "Whether you're a [X] or a [Y]..."
- "From X to Y" (range opener)
- "At the end of the day..."
- "The bottom line is..."
- "Here's the thing..."
- "Here's the deal..."
- "Without further ado..."
- "In a nutshell..."
- "Buckle up"
- "Take it to the next level"
- "Unlock the power of..."
- "Empower / empowering"
- "Elevate your..."
- "Streamline your..."
- "Supercharge your..."
- "Bridge the gap"
- "Move the needle"
- "In conclusion"
- "Overall," (paragraph starter)
- "Firstly... Secondly... Thirdly..."
- "I hope this helps"
- "I hope this finds you well"
- "I hope this email finds you well"
- "As per my last email"
- "Please don't hesitate to reach out"
- "Here's the kicker"
- "The result?" (rhetorical question + one-line answer)
- "It's not X. It's Y."
- "No X. No Y. Just Z."
- "Ultimately," (paragraph starter)
- "Double-edged sword"
- "Silver bullet" / "No silver bullet"
- "Perfect storm"
- "The elephant in the room"
- "Swiss Army knife" (figurative)
- "What nobody tells you..." / "Here's what nobody tells you"
- "The part everyone misses"
- "What most people get wrong"
- "This is the part most people skip"
- "What if I told you..."
- "Plot twist:"
- "Think about it:"
- Self-answered rhetorical pairs ("Question? Answer.")
- "Marks a pivotal moment"
- "Plays a vital role" / "plays a crucial role"
- "Solidifies its position"
- "Stands as a testament"
- "Experts agree" / "studies show" / "research shows" / "industry reports suggest" / "many argue" / "widely regarded as" (name the source or cut the claim)
- "Serves as a..." (say what it is or does: "is," "tracks," "stores")
- "Let that sink in"
- "Read that again"
- "Full stop" (as emphasis)
- "What's your take?"
- "Curious what others think" / "Curious to hear your thoughts"
- "Let me know in the comments" / "Drop a comment"
- "Sound familiar?"

## Banned Sentence/Paragraph Openers

- "Certainly,"
- "Absolutely,"
- "Sure,"
- "Great question!"
- "That's a great point!"
- "I'd be happy to..."
- "As an AI..."
- "As a language model..."
- "However, it's important to..."
- "Moreover,"
- "Furthermore,"
- "Additionally,"
- "Interestingly,"
- "Notably,"
- "Importantly,"
- "Indeed,"

## Claude-Specific Tells

Claude's slop profile differs from ChatGPT's: fewer "delve"-class words, more manufactured candor, dramatic framing devices, and formatting habits. Ban all of the following.

### Vocabulary

genuinely (as intensifier: "genuinely useful," "genuinely hard"), quietly (as praise: "quietly one of the best"), "heavy lifting" (figurative: "does a lot of the heavy lifting"), under the hood, through-line, crisp / punchy / tight / clean / elegant (as praise for writing, code, or ideas), sharp (as praise: "a sharp observation"), compelling, resonate / resonates, lands / landed (figurative: "the point lands"), worth noting / worth flagging / worth calling out / worth a look, flag / flagging (meaning "to mention"), tension (as framing: "there's a real tension here"), at scale (filler)

### Phrases

- "Honestly," / "Frankly," (openers)
- "Let me be direct" / "I'll be honest" / "The honest answer is..."
- "To be clear," / "To be fair,"
- "The short answer is X. The longer answer..."
- "This is where it gets interesting"
- "Think of it as..." / "Think of it like..."
- "Not because X, but because Y"
- "Two things can be true"
- "which is exactly the point" / "That's the whole point"
- "In practice," (paragraph opener)
- "The real question is..."
- "That said," (transition)
- "A few things stand out" / "A couple of things worth mentioning"
- "Here's why that matters" / "This matters because..."
- "The catch:" / "The trade-off:" (dramatic setup labels)
- "You're absolutely right" / "Great catch" / "That's a sharp observation" (validation openers)
- "This is deliberate" / "That's by design" / "This is intentional" (significance-announcing)
- "This distinction matters" / "The distinction is subtle but important"
- "Note that..." / "Note the..." (openers)
- "Want me to...?" / "Happy to..." (next-step offer closers in ghostwritten text)

### Structural habits

- Bold-label bullets: `**Label.** Explanation sentence.` or `**Label:** explanation` — Claude's single most recognizable formatting pattern
- One-line dramatic kicker paragraphs ("That's it. That's the fix.")
- Anaphora chains ("It means X. It means Y. It means Z.")
- "A few thoughts:" followed by a numbered list
- Manufactured candor: announcing honesty or directness instead of just being direct
- Self-annotating significance: stating something, then narrating that it was on purpose or that it matters ("X is Y. This is deliberate:", "That's by design."). If the choice matters, give the reason itself; the reader doesn't need to be told a choice was a choice

## Borderline Patterns (do not ban outright)

AI overuses these, but plenty of humans use them naturally: "simply" and "just" as minimizers, "chances are," "the good news is / the bad news is," "pro tip:", "spoiler:". Keep them when they match the writer's established voice or their writing guide permits them. A writing guide always wins over this list. Treat them as slop only when there's no voice evidence and they're doing filler work.

## Model-Specific First-Word Habits (vary your openers)

ChatGPT tends to start with: "as," "yes," "sure," "here," "in," "to," "creating," "certainly," "title," "the"
Claude tends to start with: "in," "from," "this," "how," "yes," "title," "according," "the," "based," "here"
Grok tends to start with: "step," "introduction," "yes," "creating," "to," "title," "in," "certainly"
Gemini tends to start with: "my," "creating," "while," "here," "yes," "this," "the"
DeepSeek tends to start with: "based," "yes," "step," "comprehensive," "here," "to," "creating," "title," "certainly"

## Era-Specific AI Vocabulary (for context)

2023–mid 2024 (GPT-4 era): additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, interplay, key, landscape, meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant

Mid 2024–mid 2025 (GPT-4o era): align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant

Mid 2025 onward (GPT-5 era): emphasizing, enhance, highlighting, showcasing
