"""Content for the FIN1209 special lecture: AI CLI tools, Git and GitHub.

Plain data, read by build_special_lecture.py. Not a textbook chapter, so it
does not use deckkit.Chapter/Section (parts, dividers, checks, answer keys):
those exist for a Lim chapter and nothing here claims to teach Lim. It still
uses deckkit's Content, TitleSlide and Closing slide types and its FEU visual
identity, because the lecture is taught in the same room from the same
projector as every other FIN1209 deck.

Every command quoted here was fetched from OpenAI's own current Codex CLI
docs on 25 Nov 2026, not from memory:

  - https://learn.chatgpt.com/codex/cli (and its .md form) - install steps,
    sign-in step
  - https://releases.openai.com/codex/install.sh - what the macOS/Linux
    installer actually does to PATH, read directly rather than guessed
  - https://github.com/openai/codex - README, cross-checked

See the speaker notes on the two install slides and the error slide for the
exact citation on each claim.
"""

from __future__ import annotations

import deckkit

TITLE = deckkit.TitleSlide(
    course="FIN1209 - Technical Analysis in Investment, FEU Manila",
    chapter="Special lecture",
    title="AI Tools, Git and GitHub for Your Final Project",
    subtitle=("Setting up Codex, Git and GitHub so your group can build "
              "Quiz 6 together"),
    presenter=("Benjamin C. Sotelo, with Tyrone Miguel Arriolado helping set "
               "up your computers today"),
    notes=(
        "This is a one-off special lecture, not a Lim chapter: everything "
        "about Codex, Git and GitHub is general tool knowledge, never "
        "presented as the textbook's.",
        "Quiz 6 is the group final project: three groups, each with a "
        "leader and a co-leader.",
    ),
)

CONTENT = [
    deckkit.Content(
        title="What is an AI CLI tool?",
        lines=(
            "A command-line program that uses an AI model to write code, "
            "run commands and manage files for you.",
            "You type what you want in plain English; it does the typing "
            "of the actual commands.",
            "We will use Codex, OpenAI's own CLI tool, for this class.",
        ),
        accent="You do not need to already know how to code to use it.",
        notes=(
            "\"AI CLI tool\" is not a Lim term; it is general software "
            "knowledge for this lecture only.",
            "CLI = command line interface: the terminal window, not a "
            "website or an app icon.",
        ),
    ),
    deckkit.Content(
        title="Install Codex: macOS",
        lines=(
            "Open Terminal: press Cmd+Space, type Terminal, press Enter.",
            "Paste the command below, press Enter, and wait for it to "
            "finish.",
        ),
        accent="curl -fsSL https://chatgpt.com/codex/install.sh | sh",
        caption=("Source: OpenAI Codex CLI docs, learn.chatgpt.com/codex/"
                 "cli, fetched 25 Nov 2026."),
        notes=(
            "Exact command quoted verbatim from learn.chatgpt.com/codex/cli "
            "(macOS/Linux tab), fetched 25 Nov 2026.",
            "No prerequisite install (no Node.js, no Homebrew) is required "
            "for this standalone installer; the docs state none.",
            "An npm alternative exists (npm install -g @openai/codex) for "
            "anyone who already has Node.js, and a Homebrew cask (brew "
            "install --cask codex); neither is the default path here.",
        ),
    ),
    deckkit.Content(
        title="Install Codex: Windows",
        lines=(
            "Open PowerShell: press the Start key, type PowerShell, press "
            "Enter.",
            "Paste the command below into the new PowerShell window and "
            "press Enter.",
        ),
        accent=('powershell -ExecutionPolicy ByPass -c "irm '
                'https://chatgpt.com/codex/install.ps1 | iex"'),
        caption=("No WSL needed; this installs Codex directly on Windows. "
                 "Same source, fetched 25 Nov 2026."),
        notes=(
            "Exact command quoted verbatim from learn.chatgpt.com/codex/"
            "cli.md (Windows section), fetched 25 Nov 2026.",
            "The docs offer WSL (Windows Subsystem for Linux) only as an "
            "option for Linux-native tooling, never as a requirement; a "
            "native Windows install exists and this is it.",
        ),
    ),
    deckkit.Content(
        title="Sign in to Codex",
        lines=(
            "In the same terminal, type: codex",
            "The first time, Codex asks you to sign in.",
            'Choose "Sign in with ChatGPT" and finish in your browser.',
        ),
        accent=("You need a ChatGPT account to sign in; it is free to "
                "create one."),
        notes=(
            'learn.chatgpt.com/codex/cli, fetched 25 Nov 2026: "Open a '
            "project directory and run codex. The first time you run "
            'Codex, choose Sign in with ChatGPT or another available '
            'sign-in method."',
            "An API key is the other option the docs name; ChatGPT sign-in "
            "is simpler for this class and needs no separate key.",
        ),
    ),
]

# The one dedicated slide the captain asked for by name: the error he expects
# on a fresh Mac, right after install, with its exact fix. Rendered as a Shot
# (a terminal-mockup illustration), not a Content slide, so the room sees the
# actual wording of the error rather than a paraphrase.
ERROR_SHOT = dict(
    title="The error you will probably see",
    label="ILLUSTRATION",
    shows=("A typical first terminal session right after installing Codex "
           "on a fresh Mac."),
    lines=(
        "~ % codex",
        "zsh: command not found: codex",
        "",
        '~ % export PATH="$HOME/.local/bin:$PATH" && codex',
        "Codex CLI - signed in as you",
        "› ",
    ),
    credit=("Illustration, not a real recording. Fix: open a brand new "
            "terminal window or tab, or run the export line above once, "
            "exactly as the installer prints it."),
    notes=(
        "Why this happens: the installer adds Codex to your PATH by "
        "editing ~/.zprofile (read verbatim from "
        "releases.openai.com/codex/install.sh, fetched 25 Nov 2026), but a "
        "terminal window already open does not re-read that file.",
        "The installer's own end-of-run message says exactly this: "
        '"Current terminal: export PATH=... && codex" / "Future '
        'terminals: open a new terminal and run: codex."',
    ),
)

