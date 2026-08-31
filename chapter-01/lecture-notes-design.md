# Why the lecture notes look the way they do

The repository already had a 23 page document called
`FIN1209-Chapter-01-Notes.pdf`. It was a good instructor run card: timing,
cut tiers, what to say, which check comes next. It was not lecture notes. It
has been renamed to `FIN1209-Chapter-01-Teaching-Plan.pdf`, which is what it
always was, and this file records the research behind the document that
replaces it in the student's hands.

The working definition, from the instructor: **lecture notes are a readable,
short file of what was discussed in the lesson, that still has the graphs.**
The test is a student who missed the class, reading alone, with the textbook
closed.

Everything below was read as the artifact, not as a description of it. Every
PDF named here was downloaded and measured with `pdfinfo` and `pdftotext`
on 31 August 2026. Where something could not be reached, it says so.

---

## 1. What was measured

| Source | Unit measured | Pages | Words | Words per page |
|---|---|---|---|---|
| MIT 18.05 Class 1 notes (Orloff and Bloom) | one 80 min class | 10 | 3,419 | 342 |
| MIT 18.05 probability notes, whole bundle | 7 classes | 111 | 45,464 | 410 |
| MIT 18.05 statistics notes, whole bundle | 8 classes | 172 | 66,881 | 386 |
| MIT 14.03 Lecture 1 (Autor) | one lecture | 17 | 3,931 | 231 |
| MIT 14.03 Lecture 16 | one lecture | 18 | 5,052 | 281 |
| MIT 14.03 Lecture 22 | one lecture | 21 | 7,269 | 346 |
| MIT 14.01 Lecture 1 summary | one lecture | 2 body | 372 | 186 |
| MIT 14.01 Lecture 4 summary | one lecture | 3 body | 780 | 260 |
| Berkeley CS 70 Note 1, Summer 2025 | one lecture | 6 | 2,704 | 451 |
| Berkeley CS 70 Note 1, current site | one lecture | 3 | 1,525 | 508 |
| Cambridge Markov Chains (Weber) | 12 lectures | 45 body | 23,426 | 521 |
| Harvard Math S-21a Unit 1 (Knill) | one lecture | 4 | 1,997 | 499 |
| Stanford CS229 main notes | whole course | 278 | 91,307 | 328 |
| LSE International Financial Crises (Guimaraes) | short course | 45 | 14,324 | 318 |
| MIT 15.401 "Lecture Notes" lec01 | one lecture | 21 | 1,464 | **70** |
| MIT 15.401 "Lecture Notes" lec21 | one lecture | 27 | 1,681 | **62** |
| Yale OYC ECON 252 Lecture 1 **transcript** | one 75 min lecture | web | **9,229** | n/a |

The two bold rows are the interesting ones and they are explained in section 6.

### The sources, with URLs

- **MIT 18.05 Introduction to Probability and Statistics, Spring 2022.**
  Course: <https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/>
  Notes bundles:
  <https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf>
  and `.../mit18_05_s22_statistics.pdf`.
  Prose notes, one document per topic, 2 to 13 pages each, grouped into
  classes. This is the closest thing to a reference standard for a
  quantitative subject and it is the main model for the FIN1209 notes.

- **MIT 14.03 / 14.003 Microeconomic Theory and Public Policy, Fall 2016
  (David Autor).**
  Notes index: <https://ocw.mit.edu/courses/14-03-microeconomic-theory-and-public-policy-fall-2016/pages/lecture-notes/>
  Lecture 1 PDF:
  <https://ocw.mit.edu/courses/14-03-microeconomic-theory-and-public-policy-fall-2016/f26552d656495d9234bd86df601c30b0_MIT14_03F16_lec1.pdf>
  Lecture 22 PDF:
  <https://ocw.mit.edu/courses/14-03-microeconomic-theory-and-public-policy-fall-2016/43f71411b698eb3cd3f088502e0636e1_MIT14_03F16_lec22.pdf>
  The closest subject match in the sample: an economics course where the
  notes are continuous prose with numbered definitions, numbered captioned
  figures, and real world applications.

