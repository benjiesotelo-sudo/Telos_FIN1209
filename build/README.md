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
.venv/bin/pip install python-pptx matplotlib
```

`python-pptx` 1.0.2 and `matplotlib` 3.9.4 are what the committed deck was
built with. matplotlib draws the nine charts this course owns; see **Charts**
below for why they are generated rather than committed as images, and for the
one consequence that has for reproducibility.

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
from, so the two can never drift apart.

## Two editions of the deck

The same content file produces both. There is no second content module and
nothing is deleted from the first one.

```
.venv/bin/python build/build_chapter1.py                     # teaching, 227 slides
.venv/bin/python build/build_chapter1.py --edition student   # student, 177 slides
```

| Edition | Output | Holds |
|---|---|---|
| `teaching` (default) | `chapter-01/FIN1209-Chapter-01.pptx` | Everything: 25 checks, 25 reveals, speaker cues. Also writes the answer sheet. |
| `student` | `chapter-01/FIN1209-Chapter-01-Student-Edition.pptx` | The same deck with all 50 check and reveal slides dropped and no speaker cues. |

The student edition exists because the checks only work while the room has
not seen them. A student holding the questions and the answers tells the
instructor nothing, and the speaker cues are written to the instructor about
the room, not to a reader.

Three things follow, and `deckkit.build` handles all three:

- **The progress markers are recomputed, not inherited.** Each marker is
  generated during the traversal from the slides that edition actually
  renders. The denominator has always counted the section body and never the
  checks, so a body slide's marker reads the same in both editions; the
  `| Check N` markers simply do not exist in the student edition.
- **The speaker cues are suppressed at the single place they are written.**
  `deckkit._notes` returns early when `INCLUDE_NOTES` is false, so the
  student `.pptx` carries no notes parts at all.
- **Any generated line that names the checks is reworded.** The roadmap
  slide's accent is the only one; it drops the clause about the checks rather
  than gaining new teaching content. Nothing in the content module refers
  back to a check, and nothing should: a slide that says "as the last
  question showed" cannot survive this switch.

Everything else is identical, and that is verifiable. Extract the text of
every slide from both decks, drop the 50 check and reveal slides from the
teaching one, and the two lists differ only at the roadmap slide.

Adding an edition to a later chapter takes no work: the switch lives in
`deckkit.py` and `build_chapter1.py` and knows nothing about Chapter 1.

## Build the two PDFs

The chapter ships two print documents from the same chapter data, for two
different readers. Keeping them apart is the point.

```
.venv/bin/python build/build_plan.py             # instructor, 26 pages
.venv/bin/python build/build_lecture_notes.py    # students, 29 pages
```

| Output | Who it is for | What is in it |
|---|---|---|
| `chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf` | The instructor | Timing, four run plans, cut tiers, speaker cues, check answers, slide numbers |
| `chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf` | The students | Readable prose, the figures, every term defined once, summary and review questions |

Neither one carries the other's content. If a slide number or a minute count
appears in the lecture notes, it is in the wrong document.

Both take `--keep-html` to write the intermediate HTML beside the PDF for
inspection; those files are gitignored.

Both are HTML with real print CSS rendered by headless Chrome
(`--headless=new --print-to-pdf`), through `build/chrome.py`. **Do not route
either through LibreOffice.** That path is what collapsed every table in an
earlier notes PDF to one character per column.

Two things about these builds are not obvious:

**Chrome writes the PDF and then does not exit.** On this machine, Chrome 151
in `--headless=new --print-to-pdf` mode finishes the file in about five seconds
and then hangs indefinitely. `chrome.render_pdf` therefore does not wait on the
process. It polls until the file appears, its size settles, and it ends in
`%%EOF`, then terminates Chrome. Waiting on the exit code instead takes over
two minutes and usually times out.

**Pagination happens inside the page, not in Chrome.** A script in the document
measures each block and distributes blocks into fixed A4 sheets. That is what
buys a running footer, blocks that are never split across a break, and headings
that are always followed by their content. Chrome's own pagination can do none
of the three. `notekit.paginator_js()` is that script and both documents use
it. Three of its behaviors are opt-in per document, and only the lecture notes
turn them on:

- `data-float="1"` on a block: it waits for the next sheet rather than forcing
  a break and leaving the rest of this one empty. Figures use it.
- `data-flow="1"` on a section: it may carry on down the current sheet if 66mm
  of it is left, instead of always opening a fresh one.
- A single paragraph with nowhere else to break breaks between its sentences.

Together those took the lecture notes from 29 pages at 79 percent page fill to
24 at 94 percent with identical content, before the self test and the central
bank example took them to 26. The teaching plan uses none of them:
an instructor turning to a part expects it at the top of a page.

### The rules the two builds enforce

`notekit.validate()` refuses to write a teaching plan that breaks the design:

- Every slide reference must resolve against the deck. The plan names slides by
  key, never by number, so a stale reference fails the build instead of
  printing a wrong number in front of a class.
- No em dashes or en dashes, checked on the rendered HTML.
- The main column measure must stay inside 45 to 90 characters.

`lecturekit.validate()` refuses to write lecture notes that break theirs. The
deck is the authority on scope, so three of the five checks are drift checks:

- Every figure number, and every chart letter, must be one the deck places.
  The two namespaces are checked separately, so a chart can never be looked up
  as a figure.
- Every figure and every chart must be referenced from the prose, by name, in
  a sentence that says what to look at. Captions do not count. A picture no
  paragraph mentions is decoration.
- Every term the deck teaches must be defined exactly once in the notes, and
  the notes may not define a term the deck does not teach.
- The summary and the review questions must be present. They are not written
  in the content module at all: `deck_closing()` lifts them from the deck's own
  closing slides, so editing those slides moves the notes with them. The audit
  that changed the review questions from six to all eight is exactly the drift
  this closes.
- No em dashes or en dashes, and the same measure band.

### Then look at them

Render the finished PDFs back to images and look at every page. This is not
optional and it is not a formality: an earlier notes PDF was committed without
anyone viewing a rendered page, and two of its pages were unusable.

For the lecture notes, look at **both** builds. The figure build is not the
placeholder build with pictures in it. An early cut of it put the artwork in an
`<img>` inside a flex column, every image overflowed its box and printed on top
of its own caption, and the placeholder build looked perfect throughout.

```
DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf /tmp/plan $(seq 1 26)
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/ln $(seq 1 29)
$DATA/pdfpng ~/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/lnfig $(seq 1 29)
```

`chapter-01/teaching-plan-design.md` and `chapter-01/lecture-notes-design.md`
record the research each design came from.

## Figures

The chapter places 35 figures from the course text. They are Wiley's, this
repository is public, so they live in `assets/figures/`, which is gitignored
and absent on a clean clone. Figures are therefore **off by default**: the
plain build above renders a placeholder in each figure's place, carrying the
figure number, what the figure shows, the credit line and the speaker cue, and
it is what produces the committed deck.

The same policy applies to the lecture notes, which place the same 35 figures.

The versions with the artwork placed go outside the repository:

```
.venv/bin/python build/build_chapter1.py \
    --with-figures --out ~/FIN1209-Chapter-01-with-figures.pptx