MORE_CONTENT = [
    deckkit.Content(
        title="From here, you just type prompts",
        lines=(
            "Codex is installed and signed in. The rest happens inside "
            "Codex.",
            "You do not need to memorize commands: you describe what you "
            "want, in plain English, as a prompt.",
            "Codex writes and runs the actual Git and GitHub commands for "
            "you.",
        ),
        accent=("Type a prompt, read what Codex plans to do, then approve "
                "it."),
    ),
    deckkit.Content(
        title="Prompt: install Git",
        lines=("Type this into Codex:",),
        accent=('"Check whether Git is installed on this computer. If it '
                'is not, install it, then tell me how to confirm it '
                'worked."'),
        caption=("Git is the tool that tracks every change to your "
                 "project's files."),
    ),
    deckkit.Content(
        title="Prompt: create and sign in to GitHub",
        lines=(
            "Creating the account itself happens in your browser, not "
            "inside Codex.",
            "Go to github.com, sign up, then come back to the terminal "
            "and type:",
        ),
        accent=('"I just created a GitHub account. Help me sign in to '
                'GitHub from this terminal."'),
    ),
    deckkit.Content(
        title="Prompt: set your name and email",
        lines=(
            "Every commit you make is labeled with a name and an email.",
            "Type this into Codex:",
        ),
        accent=('"Set up my Git identity with my name and my email, so my '
                'commits are labeled correctly."'),
    ),
    deckkit.Content(
        title="Prompt: create your group's repository",
        lines=(
            "Only the leader does this step, once per group.",
            "Type this into Codex:",
        ),
        accent=('"Create a new private GitHub repository for our group\'s '
                'Quiz 6 project, and invite my teammates\' GitHub usernames '
                'as collaborators."'),
        caption=("Everyone else waits for the leader's invite, then "
                 "accepts it on github.com."),
    ),
    deckkit.Content(
        title="Prompt: clone, branch, commit, push",
        lines=("Once you have accepted the invite, type this into Codex:",),
        accent=('"Clone our group\'s repository to this computer, create a '
                'new branch for my part of the work, and show me how to '
                'commit and push my changes."'),
        caption=("A branch is your own copy of the project to work in "
                 "without disturbing anyone else's."),
    ),
    deckkit.Content(
        title="Prompt: pull request, review, merge",
        lines=("When your part is ready, type this into Codex:",),
        accent=('"Open a pull request for my branch, and once a teammate '
                'approves it, help me merge it into the main branch."'),
        caption=("A pull request is a request to add your branch's changes "
                 "into the group's shared project."),
    ),
    deckkit.Content(
        title="How your group collaborates on Quiz 6",
        lines=(
            "The leader creates the repository and invites the co-leader "
            "and members.",
            "Everyone works on their own branch, never directly on the "
            "main branch.",
            "Finish a piece of work, then open a pull request instead of "
            "pushing straight in.",
            "Pull before you push, every time, so you never overwrite a "
            "teammate's work.",
        ),
        accent=("Never edit the same file as a teammate without pulling "
                "first."),
    ),
    deckkit.Content(
        title="What we built: Stock Desk",
        lines=(
            "A live stock tool built the same way: an AI CLI tool, Git and "
            "GitHub, start to finish.",
            "It tracks five stocks plus the S&P 500, with live prices and "
            "Chapter 8's buy and sell signals.",
            "It is mine, not yours: a demonstration of what these tools "
            "can build, not a class assignment.",
        ),
        accent=("This is the same workflow you just learned, used on a "
                "real project."),
    ),
]

# The two screenshots, described in order. See build_special_lecture.py for
# the source files and the firstmate home evidence folder they are pulled
# from.
STOCK_DESK_SHOTS = [
    dict(
        title="Stock Desk: live prices and signals",
        label="SCREENSHOT",
        shows=("The main Stock Desk screen: live prices, Chapter 8's "
               "signal panel, fundamentals and a session replay."),
        source_file="deployed-final-ipad.png",
        credit=("Stock Desk, the captain's own tool, signed in "
                "with his own passphrase. Live Yahoo prices, Chapter 8's "
                "five-day-high / RSI / MACD signal rule, fundamentals from "
                "each company's own SEC filing, and a session replay."),
        notes=(
            "How he uses it, for his own reference (not shown to the "
            "class): sign in with his passphrase, pick a stock from the "
            "watchlist, read the signal panel (trend, signal, trigger, "
            "volume), then log a buy only if he decides to act on it.",
            "Students never get the passphrase or access; this is a "
            "demonstration, never a class assignment.",
        ),
    ),
    dict(
        title="Stock Desk: logging a position",
        label="SCREENSHOT",
        shows=("The position card after logging a buy: bought price, "
               "target, stop, and the running gain or loss."),
        source_file="deployed-position-card.png",
        credit=("Stock Desk, the captain's own tool. Logging a "
                "buy records the price, the stop and the target; the tool "
                "never places a trade, it only tracks one he decides to "
                "log himself."),
    ),
]

CLOSING = deckkit.Closing(
    title="Thank you",
    lines=(
        "Thank you to Tyrone Miguel Arriolado, who is helping set up Git, "
        "GitHub and Codex on your computers today.",
        "Install Codex, sign in, then keep this deck open: every prompt "
        "you need is on these slides.",
        "Questions anytime, in class or after.",
    ),
)
