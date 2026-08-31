# Building the next chapter

Read this before you touch anything. Chapter 1 is the template: it is 218
slides, 25 in-class checks carrying 50 items, 49 terms and 35 figures, and it
ships as four documents built from the same data, one of them a second edition
of the deck. Chapter 2 is three content files and nothing else. You should not
need to open a renderer.

The two design documents behind the print documents are
`chapter-01/teaching-plan-design.md` and
`chapter-01/lecture-notes-design.md`. They record the research each layout came
from, with sources. This file does not repeat them; when you want to know why a
page looks the way it does, go there.

---

## The standing principle: teach only what the textbook teaches

This is the instructor's rule and it outranks everything else in this file.

The course text is Lim, M. (2016), *The Handbook of Technical Analysis*
(Wiley). The chapter's scope is that book's chapter. Where the book defines a
term, use the book's definition. Where the book is silent or ambiguous, **say
so plainly on the slide and in the notes**, and do not import a definition from
somewhere else to fill the hole.

Chapter 1 has a worked example of this. The book lists *supply side* and
*demand side* among its eight categories of market participant and never
defines either, anywhere in the book. An earlier cut of the deck supplied a
definition in the authoritative "formal" register and then examined it. That
was wrong twice over: the ruling was ours, not the book's, and a check item
rested on it. What ships instead names the gap, offers the two readings that
circulate outside the text as an explicitly non-examinable aside, and sets no
question on either. See `build/content_chapter01.py`, the term
`Supply side and demand side`, and section 6.1 of the lecture notes.

The same rule covers dates, later events and outside history. The book's
Swiss National Bank example is written as though the 1.2000 ceiling still
stands. The deck teaches it as the book teaches it and the speaker note says
the book does not tell us what came afterwards. It does not narrate what
happened next, because the book does not.

Where the book contradicts *itself*, say that too rather than picking a side
quietly. Its prose calls the third family of breakout filters *algorithmic*
and its own Figure 1.21 calls it *event-based*. Both documents name the
disagreement in one sentence and move on.

---

## Which files to copy, and which to write fresh

Copy these and change the chapter number. They are wiring, not content:

| Copy | To | Then |
|---|---|---|
| `build/build_chapter1.py` | `build/build_chapter2.py` | point it at the new content module; the `--edition` switch comes with it |
| `build/build_plan.py` | `build/build_plan2.py` | point it at the new plan module |
| `build/build_lecture_notes.py` | `build/build_lecture_notes2.py` | point it at the new lecture module |

Write these three fresh, using the Chapter 1 file beside you as the shape:

| Write | From the shape of | What it is |
|---|---|---|
| `build/content_chapter02.py` | `build/content_chapter01.py` | the deck, as plain data |
| `build/plan_chapter02.py` | `build/plan_chapter01.py` | the instructor's run card, as plain data |
| `build/lecture_chapter02.py` | `build/lecture_chapter01.py` | the students' notes, as plain data |

**Never copy or edit these.** They are chapter-agnostic renderers and a change
here changes every chapter:

`build/deckkit.py`, `build/notekit.py`, `build/lecturekit.py`,
`build/chrome.py`.

If a chapter seems to need a new kind of slide or block, add the dataclass and
its renderer to the kit, not a special case to the content file. Content files
carry no drawing code and no HTML.

---

## The content module's structure

`build/content_chapter01.py` is the authority on scope. The plan and the notes
are both checked against it, so build it first and finish it before you write
the other two.

It is pure data, in this shape:

```
SECTION = Section(
    number, title, short, minutes, covers=(...),
    slides=( ...Content / Term / Quote / Figure / Check... ),
    recap=Recap(items=(...)),
)

CHAPTER = Chapter(course, code, chapter, title, subtitle, presenter,
                  objectives=(...), roadmap=(...),
                  sections=(PART1, ... PART6), closing=CLOSING)
```

The slide types are dataclasses in `build/deckkit.py`:

- `Content(title, lines, accent, caption, notes)` - a teaching slide. Six body
  lines maximum, three preferred. `accent` is the one gold line, the thing to
  notice. `caption` is the small muted line under it.