.venv/bin/python build/build_chapter1.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-01-Student-Edition.pptx
.venv/bin/python build/build_lecture_notes.py \
    --with-figures --out ~/FIN1209-Chapter-01-Lecture-Notes.pdf
```

The last two are what students get through Canvas.

Both builds produce identical pagination either way: the same slide count for
the edition, and the same 29 pages, because a placeholder occupies exactly the
height its artwork would. Both builds refuse `--with-figures` aimed anywhere
inside the repository, so the artwork cannot reach a commit by accident,
whichever edition is being built. See `chapter-01/README.md` for the file
naming and the full figure list.

## Charts

The nine charts in Part 1 are the exact opposite of the figures and none of
the policy above applies to them. **They are ours.** They are drawn by
`chartkit.py`, which knows nothing about any chapter, from the data in
`charts_chapter01.py`, which carries no drawing code. Every build of the deck
and of the lecture notes redraws all nine into `build/generated/charts/`
before it starts, so a fresh clone produces the real slide and the real page
rather than a placeholder, and the folder is gitignored because it is output.

Three things about them are deliberate and should not be quietly undone.

**They are a separate slide type.** `deckkit.Chart` is not a subclass of
`deckkit.Figure`. A Figure is Wiley's, numbered in the book's scheme, credited
to Wiley by a hard coded line, and absent from this repository; a Chart is
ours, lettered, credited to us, and committed. Keeping them apart is what
stops one being credited as the other, which the hard coded line on
`Figure.credit` would otherwise do the first time an authored chart is placed.
`deckkit.chart_credit()` is the single place the namespace and the credit
wording are written, and both the deck and the lecture notes read it from
there.

**The data is invented, and every chart says so.** We hold no market data
licence, so nothing is fetched and no price file exists. The series come from
`chartkit.walk()` with fixed seeds. A definitional graphic makes no claim
about markets that being real would support, and the credit line under every
chart says the data is illustrative.

**The images have to be byte reproducible**, because the committed deck
embeds them and a deck rebuild with no content change has to leave `git
status` clean. Two things buy that: the series use only `random.Random` and
`uniform()`, whose stream is stable, and `savefig` is told to write no
`Software` metadata, which otherwise stamps the matplotlib version into the
PNG. A matplotlib upgrade will still move the bytes, exactly the way a
python-pptx upgrade does, and the fix is the same: rebuild, look at it,
commit the churn deliberately.

Before committing a deck, confirm the only images in it are those nine:

```
unzip -o -d /tmp/media chapter-01/FIN1209-Chapter-01.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts/*.png | awk '{print $1}' | sort)
```

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
| `build/content_chapter01.py` | Chapter 1 deck content as plain data. No drawing code. |
| `build/build_chapter1.py` | Wires the two together and writes the deck outputs. |
| `build/notekit.py` | Every teaching plan block renderer, its print CSS, and the paginator both PDFs share. Knows nothing about any chapter. |
| `build/plan_chapter01.py` | Chapter 1 teaching plan as plain data. No layout code. |
| `build/build_plan.py` | Resolves the plan against the deck and renders the PDF. |
| `build/lecturekit.py` | Every lecture notes block renderer, its print CSS, and the figure plate machinery. Takes the palette and the paginator from notekit. Knows nothing about any chapter. |
| `build/lecture_chapter01.py` | Chapter 1 lecture notes as plain data. No layout code. |
| `build/build_lecture_notes.py` | Checks the notes against the deck and renders the PDF. |
| `build/chrome.py` | Headless Chrome, shared by both PDF builds. |
| `assets/figures/` | Textbook artwork. Gitignored, absent by default. |

## Adding Chapter 2

Copy the shape of `content_chapter01.py` into `content_chapter02.py`, then
copy `build_chapter1.py` and point it at the new module. The renderers do not
change. Sections, terms, quotes, checks, recaps and closings are all declared
as dataclasses in `deckkit.py`.

Both PDFs are the same move. Copy `plan_chapter01.py` into
`plan_chapter02.py`, and `lecture_chapter01.py` into `lecture_chapter02.py`,
then point copies of the two builders at them. Sheets, parts, ladders, flags,
boards, check cards and tables are dataclasses in `notekit.py`; sections,
prose, definitions, figures, plates, quotations and self checks are
dataclasses in `lecturekit.py`. Chapter 2 is two content files, not a
redesign.

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
- Every chart slide is lettered with one capital letter in our own namespace,
  never a book figure number; says what it shows, which the lecture notes
  reuse; and claims a cut tier the teaching plan recognises, so the plan's
  ladder and the deck cannot disagree about what is safe to drop. No letter is
  used twice.
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
