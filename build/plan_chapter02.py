"""FIN1209 Chapter 2 run card, as plain data.

Three pages, and deliberately not a teaching plan. Chapter 1 shipped a 26 page
one and the instructor said plainly, after teaching from it on 2026-09-02,
that he did not really use it. What failed him was not the depth. It was the
pacing: he had 180 minutes and reached the end of Part 4 of 6.

So this document does three things and nothing else.

  1. What each part costs in minutes, with an honest total, and the wall
     clock time he should be starting each part at.
  2. What to cut first, second and third, named slide by slide with the
     minutes each cut buys.
  3. What must not be cut, with the reason: a check or Homework 1 rests on it.

**The minutes are calibrated, not estimated.** Chapter 1's front matter plus
its first four parts is 155 slides, and that is what 180 minutes actually
bought in the room. Every minute figure below is Chapter 2's own slide mix
costed at that measured rate. See chapter-02/README.md for the arithmetic.

Layout is build/notekit.py, which knows nothing about any chapter. This file
carries no layout and no typed slide numbers: slides are named by stable key
and build_plan2.py resolves them against the deck, so a content change moves
this card with it and a broken reference fails the build.
"""

from __future__ import annotations

from notekit import Bullets, Flag, Notes, Prose, Sheet, Table


# ==========================================================================
# Page 1 - the clock
# ==========================================================================

THE_CLOCK = Sheet(
    title="Where you should be, minute by minute",
    kicker="Read this before you open the deck",
    footer="The clock",
    blocks=(
        Prose(
            cue="The honest number",
            text=(
                "Chapter 2 is 175 slides. At the pace you actually taught "
                "Chapter 1, that is **about 202 minutes, and the session is "
                "180.** The chapter does not fit as it stands, and it is "
                "better to know that now than at the 90 minute mark."
                "\n\n"
                "That rate is measured, not guessed. Chapter 1's openers plus "
                "its first four parts is 155 slides, and 155 slides is what "
                "180 minutes bought. Every minute below is Chapter 2's own "
                "mix of terms, figures, charts and checks priced at that rate."
            ),
        ),
        Table(
            cue="Read the last two columns",
            title="Minutes per part, and the clock time to start it",
            full=True,
            compact=False,
            headers=("Part", "Slides", "Full", "Start at", "Cut", "Start at"),
            align=("l", "n", "n", "n", "n", "n"),
            rows=(
                ("Openers and roadmap", "4", "6", "0:00", "6", "0:00"),
                ("1  Origins", "21", "25", "0:06", "23", "0:06"),
                ("2  Discounting", "20", "23", "0:31", "21", "0:29"),
                ("3  Primary trend", "38", "43", "0:54", "36", "0:50"),
                ("4  Secondary and minor", "20", "23", "1:37", "21", "1:26"),
                ("5  Phases and reversal", "32", "38", "2:00", "34", "1:47"),
                ("6  Confirmation and volume", "36", "40", "2:38", "34", "2:21"),
                ("Wrap up and homework", "4", "5", "3:18", "5", "2:55"),
                ("Whole chapter", "175", "202", "ends 3:23", "180", "ends 3:00"),
            ),
            note=(
                "Full is the deck with nothing dropped. Cut is the same deck "
                "with Cut 1 and Cut 2 from page 2 taken before you start. "
                "Slide counts run from the part divider to the recap, which "
                "is what the progress marker counts."
            ),
        ),
        Flag(
            kind="rule",
            cue="At every part boundary",
            title="Check the clock against the column you are running",
            text=(
                "If you are more than five minutes late starting a part, "
                "take the next unused cut on page 2 **before** you begin it, "
                "not during it. Cutting inside a part is how a session ends "
                "in the middle of an argument."
            ),
        ),
        Prose(
            cue="If it slips anyway",
            text=(
                "**Stop at the end of Part 5 and carry Part 6 to the next "
                "session.** Part 6 is the only part that is genuinely self "
                "contained: two tenets and the seven criticisms, with nothing "
                "later in the chapter depending on it. Every other boundary "
                "leaves something owed."
                "\n\n"
                "If you do split, the wrap up slides are three minutes and "
                "they carry Homework 1 and the Elliott note. **Run them at "
                "the end of the first session anyway**, whatever else you "
                "drop, or the homework never gets set."
            ),
        ),
    ),
)