- **MIT 14.01 Principles of Microeconomics, Fall 2023, lecture summaries.**
  <https://ocw.mit.edu/courses/14-01-principles-of-microeconomics-fall-2023/lists/lecture-summaries/>
  Lecture 1: `.../mit14_01_f23_lec1.pdf`.
  These are labelled summaries, not notes, and they read like it: all
  bullets, no connective prose, no figures. Useful as the lower bound of what
  a student-facing document can be and still be worth printing.

- **MIT 15.401 Finance Theory I, Fall 2008.**
  <https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/lecture-notes/>
  Filed under "Lecture Notes", but every file is a slide deck. See section 6.

- **Berkeley CS 70, Discrete Mathematics and Probability Theory.**
  <https://su25.eecs70.org/assets/pdf/notes/n1.pdf> and
  <https://www.eecs70.org/assets/pdf/notes/n1.pdf>
  One numbered "Note" per lecture, 3 to 6 pages, running footer reading
  `CS 70, Summer 2025, Note 1`, and inline **Concept check!** boxes.

- **Cambridge, Markov Chains, Part IB (Richard Weber).**
  <http://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf>
  61 pages for a 12 lecture course: one numbered chapter per lecture, about
  4 pages each, two level section numbering, and a final chapter of
  "Concluding problems and recommendations for further study".

- **Harvard, Math S-21a Multivariable Calculus (Oliver Knill).**
  <https://people.math.harvard.edu/~knill/teaching/summer2023/handouts/lecture01.pdf>
  4 pages per lecture. Numbered paragraphs (1.1, 1.2, ...), boxed
  `Definition:` blocks, `Figure 1.` with a caption below it, then Examples
  and a numbered Problems section, then a one line author and course footer.

- **Stanford CS229 Machine Learning, main lecture notes.**
  <https://cs229.stanford.edu/main_notes.pdf>
  278 pages for the course. The figure convention here is the cleanest in the
  sample: `Figure 7.1: Housing prices with a "kink" in the graph.` set below
  the artwork, chapter dot number, and always referenced from the running
  text ("as shown in Figure 7.1", "see an illustration of an MLP in Figure
  7.4, Left").

- **LSE, International Financial Crises (Bernardo Guimaraes).**
  <https://personal.lse.ac.uk/guimarae/lecturenotes.pdf>
  45 pages, three level numbering, a contents page, and an honest abstract
  that says what the notes are and are not.

- **LSE, ST419 Computational Statistics.**
  <http://stats.lse.ac.uk/baurdoux/CS/Lecturenotes.pdf>
  112 pages. Included for length only: its figures carry no numbers or
  captions, which is the failure mode this design avoids.

- **Yale, Open Yale Courses, ECON 252 Financial Markets (Robert Shiller),
  Lecture 1.**
  Page: <https://oyc.yale.edu/economics/econ-252-08/lecture-1>
  Transcript: <https://openmedia.yale.edu/projects/iphone/departments/econ/econ252/transcript01.html>
  Open Yale publishes audio, the slide PDF, and a full transcript. It
  publishes no lecture notes at all. The transcript is 9,229 words for one
  75 minute lecture.

### What could not be verified

- **Oxford.** No official departmental lecture notes were reachable. Oxford
  course material sits behind the department intranet and Canvas. The one
  public Oxford artifact found,
  <https://users.ox.ac.uk/~nuff0177/finalstutes12.pdf> (Macroeconomics
  Tutorials, 51 pages), is a tutorial reading guide rather than lecture
  notes, and it says so in its own first paragraph. Everything else returned
  by search was a commercial student notes reseller, which is not evidence of
  what Oxford publishes.
- **Cambridge Faculty of Economics.** Same situation. The Cambridge artifact
  used here is from the Statistical Laboratory instead, which does publish.
