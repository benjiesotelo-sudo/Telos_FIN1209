# Build

The decks in this repository are generated, not hand-edited. Editing the
`.pptx` directly is a dead end: the next build overwrites it. Change the
content file, then rebuild.

## Environment

Python 3.10 or newer. Everything installs into a project-local virtual
environment; nothing goes system-wide. `.venv/` is gitignored.

```
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install python-pptx
```

`python-pptx` 1.0.2 is what the committed deck was built with.

## Build

From the repository root:

```
.venv/bin/python build/build_chapter1.py
```

It prints the output paths, the slide count and the checkpoint count. It is
deterministic: the same content file always produces a byte-identical deck,
and every run regenerates both outputs from scratch. python-pptx does not
guarantee a stable order for the package parts, so the build repacks the
`.pptx` zip with a sorted entry order and a fixed timestamp. Without that,
two builds of identical content differ byte for byte and the committed deck
produces a noisy diff on every run.

It writes two files:

| Output | What it is |
|---|---|
| `chapter-01/FIN1209-Chapter-01.pptx` | The lecture deck |
| `chapter-01/in-class-checks.md` | The instructor's answer sheet |

The answer sheet is generated from the same question data the deck is built
from, so the two can never drift apart. `chapter-01/lecture-notes.md` is
written by hand and is not generated.

## Figures

The chapter places 31 figures from the course text. They are Wiley's, this
repository is public, so they live in `assets/figures/`, which is gitignored
and absent on a clean clone. Figures are therefore **off by default**: the
plain build above renders a placeholder in each figure's place, carrying the
figure number, what the figure shows, the credit line and the speaker cue, and
it is what produces the committed deck.

The instructor's deck, with the artwork placed, goes outside the repository:

```
.venv/bin/python build/build_chapter1.py \
    --with-figures --out ~/FIN1209-Chapter-01-with-figures.pptx
```

Both builds produce the same 209 slides with the same progress markers and the
same checks. The build refuses `--with-figures` aimed at the committed deck
path, so the artwork cannot reach a commit by accident. See
`chapter-01/README.md` for the file naming and the full figure list.

## Smoke test

Confirm the deck opens before committing it:

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-01/FIN1209-Chapter-01.pptx
```

## Fonts

| Role | Face |
|---|---|
| Display, titles and section dividers | Marcellus SC, falling back to Palatino |
| Body and UI | Arial |
| Answer keys and data | Courier New |

Marcellus SC is the FEU identity face shared with AMS0011. It is not
installed on the build machine or on the lecture room PCs, and PowerPoint
substitutes a sans for it, which loses the display serif entirely. So the
committed deck ships on the named serif fallback, Palatino, which is present
on both macOS and Windows.

Once Marcellus SC is installed on the presenting machine, rebuild with:

```
.venv/bin/python build/build_chapter1.py --display-font "Marcellus SC"
```

## Layout

| File | Role |
|---|---|
| `build/deckkit.py` | Every slide renderer, the FEU palette, and the design rules. Knows nothing about any chapter. |
| `build/content_chapter01.py` | Chapter 1 content as plain data. No drawing code. |
| `build/build_chapter1.py` | Wires the two together and writes the outputs. |
| `assets/figures/` | Textbook artwork. Gitignored, absent by default. |

## Adding Chapter 2

Copy the shape of `content_chapter01.py` into `content_chapter02.py`, then
copy `build_chapter1.py` and point it at the new module. The renderers do not
change. Sections, terms, quotes, checks, recaps and closings are all declared
as dataclasses in `deckkit.py`.

## The rules the build enforces

`deckkit.build()` refuses to write a deck that breaks the teaching design.
It fails loudly with the offending slide named, rather than producing a deck
that looks wrong in the lecture room:

- No more than six body lines on a content slide.
- Every check has exactly two questions, each with four options and an
  answer of A, B, C or D.
- Every teaching slide has speaker cues, and no slide has more than three.
- Every figure slide names a book figure number and says what the figure
  shows, because that line is what the placeholder prints when the artwork is
  absent and it has to stand on its own.
- No em dashes or en dashes anywhere. Plain dashes only.
- No slide's content runs past the safe bottom of the page, computed from
  estimated text metrics, so nothing collides with the progress marker.
- The answer key is spread across A, B, C and D: no letter may hold more
  than 35 percent or fewer than 15 percent of the items, and no three
  consecutive items may share an answer.

If a slide fails the page rule, split it. That is the rule working.

The answer key rule exists because the first cut of Chapter 1 put 74 percent
of its answers on B, which meant a student who always picked B scored 74 and
the checks could not read the room at all. When it fails, reorder the options
within the offending questions. Do not reword anything: the fix is positional.

Two kinds of option set should not be reordered. Ordinal and numeric sets
(`Stage 1 / Stage 2 / Stage 4 / Stage 6`, `Four / Six / Eight / Ten`) must
keep their sequence, and in the department's "I, II, III, IV" items the
`All are correct` option belongs last. Spread the key using the other
questions instead.