- `Term(term, plain, example, formal, notes)` - a new term. The three fields
  are the teaching order and they are not interchangeable; see below. An empty
  `formal` renders no formal row, which is how a term the book leaves
  undefined is taught.
- `Quote(text, source, takeaway, notes)` - a short attributed definition
  students are expected to reproduce. The only verbatim text in the chapter.
- `Figure(title, number, shows, notes)` - one book figure. `number` is the
  book's own figure number. `shows` is one line saying what is in the artwork;
  it is what the placeholder prints when the artwork is absent **and** what the
  lecture notes use, so it has to stand on its own.
- `Check(label, questions)` - exactly two `Question(stem, options, answer,
  reason)`. Renders as a question slide plus a reveal slide, so a check always
  costs two slides.
- `Recap(items, notes)` - the you-now-know close of a section.
- `Closing(title, lines, accent, notes)` - the wrap-up slides.

`minutes` on a `Section` is the Full-plan time minus one minute per figure in
that part. The teaching plan's Full column is the number including the figures.
Keep the two consistent; nothing checks it for you.

**The `CLOSING` tuple escapes validation.** `deckkit.validate()` walks
`chapter.sections` only, so a closing slide that overflows the page builds
clean and then collides with the progress marker in the room. When you edit
one, call `deckkit._content_bottom()` on it by hand and compare against
`deckkit.SAFE_BOTTOM`.

---

## The teaching design rules that are not negotiable

The room includes students with ADHD. These are not preferences.

**One idea per slide.** Many small slides, never a wall of text. Most teaching
slides are one idea and should take under a minute. Six body lines is the hard
ceiling the build enforces; three is the target. If a slide fails the page
rule, split it. That is the rule working, not an obstacle to route around.

**Plain words, then a concrete example, then the formal definition.** In that
order, every time, which is why `Term` has exactly those three fields. The
plain gloss is what a student who has never met the word can follow. The
example is concrete and local: pesos, and companies traded on the PSE, with
arithmetic that actually computes. The formal definition comes last and is the
wording a student should be able to reproduce in an exam. Never lead with the
formal one.

**A two-question check after every two or three new terms.** Twenty five of
them in Chapter 1, fifty items. Each is a dark green question slide with a gold
CHECK chip, followed by a reveal slide carrying the letter, the option text and
a one-line reason. The reason is not decoration: the letter alone teaches
nothing. Checks carry no marks and the instructor says so out loud the first
time, or the room freezes.

The answer key must be spread. No letter may hold more than 35 percent or fewer
than 15 percent of the items, and no three consecutive items may share an
answer. The build refuses a deck that breaks this. The first cut of Chapter 1
put 74 percent of its answers on B, which meant a student who always picked B
scored 74 and the checks could not read the room at all. **When it fails, the
fix is positional: reorder the options within the offending questions. Do not
reword anything.** Two kinds of option set must not be reordered: ordinal and
numeric sets (`Stage 1 / Stage 2 / Stage 4`, `Four / Six / Eight`) keep their
sequence, and in the department's "I, II, III, IV" items the `All are correct`
option belongs last. Spread the key using the other questions instead.

**A visible progress marker.** Bottom left of every slide:
`Part 3 of 6 - Classifications | 7 of 19`. Students always know where they are,
and when someone asks how much is left the instructor points at it rather than
answering. It is why nothing may run past `deckkit.SAFE_BOTTOM`, and why the
six parts each open with what they cover and close with a recap: every part
boundary is a clean stop.

**No em dashes or en dashes**, anywhere, in any of the three documents. All
three builds check the rendered output and refuse. Plain dashes only.

One more that is not a rule but is worth knowing: some sequences are a single
teaching move rather than a set of slides. Chapter 1's Figures 1.9 to 1.15 are
the same chart read seven ways and they run straight through without stopping,
because that sequence *is* the argument that analysis is subjective. If your
chapter has one of these, say so in the plan and mark it uncuttable.

---

## The copyright split for figures

The textbook, the publisher's scans, the previous course holder's decks and
**the book's figure artwork** are third-party copyrighted works. This
repository is public. None of them may be committed, ever.