- **Harvard Statistics 110.** Only a maths review handout is public
  (<https://projects.iq.harvard.edu/files/stat110/files/math_review_handout.pdf>);
  the lecture notes circulating online are student transcriptions, not
  Harvard's own, so they were not used. The Harvard artifact used here is
  from the Mathematics department, which does publish.
- **LSE EC201 and EC202** publish handouts and slide sets rather than prose
  notes; the two LSE PDFs used are personal pages of LSE staff, which is what
  LSE makes public.

The pattern in these gaps is itself a finding: the institutions that publish
real prose lecture notes to the open web are the ones that decided to, and
MIT OCW is the only one that does it at scale.

---

## 2. How long is one chapter of lecture notes

Real per lecture notes cluster in a band:

- **Short and dense:** Cambridge and Harvard, 4 pages and about 2,000 words
  per lecture. Both are mathematics, where a page holds fewer words.
- **Middle:** Berkeley CS 70, 3 to 6 pages, 1,500 to 2,700 words.
- **Long:** MIT 18.05, 10 pages and 3,400 words for one class; MIT 14.03,
  17 to 21 pages and 3,900 to 7,300 words for one lecture.
- **A whole course:** Stanford CS229 at 278 pages, LSE at 45.

So one lecture is 4 to 21 pages, 1,500 to 7,300 words, and the median is
around 6 pages and 2,700 words.

FIN1209 Chapter 1 is not one lecture. The deck is 218 slides and 205 minutes
of teaching, which is about two and a half standard 80 minute lectures. Scaled
on the MIT 14.03 figure, a faithful set of notes would be 40 pages. Scaled on
Cambridge, 10.

**The decision: about 6,900 words of body text, which came out at 24 A4
pages.** The chapter has grown since: restoring the book's self test and the
central bank example took the deck to 218 slides and 35 figures, and the notes
to 7,725 words and 26 pages. The rule below is what set the length, and it is
still the rule. The measurements in the table are the ones taken on the 24 page
cut.

The first draft of this file budgeted 14 to 18 pages, and that number was
wrong. It was written before anything had been measured, and it ignored the
two fixed costs this chapter carries that a normal set of lecture notes does
not. Here is the arithmetic that replaced it, taken from the built document:

| What | Cost |
|---|---|
| 19 figure blocks holding all 31 figures | 7 pages |
| 49 definitions, one per term the deck teaches | 5 pages |
| Body prose, 6,922 words | 10 pages |
| Openers, headings, quotations, self checks, front and back matter | 2 pages |

Those were measured by rebuilding the document with each element removed in
turn. The prose is the only part that was a free choice, and 6,900 words is
already at the short end of real practice: MIT 18.05 spends 3,400 words on one
80 minute class, which scales to about 8,300 for 195 minutes, and MIT 14.03
spends 3,900 to 7,300 on a single lecture, which scales to 12,000 or more.

So the length is what carrying every figure and every term costs, and the
reasons to accept it rather than cut into that:

1. It is a quarter of what a transcript of the same session would be. Yale's
   transcript is 9,229 words for 75 minutes, so 195 minutes is roughly 24,000
   words of talking. The notes are the compression, not the record.
2. It is half the deck. The deck at its own density is about 14,000
   words of fragments. The notes are shorter than the slides and are the only
   one of the two that can be read on their own.
3. The instructor's two requirements were short and **still has the graphs**.
   Dropping figures to reach 16 pages would have satisfied the first by
   breaking the second. Cutting the prose to 4,000 words would have made the
   notes gesture at the argument instead of making it.
4. Per minute of teaching it is well inside the band. MIT 14.03 spends 17 to
   21 pages on one 80 minute lecture; the same rate over 195 minutes would be
   more than 40.

What a page holds, in practice: about 580 words of pure prose at 10.6pt on a
160mm measure, less wherever a figure or a definition sits. Mean page fill in
the built document is 94 percent, and no page is emptier than 74 percent.

**The budget for Chapters 2 to 10** is therefore not a page count. It is:
every figure the deck places, every term the deck teaches, and prose at about
35 words per minute of teaching. Chapter 1 comes out at 26 pages on that rule.
A chapter with half the figures will come out much shorter, and that is
correct.

---

## 3. Structure

Every prose set in the sample opens the same way and closes the same way.

**Opening.** A title block naming the course, the unit and the author, then,
before any content, a statement of what the reader should be able to do.
MIT 18.05 heads every class document with a numbered `1 Learning Goals`
list. MIT 14.03 opens with a numbered outline of the argument. Berkeley opens
with a paragraph placing the note in the sequence.

*Decision:* a masthead with the course code, chapter number, chapter title and
the instructor, then a short orientation paragraph, then the chapter's seven
learning objectives as a numbered list. The objectives already exist in
`build/content_chapter01.py` and are the department's, so they are used
verbatim rather than invented.

**Numbering.** Two levels everywhere: MIT 18.05 uses `2`, `2.1`, `2.2`;
Cambridge uses `11.2`; Harvard numbers every paragraph as `1.5`. Nobody uses
three levels for a single lecture.

*Decision:* two levels. Sections 1 to 6 are the deck's own six parts in the
deck's own order, so a student can move between the deck and the notes without
a mapping table. Subsections are `1.1`, `1.2`, and so on.

**Closing.** Cambridge ends with a chapter of concluding problems and further
reading. Harvard ends with numbered problems. MIT 14.01 ends each lecture with
a `TO KNOW - Conceptual Understanding` block that restates the lecture in two
or three sentences. Nobody ends a set of notes on the last content sentence.

*Decision:* a Summary section that is the chapter in five sentences, then the
book's own six review questions, then a key terms index, then the sources.

**What is not a section.** No table of contents. At 16 pages, with running
footers and six numbered sections, a contents page is a page the student turns
past. Cambridge has one because it is 61 pages; Harvard, at 4 pages, does not.

---

## 4. Figures

This is where the sample splits cleanly.

- **Numbered, captioned, referenced.** Stanford CS229: `Figure 7.1: Housing
  prices with a "kink" in the graph.` below the artwork, and the prose says
  "as shown in Figure 7.1". MIT 14.03 Lecture 22 does the same with
  `Figure 1: Potential Nash Equilibria of Used Car Market with lambda = 0.3`
  and the text "In Figure 1, lambda = 0.3, and there are two ranges of Nash
  equilibria". Harvard: `Figure 1. The 3-4-5 triangle and the Curry missing
  square paradox.`
- **Dropped inline with a deictic reference.** MIT 18.05 never numbers a
  figure. It writes "the figure below", "the right-hand figure also
  illustrates that", "see the figure". This works because a figure is always
  on the same page as the sentence that needs it.
- **Neither.** LSE ST419 has figures with no numbers and no captions. A
  reader coming back to it three weeks later cannot cite anything.

The 18.05 approach depends on the figure never moving. In a paginated build
where a figure can slide to the next sheet, it fails.

*Decisions:*

1. **Every figure is numbered with the book's own number**, `Figure 1.9`, not
   renumbered `Figure 1`, `Figure 2`. This is a deliberate departure from
   CS229. The students have the textbook; using Lim's numbering makes the
   notes and the text cross-reference for free, and makes the notes and the
   deck agree, since the deck's figure slides also carry the book's numbers.
2. **Caption below the artwork**, in the CS229 form: the number, then a
   sentence saying what the figure shows. The caption sentence is a sentence,
   not a label.
3. **Every figure is referenced from the prose by number, in a sentence that
   says what to look at.** "Figure 1.9 is that chart with nothing on it."
   The build enforces this: a figure that no paragraph mentions fails the
   build. A figure nobody points at is decoration.
4. **A sequence of figures making one argument becomes one plate.** Figures
   1.9 to 1.15 are the same price chart read seven ways, and that is the
   central argument of Part 4. As seven separate figures they eat three
   pages; as one plate of seven panels under one caption, the point is
   visible at a glance, which is what a textbook does with a sequence. The
   same applies to the pairs (1.3 and 1.4, 1.17 and 1.18, 1.25 and 1.26,
   1.31 and 1.32) and to the discounting trio (1.27, 1.28, 1.29).
5. **Credit line under every figure.** The artwork is Wiley's.

---

## 5. Prose, definitions, and terminology

**Prose against bullets.** The prose sets are prose. MIT 18.05, MIT 14.03,
Cambridge, LSE and CS229 are continuous paragraphs, and they use a numbered
or bulleted list only where the content is genuinely a list: an enumeration of
cases, an algorithm, a set of axioms. MIT 14.01's summaries are the opposite,
100 percent bullets, and they are explicitly labelled summaries rather than
notes. The teaching plan in this repository is also bullet dominated, because
an instructor scanning a page mid class needs fragments.

*Decision:* body text is full sentences in paragraphs. Lists are reserved for
things that are actually lists: the four trading verbs, the three forms of
EMH, the six streams of market action, the five underlying markets. The rule
of thumb applied while writing was that if a bullet could be a clause in the
sentence above it, it became one.

**Definitions.** Two conventions in the sample. MIT 14.03 numbers them,
`Definition 1. Randomized experiment.`, and follows immediately with
`Example:`. Harvard boxes them under a plain `Definition:` label. Both put the
definition at the point of first use, in the flow of the argument, not in a
glossary at the back.

*Decision:* a definition block at first use, carrying the term and the formal
sentence, sitting inside the paragraph flow that has just introduced the term
in plain language and given a concrete example. The plain gloss comes first,
the example second, the formal wording third, which is the order the deck
already teaches in and the order that survives an exam. All 45 of the deck's
terms are defined exactly once, and the build fails if the notes and the deck
disagree about which terms exist.

**Terminology afterwards.** None of the prose sets carries a glossary; they
rely on the definition being findable in the section it belongs to. At 4 or 6
pages that is fine. At 16 pages, with 45 terms and a quiz coming, it is not.

*Decision:* a **Key terms** index at the back listing every term against the
section it is defined in. Section numbers, not page numbers, so the index
cannot go stale when a paragraph is added.

**Self-check questions.** Berkeley CS 70 puts a boxed `Concept check!` in the
middle of the argument. MIT 18.05 uses `Think:`, `Concept question:` and
`Test your intuition:` the same way. Both are unmarked, unassessed, and
answered by the next paragraph.

*Decision:* a small number of short **Check yourself** prompts, one per
section, at the point where a student reading alone would have quietly lost
the thread. The 25 in-class multiple choice checks stay in the deck and the
teaching plan; putting 50 items with their answer letters in a student
handout would turn the notes into an answer key.

---

## 6. What is deliberately not in lecture notes

The clearest evidence in the whole sample is the contrast between three
documents about the same kind of material.

**Slides.** MIT 15.401 files its slide decks under "Lecture Notes". They
measure 62 to 70 words per page, against 231 to 508 for every prose document
in the table. A slide page carries a title and five fragments. It is a
prompt for someone who is talking, and it does not survive the removal of the
person who was talking.

**A transcript.** Yale ECON 252 Lecture 1 is 9,229 words for 75 minutes, and
its own section headings are "Introduction to the Course", "Textbooks and
Course Logistics", "Technology and the Subprime Crisis". Two of the five are
administration. A transcript contains everything that was said, which includes
the teaching assistants' names, the jokes, the repetitions, and the answers to
questions nobody reading later can hear.

**Notes.** Sit between the two. They keep the argument and throw away both the
fragments and the talking.

So, the list of what is out:

- **Timing.** No minute counts, no run plans, no cut tiers. Those exist and
  they live in `FIN1209-Chapter-01-Teaching-Plan.pdf`.
- **Instructions to the instructor.** No speaker cues, no "ask the room", no
  "let two people answer", no board work.
- **Slide numbers.** The notes are not an index into the deck. They follow the
  deck's six parts in order, which is enough to move between them. Printing
  `s147` next to a paragraph is a habit from the teaching plan.
- **The check answer letters.** They are in the deck and in
  `in-class-checks.md`.
- **The slide fragments themselves.** No line of the notes is a slide bullet
  copied across. Every one was rewritten as a sentence.
- **Jokes and classroom management.** The Pring quotation stays because it is
  examinable. "Ask what the mood of the room is right now" does not.
- **A contents page.** See section 3.

---

## 7. The typographic decisions

The FEU identity is fixed by the rest of the repository and is not up for
review here: green `#007A33`, gold `#F2A900`, ink `#1a1a1a`, paper `#faf8f2`,
Marcellus SC for display with Palatino as the shipped fallback, Arial for body.
`build/notekit.py` already holds those values and the lecture notes import
them rather than restating them.

What is specific to this document:

- **A4, single column, 24mm side margins.** 162mm of measure at 11pt Arial is
  about 83 characters, inside Butterick's 45 to 90 band. The teaching plan is
  two column, a 34mm cue rail beside a 134mm main column, because an
  instructor scans a rail. A student reads a line, so the rail is gone.
- **11pt body on 1.45 line height**, against the plan's 10pt on 1.40. The plan
  is held at arm's length and scanned; the notes are read at desk distance for
  half an hour.
- **Running footer** carrying the section name on the left and the page number
  on the right, in the CS 70 form. Pagination is done by the same in-page
  paginator the plan uses, because Chrome cannot produce a running footer and
  will happily split a figure across a sheet.
- **Sections do not force a fresh page.** They open with a full width band and
  carry on down the current sheet, so long as 66mm of it is left. Forcing six
  page breaks was the first thing tried, because that is what 18.05 does and
  what the teaching plan does. On this document it cost four pages of white
  paper and stranded single paragraphs on sheets of their own. Cambridge's
  Markov Chains notes do not force one either. The teaching plan still does,
  because an instructor turning to a part expects it at the top of a page.
- **Three pagination rules earn their keep here**, all added to the shared
  paginator in `notekit.py` and all opt-in so the teaching plan is unaffected:
  a figure that will not fit at the foot of a sheet waits rather than leaving
  the rest of the sheet empty; a single paragraph with nowhere else to break
  breaks between its sentences; and a section opener is glued to whatever
  follows it. Together they took the document from 29 pages at 79 percent fill
  to 24 at 94 percent, with the same content in it.
- **No em dashes or en dashes**, enforced on the rendered HTML by
  `lecturekit.validate`, the same rule the deck and the plan already carry.

---

## 8. What this means for Chapters 2 to 10

The point of writing this down is that Chapter 2 is a content file.

- `build/lecturekit.py` holds the layout: the blocks, the print CSS, the
  figure plate machinery, the validator. It knows nothing about any chapter,
  the way `deckkit.py` and `notekit.py` know nothing about any chapter. It
  shares the FEU palette and the paginator with `notekit.py` rather than
  copying either.
- `build/lecture_chapter01.py` holds Chapter 1 as plain data.
- `build/build_lecture_notes.py` wires them together, checks the notes against
  the deck, and renders the PDF.

Chapter 2 is `lecture_chapter02.py` plus one line in the builder. The rules
below travel with it:

1. Budget prose at about 35 words per minute of teaching, then let the page
   count fall out of the figures and the terms. If the draft is too long, cut
   prose, not figures.
2. Every term the deck defines is defined once in the notes, at first use.
   The build checks this against `content_chapter02.py` and fails otherwise.
3. Every figure carries the book's number, a caption sentence, a credit line,
   and at least one reference from the prose. The build checks the last one.
4. Sections are the deck's parts, in the deck's order.
5. The document ends with Summary, Review questions, Sources, Key terms. The
   first two are lifted from the deck's own closing slides by the build, not
   retyped: they are the book's questions, the deck is where they are
   maintained, and a copy here goes stale the moment somebody edits that
   slide. It already did once.
6. Render every page of both builds to PNG and look at every one before
   committing. The figure build is not the placeholder build with pictures in
   it: an early cut of this document put the artwork in an `<img>` inside a
   flex column, and every image overflowed its box and printed on top of the
   caption and the paragraph below. The placeholder build looked perfect. Only
   the rendered figure build showed it.

Chapter 1's figures are Wiley's and this repository is public, so the
committed PDF is the placeholder build and the real one is written outside the
repository. `chapter-01/README.md` has the two commands.
