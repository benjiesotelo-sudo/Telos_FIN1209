"""Deck 2: the Stock Desk guide, one feature per slide.

Plain data, read by build_special_lecture_deck2.py. Presented by Benjamin
C. Sotelo alone (his own 25 Nov answer); a guide he can present from or
skip, not a hands-on walkthrough like deck 1, since Stock Desk is his own
tool, not something the class builds. Built only from the real screenshots
in the firstmate home's data/stock-desk-guide/guide/png/ (step01 through
step10) and the plain-words captions in that guide's own report.md, both
confirmed fixed (badges beside, not on; sharp 2x crops) by that report's
own 25 Nov revision note.

Every position or trade shown is made-up, never a real holding of his, per
his own instruction for this deck: steps 6, 7 and 9 show a single test
trade (MU, 1 share, logged and closed the same day) made only to
demonstrate those screens while building the guide, confirmed deleted from
the real tool afterward (see that report's "Database cleanup check").

Neutral Metropolis visual style, not FEU's; see special_lecture_kit.py.
"""

from __future__ import annotations

import deckkit

SPEAKERS = (
    ("Benjamin C. Sotelo", "Lecturer, FIN1209"),
)

TITLE = deckkit.TitleSlide(
    course="FIN1209 - Technical Analysis in Investment",
    chapter="Special lecture 2 of 3",
    title="The Stock Desk",
    subtitle="A guide to my own live stock tool, one feature per slide",
    presenter="Benjamin C. Sotelo",
    notes=(
        "Presented by Benjamin C. Sotelo alone (his own 25 Nov answer).",
        "This is a guide, skippable in class; not a hands-on exercise "
        "like deck 1, since Stock Desk is his own tool, not something "
        "the class builds.",
        "Students never get the passphrase or access; this is a "
        "demonstration, never a class assignment.",
    ),
)

INTRO = deckkit.Content(
    title="What is the Stock Desk?",
    lines=(
        "A live stock tool I built the same way as deck 1: an AI CLI "
        "tool, Git and GitHub, start to finish.",
        "It tracks five stocks plus the S&P 500, with live prices and "
        "Chapter 8's buy and sell signals.",
        "It is mine, not yours: a demonstration of what these tools "
        "can build, not a class assignment.",
    ),
    accent=("This deck is a guide you can read at your own pace; I may "
            "skip some of it in class."),
)

# One slide per guide step. "shows" is the plain-words caption from the
# guide's own report.md; "note" is this deck's own addition where a step
# needs the made-up-positions disclosure.
STEPS = [
    dict(
        title="Sign in",
        image_file="step01-signin.png",
        shows=("The whole page sits behind a passphrase; this is the "
               "only screen anyone sees without it."),
        note=None,
    ),
    dict(
        title="Pick a stock, change the timeframe, change the view",
        image_file="step02-pick-stock-timeframe-view.png",
        shows=("The watchlist on the left; tap a stock to open it. "
               "Four timeframe buttons change the chart's range; three "
               "view buttons (1 stock / 1 + list / 3 at once) change "
               "the layout."),
        note=None,
    ),
    dict(
        title="Read the chart",
        image_file="step03-read-chart.png",
        shows=("20 and 50-day averages, BUY/SELL marks from Chapter 8's "
               "five-bar rule, volume, RSI and MACD below the price."),
        note=None,
    ),
    dict(
        title='Read "Last signal fired" and the live reading',
        image_file="step04-last-signal-live.png",
        shows=("The last real buy or sell and the four checks behind "
               "it; a line below it always shows where today stands, "
               "signal or not."),
        note=None,
    ),
    dict(
        title="Read the scoreboard",
        image_file="step05-scoreboard.png",
        shows=("How often past signals were right 5 trading days "
               "later. Too few signals yet to prove a rule; the count "
               "stays beside every score."),
        note=None,
    ),
    dict(
        title="Log a buy and read the position card",
        image_file="step06-log-buy-position-card.png",
        shows=("Logging a buy gives an advice-only stop and target; a "
               "sell signal never forces an exit, I decide."),
        note=("Made up: a test buy (MU, 1 share) logged only to build "
              "this guide, closed and deleted from the real tool the "
              "same day; not a real holding of mine."),
    ),
    dict(
        title="Log a sell",
        image_file="step07-log-a-sell.png",
        shows="Closing a logged position the same way, by its own price and date.",
        note=("Made up: the same test trade's closing side, since "
              "deleted; not a real sale of mine."),
    ),
    dict(
        title="Add and remove a stock",
        image_file="step08-add-stock.png",
        shows=("Type a ticker and tap Add; only stocks with complete "
               "SEC figures are accepted. Tap a card's x to remove it."),
        note=None,
    ),
    dict(
        title="Play the replay",
        image_file="step09-replay.png",
        shows=("Plays back the last session in about 2 minutes, "
               "signals firing as they would have, worked out only "
               "from bars already shown."),
        note=("The buy/sell log shown is the same made-up test trade "
              "as the last two slides, since deleted."),
    ),
    dict(
        title="Sign out",
        image_file="step10-signout.png",
        shows=("One tap signs out; anyone else stops at the sign-in "
               "screen and sees nothing, not even the charts."),
        note=None,
    ),
]

CLOSING = deckkit.Closing(
    title="Thank you",
    lines=(
        "Thank you for joining today's special lecture.",
        "Stock Desk is mine, not yours: a demonstration of what these "
        "tools can build.",
        "Questions anytime, in class or after.",
    ),
)
