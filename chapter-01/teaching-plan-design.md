# Designing the FIN1209 teaching plan

This file is the record behind `FIN1209-Chapter-01-Teaching-Plan.pdf`, the
**instructor's** document: timing, run plans, cut tiers, what to say, which
check comes next. Throughout this file, "the notes" means that document. It was
called `FIN1209-Chapter-01-Notes.pdf` when this was written, which was a
misleading name, because a teaching plan is not lecture notes. The students'
document is a separate artifact with a separate design file,
`lecture-notes-design.md`.

It exists so that Chapter 2 is a content file rather than a fresh argument
about layout. It has three parts: what was read, what each source contributed,
and the decisions that follow. The last section is honest about what could not
be verified.

The plan is generated. `build/build_plan.py` is the entry point,
`build/notekit.py` is the chapter-agnostic renderer, and
`build/plan_chapter01.py` is the Chapter 1 content. Nothing in the PDF is
hand-set.

## Why this was rebuilt

The previous `lecture-notes.md` was converted to PDF by a hand-written markdown
converter that nobody ever looked at the output of. Page 1 turned every
hard-wrapped source line into its own paragraph, so sentences broke mid-thought
with a paragraph gap in the middle, and a `**bold**` span that crossed a line
break leaked through as literal asterisks. Page 5 rendered the timing table one
character per line: a full A4 sheet of single letters running down the page.

The content was never the problem. The failure was that the artefact was
produced and committed without anyone rendering it back to an image and looking
at it. That is the process defect this rebuild is designed around, which is why
`build/build_plan.py` renders through headless Chrome and why every page of the
committed PDF was rendered to PNG and viewed before commit.

## What a set of teaching notes is

### Milkova, S., "Strategies for Effective Lesson Planning", Center for Research on Learning and Teaching, University of Michigan

<https://crlt.umich.edu/sites/default/files/instructor_resources/strategies_for_effective_lesson_planning.pdf>

The load-bearing source. A lesson plan integrates three things: objectives for
student learning, teaching and learning activities, and strategies to check
student understanding. It closes by saying what a lesson plan is not:

> To be effective, the lesson plan does not have to be an exhaustive document
> that describes each and every possible classroom scenario. Nor does it have to
> anticipate each and every student's response or question. Instead, it should
> provide you with a general outline of your teaching goals, learning
> objectives, and means to accomplish them. It is a reminder of what you want to
> do and how you want to do it.

That sentence is the brief for the whole document. Teaching notes are a reminder,
not a script and not a transcript.

Its step 1 is the one that shaped the structure most. Having listed the
objectives, you rank them, and the ranking questions are explicitly about
triage:

> If I ran out of time, which ones could not be omitted? And conversely, which
> ones could I skip if pressed for time?

Step 6 says to build a realistic timeline, to accept that you will adjust the
plan during class, and that the prioritised list is what lets you "make decisions
on the spot".

**What this contributed.** The existing Core / Reinforcement / Enrichment / Fold
markers and the run plans are not an eccentricity of this course. They are
the CRLT triage step, already done, written down before the session rather than
improvised at the 90 minute mark. That promoted them from body text to the most
prominent element on every part page.

### Centre for Teaching Excellence, Singapore Management University, "Lesson Planning"

<https://cte.smu.edu.sg/lesson-planning>

Same three components as CRLT, plus two additions used here: build a realistic
timeline by estimating each activity and then adding buffer, and share the plan
with the students by putting a brief agenda where they can see it.

**What this contributed.** Confirmation that the estimate-plus-buffer timing
belongs in the notes as a number per part, and support for the deck's progress
marker as a student-facing agenda rather than decoration.

### Eberly Center, Carnegie Mellon University, "Lectures"

<https://www.cmu.edu/teaching/designteach/teach/instructionalstrategies/lectures.html>

Open with an introduction, outline or agenda. Signal transitions between
subtopics, and from a general theory to an example. Use "markers that clearly
signal important, or challenging, or counterintuitive points". Include periodic
summaries and close with a synthesis.

**What this contributed.** The word *markers*. The chapter has a small number of
genuinely counterintuitive moments that a reader skimming prose will slide past:
overvalued means price is **above** intrinsic value, buying high and selling
higher is a profitable scenario, covering is a buy that ends a bearish position,
a good trend-following method loses most of its trades. Those became a typed
element in the document (the trap flag) rather than a bolded clause inside a
paragraph.