# ==========================================================================
# Page 2 - the first two cuts
# ==========================================================================

THE_CUTS = Sheet(
    title="What to cut, in this order",
    kicker="When the clock is against you",
    footer="Cuts 1 and 2",
    blocks=(
        Table(
            cue="The ladder",
            title="What each cut buys",
            compact=True,
            headers=("Cut", "What comes out", "Minutes", "Chapter runs"),
            align=("l", "l", "n", "n"),
            rows=(
                ("None", "The whole deck", "", "202"),
                ("1", "Nine repeat pictures", "9", "193"),
                ("2", "All eight charts, and eight slides", "14", "179"),
                ("3", "Three checks", "9", "170"),
            ),
            note=(
                "Take 1 and 2 before you start if the session is 180 minutes. "
                "Cut 3 is the emergency and costs you a reading of the room."
            ),
        ),
        Prose(
            cue="Cut 1",
            text=(
                "**Nine pictures that repeat a picture you have already "
                "shown.** Nothing is lost but the second telling. Each one is "
                "about a minute."
            ),
        ),
        Bullets(
            cue="Skip these",
            title="Cut 1, nine figures",
            items=(
                "Slides `{s:fig:2.6}` and `{s:fig:2.7}`, Figures 2.6 and 2.7. "
                "Long run examples; Figure 2.5 shows the shape already.",
                "Slides `{s:fig:2.10}` and `{s:fig:2.11}`, Figures 2.10 and "
                "2.11. The second scaling pair; 2.8 and 2.9 make the point.",
                "Slide `{s:fig:2.13}`, Figure 2.13. Several reactions at once; "
                "Figure 2.12 carries the argument on its own.",
                "Slide `{s:fig:2.19}`, Figure 2.19. The bottom reversals; the "
                "book says the same rationale applies in reverse.",
                "Slides `{s:fig:2.23}` and `{s:fig:2.24}`, Figures 2.23 and "
                "2.24. Correlated markets; the tenet is made on 2.20 to 2.22.",
                "Slide `{s:fig:2.26}`, Figure 2.26. The second volume example; "
                "Figure 2.25 is the same test done once.",
            ),
        ),
        Prose(
            cue="Cut 2",
            text=(
                "**Every chart, and eight slides that restate their "
                "neighbour.** No check and no homework needs any of them. The "
                "charts are ours and they only ever illustrate a term that "
                "has already been taught; they never introduce one."
            ),
        ),
        Bullets(
            cue="Skip these too",
            title="Cut 2, eight charts and eight slides",
            items=(
                "All eight charts: slides `{s:chart:A}`, `{s:chart:B}`, "
                "`{s:chart:C}`, `{s:chart:D}`, `{s:chart:E}`, `{s:chart:F}`, "
                "`{s:chart:G}` and `{s:chart:H}`.",
                "Slide `{s:slide:Charles H. Dow}`, Charles H. Dow. The names "
                "are all on the next two slides.",
                "Slide `{s:slide:What the analyst does with that}`, effects "
                "not causes. Chapter 1 taught it.",
                "Slide `{s:slide:Tides, waves and ripples}`, tides, waves and "
                "ripples. A mnemonic, and nothing is set on it.",
                "Slide `{s:slide:Dow thought the trade was worth it}`, Dow "
                "thought it worth it. The examined number is the slide before.",
                "Slide `{s:slide:Who is on each side during accumulation}`, "
                "who is on each side. The term slide carries both already.",
                "Slide `{s:slide:The longer the base, the bigger the move out "
                "of it}`, the longer the base. One sentence, and it points at "
                "Chapter 4.",
                "Slide `{s:slide:Confirmation between closely correlated "
                "markets}`, correlated markets. Goes with 2.23 and 2.24 above.",
                "Slide `{s:slide:And volume is only a secondary indicator}`, "
                "volume is secondary. Check 19's reveal says it too.",
            ),
        ),
    ),
)


