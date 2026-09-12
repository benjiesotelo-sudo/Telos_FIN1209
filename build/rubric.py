#!/usr/bin/env python3
"""The course's general rubric for written answers, as plain data.

Every quiz and activity in FIN1209 that asks for a written answer is marked
with this rubric, and every one of them prints it from here. **Nothing in a
content module retypes these words.** A document imports `WRITTEN` and hands
it to its renderer, the same way the lecture notes take their summary from the
deck instead of holding a copy.

The reason is one this course has already paid for. The Chapter 1 activity
told students to mark their chart in pen on paper after the submission had
become a spreadsheet, because the instruction lived in two places and only one
of them was changed. A rubric copied into each document would drift the same
way, and a student marked on one wording while reading another is the worst
place for that to happen.

What lives here: the words of the rubric and the arithmetic that turns its
percentages into marks. What does not: how a page lays it out, which is the
renderer's job (`activitykit.written_rubric`), and the worked examples, which
have to be written on each document's own material and so live beside that
document's content.

**It applies only to written answers with no single correct response.** A
value read off the record, a date, a count, a formula's result, is right or
wrong and needs no rubric. The levels are percentages so that the same rubric
marks a question worth four points or forty.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Criterion:
    """One thing a marker looks for in a written answer."""
    name: str
    means: str
    # False for a criterion the rubric names and teaches but never marks.
    marked: bool = True


@dataclass(frozen=True)
class Level:
    name: str
    percent: int
    looks_like: str


@dataclass(frozen=True)
class Rubric:
    title: str
    # Printed first, where it cannot be missed.
    disclaimer: str
    applies: str
    criteria: tuple[Criterion, ...]
    levels: tuple[Level, ...]

    def __post_init__(self) -> None:
        percents = [lv.percent for lv in self.levels]
        if percents != sorted(percents, reverse=True):
            raise ValueError("rubric levels must run from most to least")
        if percents[0] != 100 or percents[-1] != 0:
            raise ValueError("rubric levels must run from 100 to 0 percent")

    @property
    def marked(self) -> tuple[Criterion, ...]:
        return tuple(c for c in self.criteria if c.marked)

    @property
    def unmarked(self) -> tuple[Criterion, ...]:
        return tuple(c for c in self.criteria if not c.marked)

    def level(self, name: str) -> Level:
        for lv in self.levels:
            if lv.name == name:
                return lv
        raise KeyError(f"the rubric has no level called {name!r}")

    def marks(self, out_of: float) -> tuple[tuple[Level, float], ...]:
        """Every level as marks on a question worth `out_of`.

        Computed, never typed, so a document cannot print a mark that
        disagrees with the percentage it came from.
        """
        return tuple((lv, out_of * lv.percent / 100) for lv in self.levels)


# --------------------------------------------------------------------------
# The rubric
# --------------------------------------------------------------------------

WRITTEN = Rubric(
    title="How a written answer is marked",
    disclaimer=(
        "**We are marking whether your answer is grounded and whether it "
        "follows, not how long it is.** A long answer that wanders earns less "
        "than two precise sentences."
    ),
    applies=(
        "This rubric is for written answers that have no single correct "
        "response. Anything that can be checked against the record, a price, "
        "a date, a count, is simply right or wrong, and no rubric is needed "
        "for it."
    ),
    criteria=(
        Criterion(
            name="Grounded",
            means=(
                "Your answer points at something specific and checkable on "
                "your own chart: a price, a date, a shape. Not \"the market "
                "looks bullish\", but \"the trough on this date, at this "
                "price, is higher than the one before it\"."
            ),
        ),
        Criterion(
            name="Connected",
            means=(
                "Your conclusion follows from what you pointed at. It is "
                "possible to name three real things and then conclude "
                "something that has nothing to do with them."
            ),
        ),
        Criterion(
            name="Honest",
            marked=False,
            means=(
                "A strong answer also names what argues against it. This is "
                "what the best answers do, and it is worth learning to do. "
                "**No marks are lost for leaving it out.**"
            ),
        ),
    ),
    levels=(
        Level("Full", 100, "Grounded and connected."),
        Level("Partial", 75,
              "One of the two is weak: the evidence is vague, or the "
              "conclusion does not quite follow from what was named."),
        Level("Minimal", 50,
              "There is a reason, but it is general rather than taken from "
              "your own chart."),
        Level("None", 0,
              "A conclusion with no reasoning, or nothing written."),
    ),
)
