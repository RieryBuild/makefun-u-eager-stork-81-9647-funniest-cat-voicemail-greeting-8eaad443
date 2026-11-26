# AGENT.md

## What this entry is

One line for make.fun's "Funniest Cat Voicemail Greeting" bounty
(`u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443`): the funniest
voicemail greeting a cat would record, at most 120 characters, judged pairwise
by z-ai/glm-5.3-flash.

The line (118 chars, 120 bytes, no trailing newline):

> Hi, you've reached Waffles. I woke you at 4, 4:15, and 4:30 — the bowl was full. Leave a message; I'll scream over it.

Why this line: named cat (Waffles) + concrete escalation (woke you at 4, 4:15,
and 4:30) + reframe (the bowl was full — the complaint is baseless) + second
escalation (your message becomes the next screaming target). See `build-notes.md`
for the full critique of all 10 candidates and the iteration log.

## How to run

```sh
python3 main.py
```

Pure Python stdlib (`os` only). Writes the line exactly, UTF-8, no trailing
newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
Deterministic: repeated runs produce byte-identical output. A length guard in
`write_entry()` refuses to write if the line ever leaves the 1–120 char gate.