The artwork lives in `assets/figures/`, which is gitignored and absent on a
clean clone. One PNG per figure, named by the book's own figure number:

```
assets/figures/figure-1-09.png    ->    Figure 1.9
assets/figures/figure-2-14.png    ->    Figure 2.14
```

That gives two builds of each deck edition and two of the lecture notes. Same
content, same slide and page counts, same order; the only difference is what
sits in the figure band, because a placeholder occupies exactly the height its
artwork would.

- **The committed versions are the placeholder builds**, and they are what a
  plain build produces on any machine. Every figure keeps its number, its
  `shows` line and the credit line, so the chapter stays complete and
  rebuildable by anyone without the artwork.
- **The teaching versions have the artwork placed** and are written outside the
  repository, to the instructor's home directory.

Both builds refuse `--with-figures` aimed anywhere inside the repository, for
either deck edition. A missing PNG is not an error: that one figure renders as
a placeholder and the rest of the document is unaffected.

Before committing a deck, confirm it embeds no artwork. Both editions:

```
unzip -l chapter-02/FIN1209-Chapter-02.pptx | grep ppt/media    # must be empty
unzip -l chapter-02/FIN1209-Chapter-02-Student-Edition.pptx | grep ppt/media
pdfimages -list chapter-02/FIN1209-Chapter-02-Lecture-Notes.pdf # must list none
```

Answer keys for graded assessments stay out of the repository too.

---

## The four build commands

From the repository root, in this order, every time:

```
.venv/bin/python build/build_chapter2.py                   # teaching deck, and the answer sheet
.venv/bin/python build/build_chapter2.py --edition student # student deck
.venv/bin/python build/build_plan2.py                      # the instructor, 23 pages for ch. 1
.venv/bin/python build/build_lecture_notes2.py             # the students, 26 pages for ch. 1
```

**Rebuild all four whenever you change the content module.** The deck is the
authority on scope and both PDFs are checked against it. The plan resolves
every slide reference against the deck; the notes resolve every figure number
and every term against it.

Then the three versions with the artwork, outside the repository:

```
.venv/bin/python build/build_chapter2.py \
    --with-figures --out ~/FIN1209-Chapter-02-with-figures.pptx
.venv/bin/python build/build_chapter2.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-02-Student-Edition.pptx
.venv/bin/python build/build_lecture_notes2.py \
    --with-figures --out ~/FIN1209-Chapter-02-Lecture-Notes.pdf
```

The last two are what students get through Canvas.

### The edition switch, which you inherit for free

`--edition` lives in `deckkit.build()` and `build_chapter1.py` and knows
nothing about any chapter, so Chapter 2 gets it by copying the build script.
`teaching` is the default and renders everything. `student` drops every
`Check`, which removes both the question slide and its reveal, and writes no
speaker notes at all.

Three consequences, all handled for you, and all worth understanding before
you write content:

- The progress markers are **regenerated** for the slides the edition renders.
  The denominator has always counted the section body and never the checks, so
  a body slide reads the same in both editions.
- Speaker cues are suppressed at the one place they are written, so the
  student `.pptx` carries no notes parts.
- **Do not write a slide that refers back to a check.** "As the last question
  showed" is true in one edition and false in the other, and nothing in the
  build can fix it for you. Chapter 1 has no such slide. The only line that
  named the checks is generated, not authored: the roadmap accent, which the
  student edition rewords.

Only the teaching build writes the answer sheet, so the student build can
never stale it.

Environment, fonts and the sharp edges of the PDF pipeline are in
`build/README.md`. The two that will bite you: headless Chrome writes the PDF
and then never exits, so the build polls for the file rather than waiting on
the process; and pagination is done by a script inside the page, not by Chrome.

---

## What the builds refuse to write

Treat a failed build as the design working. Do not route around it.

`deckkit.build()`: more than six body lines on a content slide; a check that is
not exactly two questions of four options with an A to D answer; a teaching
slide with no speaker cue or more than three; a figure slide with no book
number or no `shows` line; any em dash or en dash; any slide whose content runs
past the safe bottom; an answer key outside the spread rule.