### Poorvu Center for Teaching and Learning, Yale University, "Preparing a Lecture"

<https://poorvucenter.yale.edu/teaching/teaching-resource-library/preparing-a-lecture>

"Whether you lecture from an outline or from a script, it is important to verify
that you have the right amount of information." Time the lecture; if it does not
fit, narrow the topic. Indicate obvious transitions between points, and use
repetition to emphasise particularly important points.

**What this contributed.** Yale declines to insist on outline over script, which
is a useful corrective: the deliverable is not "notes must be terse". It is that
the amount of material must be verified against the clock. That is what the four
run plans are, so they were kept in full and given the first page of the
document.

## Documents that are read while doing something else

Standing in front of a class, talking, watching a room, is not a reading
posture. The closest well-studied analogue is flight-deck documentation, where
someone is operating an aircraft and consulting paper at the same time. Two NASA
contractor reports cover it directly, and both are specific enough to design
from.

### Degani, A. (1992). *On the Typography of Flight-Deck Documentation*. NASA Contractor Report 177605

<https://ntrs.nasa.gov/citations/19930010781>
(PDF: <https://ntrs.nasa.gov/api/citations/19930010781/downloads/19930010781.pdf>)

The report's own list of design recommendations, of which these were applied:

1. Sans-serif fonts are usually more legible than fonts with serifs.
4. Long chunks of text should be set in lower case.
9. Vertical spacing between lines should not be smaller than 25 to 33 percent of
   the overall size of the font.
11. Avoid using long strings of text set in italics.
12. Use primarily one or two typefaces for emphasis.
13. Use black characters over a white background for most cockpit documentation.
14. Avoid white characters over a black background. If it is wanted anyway: use
    a minimum amount of text, a relatively large typesize, and sans-serif.
15. Black over white or yellow are recommended.
16. Avoid black over dark red, green, and blue.

Section 3.7, on line length, contributed the most specific idea in the whole
document. Describing the checklist layout of challenge on the left and response
on the right, Degani writes:

> A common problem with these layouts is the large gap between the entry and the
> corresponding information (Challenge <-> Response). The wider the gap, the
> greater the chance that the reader will make a mistake through perceptual
> misalignment.

Section 3.11 adds that sub-optimal typographic conditions compound, and that the
combined penalty is worse than the sum of the parts, so a designer should not
stack several marginal choices.

**What this contributed.** Four decisions. Body text is sans and set black on
the warm paper colour, never reversed out of green. Gold is the only colour used
as a *field* behind body-sized text, because rule 15 names yellow explicitly and
rule 16 rules out the obvious alternative of the FEU green. Green is confined to
rules, headings and short chips where the text is a few words at a large size,
which is the escape clause in rule 14. And no table in this document is allowed
to open a wide gap between a label and its number: every table is set to its
content width and left-aligned rather than justified across the full measure, and
the timing figures sit immediately beside their labels.

### Degani, A., and Wiener, E. L. (1990). *Human Factors of Flight-Deck Checklists: The Normal Checklist*. NASA Contractor Report 177549

<https://ntrs.nasa.gov/api/citations/19910017830/downloads/19910017830.pdf>

Read for Appendix A, the proposed design guidelines. Four transfer directly:

- **(4)** Responses should portray the desired status or value of the item, not
  just "checked" or "set".
- **(6)** The completion call should be written as the last item, "allowing all
  crew members to move mentally from the checklist to other activities".
- **(7)** A long checklist should be subdivided into smaller task-checklists or
  chunks that can be associated with systems and functions.
- **(10)** "The most critical items on the task-checklist should be listed as
  close as possible to the beginning of the task-checklist, in order to increase
  the likelihood of completing the task before interruptions may occur."
- **(12)** Checklists should not be tightly coupled to other tasks; provide
  buffers for recovery and a way to take up the slack when completion does not
  keep pace with the external operation.

**What this contributed.** Guideline (10) is the reason the never-cut material
sits at the top of each part page and the cuttable material below it, rather than
the two being interleaved in slide order in a single list. Guideline (4) is why
the Fold entries carry the actual sentence to say rather than an instruction to
mention a topic. Guideline (6) is why every part ends with an explicit close
rather than simply stopping. Guideline (7) is why one part is one self-contained
unit that starts on a fresh page. Guideline (12) is what the run plans and the
mid-session drop rule already were, and it is the argument for keeping them.

### Butterick, M., *Practical Typography*, "Summary of key rules" and "Line length"

<https://practicaltypography.com/summary-of-key-rules.html>
<https://practicaltypography.com/line-length.html>

Point size 10 to 12 points in printed documents. Line spacing 120 to 145 percent
of point size. Average line length 45 to 90 characters including spaces. Use
bold or italic as little as possible, and not together. All caps are fine for
less than one line of text. Use centred text sparingly. Separate paragraphs with
either a first-line indent or 4 to 10 points of space, not both.

**What this contributed.** The measure was computed rather than guessed, and it
is checked by the build. The 45 to 90 band and Degani's 25 to 33 percent leading
minimum overlap with Butterick's 120 to 145 percent, so the settled values sit
inside both: 10pt body on 14pt leading (140 percent), main column 134mm, which
is about 76 characters. Bold is reserved for the one clause per paragraph that is
the point of the paragraph, and italic is not used for runs of text at all,
which also satisfies Degani rule 11.

## Cognitive load and retrieval practice

### Centre for Education Statistics and Evaluation, NSW Department of Education (2017). *Cognitive load theory: Research that teachers really need to understand*

<https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf>

Working memory holds about four chunks at once. Two effects were used:

**The redundancy effect.** Learners do not learn effectively when working memory
is spent on unnecessary or repeated information, including "the same information
in multiple forms", and the paper's example is a presenter reading the text that
is already on the screen. It quotes Sweller: "Redundancy is anything but
harmless. Providing unnecessary information can be a major reason for
instructional failure."

**The split attention effect.** When two sources of information must be
integrated to be understood, and they are separated in space, the reader has to
hold both and merge them mentally. The paper's remedy is to physically integrate
them so they do not have to be mentally integrated, and it quotes Sweller, van
Merrienboer and Paas: the evidence "suggests overwhelmingly that it has negative
consequences and should be eliminated wherever possible".

**What this contributed.** These two are the strongest constraints on the
document, and they pull against each other, which is the interesting part.

Redundancy says the notes must not restate what is on the slide. Every slide
already carries its own speaker cue in the PowerPoint notes, visible in Presenter
View. So this document deliberately carries only what is *not* on the screen and
*not* in Presenter View: the timing, the cut decision, the board work, the traps,
the folds, the department evidence, and the answer letters.

Split attention says everything needed for one moment must be in one place. That
is why the slide number sits in a rail immediately beside the sentence it belongs
to instead of in a separate index, why each part page carries its own figure list
and its own check answers rather than pointing at a central table, and why the
answer letters are printed in the notes at all rather than leaving the instructor
to hold `in-class-checks.md` in the other hand.

The one place the two effects genuinely conflict is the run plans. The per-part
skip and fold detail is repeated on the part pages after appearing in the run
plan pages. That repetition is deliberate: choosing a plan before the session and
executing a part during the session are two different tasks at two different
times, and eliminating the split attention during teaching is worth the
redundancy during preparation.

### Kenney, K. L., and Bailey, H. (2021). "Low-Stakes Quizzes Improve Learning and Reduce Overconfidence in College Students". *Journal of the Scholarship of Teaching and Learning* 21(2), 79 to 92

<https://files.eric.ed.gov/fulltext/EJ1303358.pdf> (doi:10.14434/josotl.v21i2.28650)

A real undergraduate course, 47 students, two to four retrieval questions at the
start of each class. Two findings were used. First, "while the simple practice of
retrieving information benefits memory, providing students feedback (i.e., the
correct answer) immediately after the practice test further increases its
beneficial effects", citing Butler, Karpicke and Roediger (2008). Second,
students were significantly less overconfident about material that had been
retrieved, and students who reread rather than retrieve get "the illusion of
learning" and stop studying early.

**What this contributed.** The reveal is not an afterthought, it is the half of
the check that does the work, which is why the notes put the answer letters and
the one-line reasons in the instructor's hand and repeat the standing instruction
to say the reason out loud. It is also why the run plans cut teaching minutes
roughly three times faster than they cut check minutes: on this evidence the
checks are the part with the measured effect.

### Roediger, H. L., and Karpicke, J. D. (2006)

Cited throughout Kenney and Bailey as the origin of the classroom testing effect.
**Not read in the original** for this document; everything attributed to it here
is secondhand through Kenney and Bailey.

## Teaching a room that includes students with ADHD

The brief asked specifically for what the instructor does, not what the slides
do. Two sources were usable at that level.

### University of Cambridge, Accessibility and Disability Resource Centre, "Attention Deficit (Hyperactivity) Disorder"

<https://www.disability.admin.cam.ac.uk/working-disabled-students/attention-deficit-hyperactivity-disorder-adhd>

The most directly actionable source found. Its recommendations to lecturers:

- "A synopsis at the start of the lecture and effective signposting throughout.
  At the conclusion of each lecture, review major points."
- "Signposting essential information will assist this student in determining
  salient information from non-essential details."
- "Provide adequate time for the student to assimilate or process questions and
  make notes or sequence ideas before being required to respond to a question."
- "Repeat information when necessary."
- "Information should be left on the board to allow adequate copying time."
- "Introduce new vocabulary in context with concepts explained."
- Copies of slides, handouts and reading lists provided in advance.

**What this contributed.** Almost every one of these is already an instruction
somewhere in the existing notes, but scattered. The synopsis and the review
became a fixed **Open** and **Close** line on every part page, in the same
position each time. The processing time is why the sixty second silent rule on a
check is stated as a rule rather than a suggestion. "Repeat information when
necessary" is the reteach rule when a third of the room misses an item. "Left on
the board to allow copying time" is why the board work blocks say explicitly to
leave the square and the three assumptions up for the rest of the session, and
why board work is a typed element with its own layout rather than a paragraph.
Materials in advance is why the Short plan's instruction to post Figures 1.33 and
1.34 to Canvas before the session survived into the rebuild.

### Indiana University of Pennsylvania, Disability Support Services, "Teaching Students with Attention Deficit Disorder or ADHD"

<https://www.iup.edu/disabilitysupport/resources-faculty-and-staff/teaching-students-with-attention-deficit-disorder-or-attention-deficit-hyperactivity-disorder.html>

"Keep your instructions as brief and uncomplicated as possible." For longer
classes, "consider offering a break partway through the class session". On
fidgeting or tapping, point it out quietly if it is affecting the class, "but do
not assume ill intent".

**What this contributed.** Brief instructions is a writing rule for the notes
themselves, since the instructor reads them aloud in effect. The break is why the
part boundaries are described as clean stops in the document and why the run
plans forbid splitting inside a part.

### Lagacé-Leblanc, J., Rousseau, N., and Massé, L. (2024). "How can postsecondary teachers promote the academic success of students with ADHD?" *McGill Journal of Education* 58(2), 178 to 201

<https://mje.mcgill.ca/article/view/10037>

Interviews with 29 college and university students with ADHD in Quebec and nine
disability services counsellors, coding teacher actions into seven categories:
visual support, comprehension support, assessment support, time management
support, organisation of information, teaching strategies, and the
teacher-student relationship. **Only the abstract and the article's summary of
its own categories were read**, not the full text, so it is cited here as
corroboration for the shape of the categories rather than for any specific
finding.

## What could not be verified, and what is contested

**The ten to fifteen minute attention span is not supported.** The project README
justifies many small slides for a room that includes students with ADHD. The
design is sound but the usual folk justification for it is not.

Wilson, K., and Korn, J. H. (2007). "Attention During Lectures: Beyond Ten
Minutes". *Teaching of Psychology* 34(2), 84 to 89.
<https://journals.sagepub.com/doi/10.1080/00986280701291291>

They reviewed note-taking studies, direct observation, self-report and
physiological measures, and concluded:

> It is clear that students' attention does vary during lectures, but the
> literature does not support the perpetuation of the 10- to 15-min attention
> estimate. Perhaps the only valid use of this parameter is as a rhetorical
> device to encourage teachers to develop ways to maintain student interest in
> the classroom.

So nothing in this document claims a slide should be short because attention
collapses on a clock. The one-idea-per-slide design and the frequent checks are
justified here on the signposting and processing-time evidence from Cambridge and
on the retrieval practice evidence from Kenney and Bailey, both of which are
about what is done rather than about when attention is presumed to fail.

**Cognitive load theory's evidence base is narrower than its use here.** The CESE
paper says so itself: the randomised trials are concentrated in maths, science
and technology, far less work exists in less technical subjects, and the
literature mostly does not address individual differences other than expertise.
Beyond that, split attention and redundancy are results about *learners studying
instructional material*. Applying them to an instructor consulting a reference
document while working is an argument by analogy. It is a good analogy, and the
flight-deck literature is doing the same job from the other direction, but it is
an extension and not a finding.

**No source was found on teaching notes as a designed artefact.** Every teaching
centre consulted describes what a lesson plan should *contain*. None of them
discusses what one should *look like* on the page, how it should be typeset, or
how it should be laid out for use while standing. The SMU page links to a USC
Center for Excellence in Teaching resource that appears to address "what about
your teaching notes? How much should you write down and bring to class with
you?", but the underlying resource could not be retrieved. That gap is why the
flight-deck literature is carrying the visual design in this document.

**Marcellus SC is not installed on this build machine.** The display face falls
back to Palatino, exactly as the deck does and for the same reason, documented in
`build/README.md`. The PDF as committed is the Palatino rendering. Installing the
identity face and rebuilding will change the display face and may move page
breaks, so re-render and look at the pages again if you do that.

## The decisions

### Structure

| Decision | Source |
|---|---|
| Notes carry only what is not on the slide and not in Presenter View | Redundancy effect (CESE) |
| One part per fresh page, self-contained | Degani and Wiener guideline (7) |
| Never-cut material at the top of the part, cuttable below | Degani and Wiener guideline (10) |
| Every part ends with an explicit close | Degani and Wiener guideline (6) |
| Fixed **Open** and **Close** lines in the same position on every part | Cambridge synopsis and review |
| Run plans get the first page, before any teaching content | CRLT step 1 triage; Yale on verifying against the clock |
| Fold entries carry the sentence to say, not the topic to mention | Degani and Wiener guideline (4) |
| Department evidence kept as its own reference page | CRLT ranking of objectives needs a stated basis |

### The page

| Decision | Value | Source |
|---|---|---|
| Page size | A4, 18mm side margins, 15mm top, 16mm bottom | Print-first requirement |
| Layout | 34mm cue rail, 6mm gutter, 134mm main column | Split attention; measure below |
| Measure | about 76 characters | Butterick 45 to 90 |
| Body | 10pt on 14pt, 140 percent | Butterick 120 to 145; Degani rule 9 (25 to 33 percent) |
| Body face | Arial, sans | Degani rule 1; matches `build/README.md` |
| Display face | Marcellus SC, falling back to Palatino | FEU identity; matches the deck |
| Mono | Courier New, for answer letters, slide numbers and data | Brief; matches the deck |
| Emphasis | Bold only, one clause per paragraph, no italic runs | Butterick; Degani rules 11 and 12 |
| Body colour | Ink `#1a1a1a` on paper `#faf8f2` | Degani rules 13 and 15 |
| Gold `#F2A900` | The only colour used as a field behind body-sized text | Degani rule 15 names yellow |
| Green `#007A33` | Rules, headings and short chips only, never a field under a paragraph | Degani rules 14 and 16 |
| Tables | Sized to content, label and value kept adjacent | Degani section 3.7, perceptual misalignment |

### Keyed to the deck

The deck has 218 numbered slides and a progress marker on every one. The notes
had no slide numbers at all, so matching a page to the screen meant reading a
paragraph and recognising a phrase.

The build now resolves every reference against the real deck. The notes content
module names slides by stable key (`fig:1.11`, `check:13`, `term:Price`,
`slide:The four ways a trade actually makes money`, `part:3`, `recap:3`), and
`build/build_plan.py` walks `build/content_chapter01.py` with the same traversal
`deckkit.build` uses to number slides, then substitutes the real numbers. A key
that does not resolve fails the build.

This means the numbers cannot drift when the deck changes, and it means the cue
rail can carry a real slide number beside every instruction. It is also what
makes the timing arithmetic checkable: the build recomputes the per-part slide
and figure counts from the deck rather than trusting the prose.

### What the document turned out to be

23 A4 pages, in this order:

| Pages | What | Why there |
|---|---|---|
| 1 | The run card: the plans as one table, the two standing rules, the pre-flight | The triage decision, made before the deck opens (CRLT step 1) |
| 2 | Standing instructions: which deck, the three carriers, running a check, running a figure slide | Read once a semester, not during a session |
| 3 | What the department examines: the Quiz 1 item map, Homework 1, the seven objectives, all with slide numbers | The stated basis for every cut marker |
| 4 to 7 | The run plans, and one mark-the-deck table | Marking the deck is a task of its own, done before the session |
| 8 to 22 | One part per opening, six parts | The working document, read while teaching |
| 23 | The review question crib and the quiz preparation to mention | Read at the end of the session |

Each part opens with a fixed masthead in the same position every time: part
number, slide range, the progress marker text, the four plan timings as four
large monospace numbers, the checks with their answer letters and slide
numbers, the figures with their slide numbers and the plan each is cut at, an
Open line, a Close line, and the terms taught. That band is the two second
answer to "where am I, how long have I got, what is next". Under it sits the
Core / Reinforcement / Enrichment / Fold ladder, and under that the teaching
run in slide order with a cue rail carrying the slide number beside every
instruction.

One decision worth recording because it was not in the plan. The old notes
carried a skip list and a fold list inside the Long plan, a longer skip list
and another fold list inside the Standard plan, and the same material again in
the per-part cut markers. Marking a deck from that meant holding four lists and
a plan name at once. They are now a single table, in deck order, with three
columns: the slide, what it is, and the sentence to say when it is folded
rather than dropped. That is Degani and Wiener's guideline (4) applied to a
plan: the entry carries the value, not a pointer to it.

### What was kept from the old notes

Everything that earns its place, which is nearly all of it: the run plans
with their skip, keep and fold lists, the Core / Reinforcement / Enrichment /
Fold markers for all six parts, the per-part figure lists, the evidence section
on Quiz 1, Homework 1 and the seven booklet objectives, the guidance on running a
check and running a figure slide, the board work, the handclap, the EMH ladder
table, the review question crib, and the quiz preparation note.

What changed is the order and the typography, not the substance. The old file
grouped all cut markers into one dense bullet per part and then told the teaching
story in a separate prose run. The rebuild interleaves them against slide
numbers, so the page can be read top to bottom while the deck advances, with the
triage summary sitting above it in a fixed position.

## How it is built, and the two things that fought back

```
.venv/bin/python build/build_plan.py
```

HTML with real print CSS, rendered by headless Chrome. Two mechanics are worth
knowing before anyone changes the build.

**Pagination is done inside the page.** A script in the document measures each
block and distributes blocks into fixed A4 sheets, then stamps a footer on each
one. Chrome cannot put a part name and a page number in a running footer by
itself (it has no support for CSS `@page` margin boxes), and its own pagination
will happily split a table across a break or strand a heading at the foot of a
sheet. Doing it in the document buys all three of the print-first requirements
at once. Blocks are atomic; only ordinary prose splits, and only between its
own paragraphs.

**Chrome writes the PDF and then does not exit.** Chrome 151 in
`--headless=new --print-to-pdf` mode finishes the file in about five seconds on
this machine and then hangs indefinitely. Waiting on the process took over two
minutes and usually hit the timeout. `render_pdf` polls instead: it waits for
the file to appear, for its size to settle, and for it to end in `%%EOF`, then
terminates Chrome. Build time went from over two minutes to six seconds.

### Then look at it. Every page.

```
DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf /tmp/plan $(seq 1 23)
```

This is not a formality, and doing it caught real defects that no amount of
reading the source would have found:

- A sheet kicker printed a raw `{s:slide:Chapter 1 in five sentences}`
  placeholder, because that one field was escaped without being run through the
  resolver first. It looked fine in the code.
- Checks with no instructor note rendered an empty white strip under the header
  bar.
- Italic is not a supported inline form, so `*probable*` printed with its
  asterisks. Exactly the failure mode of the document this replaced.
- The cue rail ran s81, s85, s84 in Part 3, because two blocks were in the
  wrong order. The rail is only useful if it counts upward.
- The ladder's text column sat 6mm to the left of every other content column,
  because `box-sizing: border-box` puts the padding inside the declared width.

Four passes were needed. The first came out at 26 pages with several sheets
more than 80 percent empty; measuring the leftover height per page rather than
guessing at it is what fixed that, and the final document is 23 pages with no
sheet stranded. The one page that is deliberately near-empty is the
mark-the-deck table, which is a working sheet and wants to be alone.