# ==========================================================================
# Page 3 - the emergency cut, and what is not on the table
# ==========================================================================

THE_FLOOR = Sheet(
    title="The emergency cut, and the floor",
    kicker="Below this, do not go",
    footer="Cut 3, and what must stay",
    blocks=(
        Prose(
            cue="Cut 3",
            text=(
                "**Three checks, and only these three.** Each one sits beside "
                "another check in the same part that covers the same ground, "
                "so the part can still read the room. Three minutes each."
            ),
        ),
        Bullets(
            cue="Skip both slides",
            title="Cut 3, three checks and their reveals",
            items=(
                "Check 3, slide `{s:check:3}`, on the averages. Part 6 comes "
                "back to the two averages in the seventh criticism.",
                "Check 15, slide `{s:check:15}`, on who is buying. Check 14 "
                "in the same part already sets the phases.",
                "Check 21, slide `{s:check:21}`, on what survives. Check 20 "
                "in the same part already sets the criticisms.",
            ),
        ),
        Flag(
            kind="trap",
            cue="Never",
            title="Two things that are never a cut",
            text=(
                "**Never drop a reveal without its question, or a question "
                "without its reveal.** The letter alone teaches nothing and "
                "the question alone reads the room and then abandons it."
                "\n\n"
                "**Never drop a term slide.** Every check in this chapter is "
                "answerable from a term or a content slide that comes before "
                "it, and the student edition has no speaker notes to fall "
                "back on."
            ),
        ),
        Prose(
            cue="The floor",
            text=(
                "Seven things carry a check, a past paper item or Homework 1. "
                "**They stay in at 202 minutes and they stay in at 150.**"
            ),
        ),
        Bullets(
            cue="These stay",
            numbered=True,
            title="What must not be cut, and why",
            items=(
                "**The six basic tenets**, slide `{s:slide:The six basic "
                "tenets of Dow Theory}`. Check 4 sets the trap on it: the "
                "tenet is that **primary** trends have three phases.",
                "**Uptrend and downtrend**, slides `{s:term:Uptrend}` and "
                "`{s:term:Downtrend}`, with Figure 2.4 on slide `{s:fig:2.4}`. "
                "Homework 1 is find a trend and interpret it, so this **is** "
                "the homework. Check 8 sets a sequence on it.",
                "**Penetration**, slide `{s:term:Penetration}`. The theory's "
                "only signal, and Check 9 sets it.",
                "**How far back a reaction comes**, slide `{s:slide:How far "
                "back a reaction usually comes}`, with Figure 2.12 on slide "
                "`{s:fig:2.12}`. Checks 11 and 12 both rest on them.",
                "**The three phases**, slide `{s:slide:The third tenet: "
                "primary trends have three phases}`, and **why accumulation "
                "is longer**, slide `{s:slide:Why accumulation lasts longer "
                "than distribution}`. Check 14, and review question 6.",
                "**Confirmation**, slide `{s:term:The averages must confirm "
                "one another}`, and **the four volume conditions**, slide "
                "`{s:slide:The four conditions, in full}`. Checks 18 and 19, "
                "and both are past paper items.",
                "**The wrap up**, slides `{s:slide:Chapter 2 in five "
                "sentences}` to `{s:slide:Next: mechanics and dynamics of "
                "charting}`. Three minutes, and the only place Homework 1 is "
                "set.",
            ),
        ),
        Prose(
            cue="One more",
            text=(
                "The answer letters for all 21 checks are in "
                "`chapter-02/in-class-checks.md`, which is generated from the "
                "same content the deck is. **Print that, not this.** This "
                "card is for the clock."
            ),
        ),
    ),
)


# ==========================================================================

PLAN = Notes(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 2",
    title="Introduction to Dow Theory",
    presenter="Benjamin C. Sotelo, Institute of Accounts, Business and "
              "Finance, FEU Manila",
    doc_kind="run card",
    # One session, one run. Chapter 1 offered five plans and the instructor
    # used none of them, so this card names the cuts rather than the plans.
    plans=(),
    front=(THE_CLOCK, THE_CUTS, THE_FLOOR),
    parts=(),
    back=(),
)