`notekit.validate()` (the plan): a slide reference that does not resolve; em or
en dashes; a main column measure outside 45 to 90 characters.

`lecturekit.validate()` (the notes): a figure number the deck does not place; a
figure the prose never mentions by number in a sentence saying what to look at;
a term the deck teaches that the notes never define, or a term the notes define
that the deck does not teach; a missing summary or review questions; em or en
dashes; the same measure band.

The plan never contains a typed slide number. It names slides by stable key
(`{s:fig:1.11}`, `{s:check:13}`, `{s:term:Price}`,
`{s:slide:The exact slide title}`, `{s:part:3}`, `{s:recap:3}`, `{a:13}`) and
the build resolves them using the same traversal that numbers the deck. Change
the deck and the plan follows; break a reference and the build fails rather
than printing a wrong number in front of a class.

The notes never retype a figure description or the chapter summary. Figure
descriptions come from the content module's `shows` lines, and the summary and
review questions are lifted from the deck's own closing slides. Do not paste
copies into the lecture module; leave `summary=()` and `review_questions=()`
and let the build fill them.

---

## Verification, before you commit

**Render every finished PDF back to images and look at every page.** This is
not optional and it is not a formality. An earlier notes PDF was committed
without anyone viewing a rendered page and two of its pages were unusable.
Later, the figure build put every image on top of its own caption while the
placeholder build looked perfect throughout.

```
DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
$DATA/pdfpng chapter-02/FIN1209-Chapter-02-Teaching-Plan.pdf   /tmp/plan  $(seq 1 23)
$DATA/pdfpng chapter-02/FIN1209-Chapter-02-Lecture-Notes.pdf   /tmp/ln    $(seq 1 26)
$DATA/pdfpng ~/FIN1209-Chapter-02-Lecture-Notes.pdf            /tmp/lnfig $(seq 1 26)
```

Look at **both** builds of the lecture notes. The figure build is not the
placeholder build with pictures in it.

For the deck, convert it and look at every slide you added or changed, in the
build with the artwork in it, because that is what the room sees. Do the
student edition too, at least the first and last slide of every part, because
that is where a dropped check could have left a wrong marker or a broken
transition:

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-02/FIN1209-Chapter-02.pptx
soffice --headless --convert-to pdf --outdir ~ ~/FIN1209-Chapter-02-with-figures.pptx
soffice --headless --convert-to pdf --outdir ~ ~/FIN1209-Chapter-02-Student-Edition.pptx
```

What to look for, in order:

1. **Nothing clipped and nothing overlapping.** Especially a caption running
   into the footer rule, and figure artwork over its own caption.
2. **No page more than about a quarter empty.** A page that is half white
   usually means one block could not fit and jumped. Splitting a long
   paragraph into two blocks lets the paginator fill the page.
3. **No page carrying a single orphaned sentence.** Trim a few words upstream
   rather than shipping the extra sheet.
4. **Every stated number.** Slide count, part names, figure count, page counts,
   minute totals and each run plan's arithmetic, in all four documents and in
   the two READMEs. Nothing checks these for you.
5. **Both editions' counts.** The student edition must come out at the
   teaching count minus twice the number of checks, hold no check or reveal
   slide, and carry no notes part:
   `unzip -l <student deck>.pptx | grep notesSlide` must be empty.

Then the paperwork:

- `git status --short` after a plain rebuild must be empty on a second run. The
  deck build is deterministic and a clean rebuild is byte-identical, for both
  editions. The two PDF builds are not: Chrome stamps its own identifiers, so
  a rebuild with no content change still moves those bytes. Check them by
  their text (`pdftotext`), and revert them if only the bytes changed.
- `unzip -l <deck>.pptx | grep ppt/media` must be empty, for both editions.
- **No image file may be committed**, in any form.
- Update `chapter-02/README.md` and the counts in `build/README.md`.

---

## What Chapter 2 inherits, in one line

Six parts, a check every two or three terms, a figure only where the book has
one, every term defined once in each document in the same words, two editions
of the deck from one content file, and no ruling the book does not make.
