# Chapter 2 - Check answerability audit

**A check must be answerable from the slides alone.** The student edition
carries no speaker notes, so a fact that lives only in a cue is a fact the
student never meets, and nothing in the room guarantees the instructor said
it out loud anyway. The same goes for the lecture notes and for the book.
Two things have to hold for every item:

1. Some slide in the deck carries the answer, in text the student can read.
2. **That slide comes before the check**, not after it.

`deckkit.validate()` cannot see either one. Chapter 1 was audited to this
standard after it shipped and two of its fifty items failed: one check sat in
front of the slide it examined, and one question named a term that only a
speaker note ever said out loud. Chapter 2 was built to the standard from the
start and audited before it shipped.

## Result

**42 items, 42 pass.** Every item has an answering slide, every answering
slide is a term slide or a content slide whose text a student can read, and
every one of them comes earlier in the deck than the check that examines it.
No item rests on a speaker cue, on a figure caption alone, or on the book.

Two consequences worth recording, because they are what makes the run card
safe:

- **No item rests on one of this course's own charts.** All eight charts
  illustrate a term that has already been taught. That is why the run card
  can drop all eight as one cut without breaking a check.
- **No item rests on any of the nine figures the run card's first cut
  drops.** Where a figure carries an argument a check examines, that figure
  is on the run card's floor instead: Figure 2.4 and Figure 2.12.

## Method

For each of the 42 items, the answering slide was identified by hand and its
slide number compared against the check's own slide number. The slide numbers
below are the teaching edition's, which is the edition the instructor
presents from; the student edition renumbers, but only by removing checks, so
the ordering is unaffected.

Speaker notes were excluded from the search on purpose. So were the lecture
notes. A student sitting in the room with the student edition open is the
reader this audit is written for.

## The 42 items

| Check | Q | Ans | Part | Answering slide | Check slide | Before? |
|---|---|---|---|---|---|---|
| 1 | Q1 | C | 1 | 9 (content) The three who came after him | 11 | yes |
| 1 | Q2 | A | 1 | 9 (content) The three who came after him | 11 | yes |
| 2 | Q1 | D | 1 | 14 (term) The primary trend is not susceptible to manipulation | 16 | yes |
| 2 | Q2 | B | 1 | 15 (term) Dow Theory is not perfect | 16 | yes |
| 3 | Q1 | A | 1 | 18 (content) 1884: eleven stocks | 23 | yes |
| 3 | Q2 | C | 1 | 22 (content) What those two averages are called now | 23 | yes |
| 4 | Q1 | C | 2 | 27 (content) The six basic tenets of Dow Theory | 29 | yes |
| 4 | Q2 | D | 2 | 28 (content) And one more rule that is not on the list | 29 | yes |
| 5 | Q1 | B | 2 | 34 (term) Acts of God | 37 | yes |
| 5 | Q2 | C | 2 | 15 (term) Dow Theory is not perfect | 37 | yes |
| 6 | Q1 | D | 2 | 40 (term) Only closing prices are recognized | 43 | yes |
| 6 | Q2 | B | 2 | 41 (content) And the size of the move does not matter | 43 | yes |
| 7 | Q1 | B | 3 | 47 (term) The market has three trends | 53 | yes |
| 7 | Q2 | C | 3 | 49 (content) The three, named | 53 | yes |
| 8 | Q1 | C | 3 | 57 (term) Uptrend | 62 | yes |
| 8 | Q2 | D | 3 | 61 (content) What the first lower peak means | 62 | yes |
| 9 | Q1 | A | 3 | 64 (term) Penetration | 69 | yes |
| 9 | Q2 | B | 3 | 65 (content) The price of waiting for it | 69 | yes |
| 10 | Q1 | A | 3 | 75 (term) Logarithmic scaling | 81 | yes |
| 10 | Q2 | C | 3 | 75 (term) Logarithmic scaling | 81 | yes |
| 11 | Q1 | C | 4 | 86 (content) How far back a reaction usually comes | 89 | yes |
| 11 | Q2 | D | 4 | 86 (content) How far back a reaction usually comes | 89 | yes |
| 12 | Q1 | A | 4 | 91 (content) When the primary trend resumes | 94 | yes |
| 12 | Q2 | B | 4 | 86 (content) How far back a reaction usually comes | 94 | yes |
| 13 | Q1 | A | 4 | 68 (content) What Dow Theory says you may trade | 101 | yes |
| 13 | Q2 | C | 4 | 98 (term) Line | 101 | yes |
| 14 | Q1 | D | 5 | 105 (content) The third tenet: primary trends have three phases | 117 | yes |
| 14 | Q2 | A | 5 | 112 (content) Why accumulation lasts longer than distribution | 117 | yes |
| 15 | Q1 | B | 5 | 106 (term) Accumulation phase | 119 | yes |
| 15 | Q2 | C | 5 | 111 (term) Distribution phase | 119 | yes |
| 16 | Q1 | B | 5 | 121 (term) A trend persists until its reversal is indicated | 131 | yes |
| 16 | Q2 | C | 5 | 126 (term) Non failure swing | 131 | yes |
| 17 | Q1 | B | 5 | 126 (term) Non failure swing | 133 | yes |
| 17 | Q2 | A | 5 | 127 (term) Double top and double bottom | 133 | yes |
| 18 | Q1 | B | 6 | 137 (term) The averages must confirm one another | 147 | yes |
| 18 | Q2 | C | 6 | 138 (content) The signal is dated by the later average | 147 | yes |
| 19 | Q1 | A | 6 | 150 (content) The four conditions, in full | 156 | yes |
| 19 | Q2 | B | 6 | 149 (term) Volume must confirm the trend | 156 | yes |
| 20 | Q1 | C | 6 | 160 (content) 2. The primary trend is susceptible to manipulation | 166 | yes |
| 20 | Q2 | B | 6 | 165 (content) 7. The two averages no longer measure what they used to | 166 | yes |
| 21 | Q1 | D | 6 | 168 (content) What the book still claims for Dow Theory | 169 | yes |
| 21 | Q2 | B | 6 | 159 (content) 1. It suits the equity markets better than anything else | 169 | yes |

## The three items that were closest to failing

None of these fail. They are recorded because they are where a later edit
would break the standard first.

**Check 12, Q2.** The stem gives the scenario itself: a reaction retraces
about 75 percent and the primary bull trend then resumes. The answer, that
depth alone does not settle what a move is, follows from the one third to two
thirds guide on slide 86 read against the stem. An earlier draft of this item
opened with "Figure 2.12 shows a reaction of about 75 percent", which would
have made the item depend on a figure. It was rewritten to be self contained.

**Check 15, Q2.** The phrase *irrational exuberance* appears in exactly one
place a student can read: the formal definition on the distribution phase
term slide. If that phrase is ever trimmed out of the definition, this item
loses its only source.

**Check 5, Q2.** The answer, that Dow Theory is not infallible, is taught in
Part 1 and examined in Part 2. That is legitimate and it is the only item in
the chapter that reaches back across a part boundary, so it is the one to
check first if Part 1 is ever reordered.

## What is not audited here

The answer key distribution is enforced by the build and does not need an
audit: no letter may hold more than 35 percent or fewer than 15 percent of
the items and no three consecutive items may share an answer. Chapter 2 comes
out at A 21 percent, B 31, C 31, D 17, with no run of three. `build/README.md`
has the rule and why it exists.
