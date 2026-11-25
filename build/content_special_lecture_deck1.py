"""Deck 1: set up Codex, Git and GitHub for the first time.

Plain data, read by build_special_lecture_deck1.py. One of three decks for
this special lecture (2 is the Stock Desk guide, 3 is building a simple
tool with structured prompts); see build_special_lecture_deck1.py's module
docstring for how the three fit together. Not a textbook chapter, so this
does not use deckkit.Chapter/Section (parts, dividers, checks, answer
keys): none of that exists here because nothing here claims to teach Lim.
It reuses deckkit's Content/TitleSlide/Closing slide types but a neutral
visual identity, not FEU's green and gold (special_lecture_kit.
apply_neutral_palette(), called by the build script before anything
renders).

Fresh-Mac-mini assumption throughout: the captain is doing this live from
a brand-new Mac mini tonight, so every Mac-specific slide (the install, the
PATH error, the Command Line Tools prompt) teaches what a FRESH machine
actually shows, not what this already-set-up build machine shows; where
the two differ, both are named and which is which is explicit.

This deck is a real, hands-on walkthrough, one action per slide, built
around a single evolving example: "group-stock-notes", a shared README.md
each teammate adds one line to. Two kinds of evidence back it:

  * SCREENSHOT - genuinely run on this machine today, in a throwaway local
    folder (codex --version, git --version, git init/branch/add/commit/
    log/diff/pull, two real `codex exec` prompts). Nothing new was
    installed; nothing was pushed to GitHub, signed in or out of, or
    shared with anyone. Where the real workflow needs a GitHub remote, a
    local bare repository stands in for it, disclosed in that slide's
    notes. A `--global` git-identity example used GIT_CONFIG_GLOBAL to
    point at a throwaway file instead of this Mac's real ~/.gitconfig,
    also disclosed.
  * ILLUSTRATION - a step no local command can show (the installer's own
    run, GitHub sign-up, accepting an invite, anything on Windows): either
    a plain mockup built from GitHub's and OpenAI's own current
    documentation, or (for the three pull-request pages) a real GitHub
    Docs screenshot (CC BY 4.0, credited; see build/assets/github-docs-
    screenshots/SOURCE.md). Never presented as a live capture of this
    build's own session.

Every command and every citation was fetched or run today (25 Nov 2026),
not from memory. See each slide's speaker notes for its exact source.
"""

from __future__ import annotations

import deckkit

# Kept in one place, as asked, so a name correction is a one-line change.
# His own verbatim confirmation, 25 Nov ~04:35: "Its Arrollado" (not the
# team's earlier records, "Arriolado").
TYRONE_SURNAME = "Arrollado"

SPEAKERS = (
    ("Benjamin C. Sotelo", "Lecturer, FIN1209"),
    (f"Tyrone Miguel {TYRONE_SURNAME}", "Lecturer, FIN1209"),
)

TITLE = deckkit.TitleSlide(
    course="FIN1209 - Technical Analysis in Investment",
    chapter="Special lecture 1 of 3",
    title="Set Up Codex, Git and GitHub",
    subtitle=("A step-by-step walkthrough: one worked example the whole "
              "way, from a fresh Mac mini"),
    presenter=f"Benjamin C. Sotelo and Tyrone Miguel {TYRONE_SURNAME}",
    notes=(
        "This is a one-off special lecture, not a Lim chapter: everything "
        "about Codex, Git and GitHub is general tool knowledge, never "
        "presented as the textbook's.",
        "Neutral visual style on purpose, not FEU's green/gold: his own "
        "words, 25 Nov, \"it shouldn't be an FEU theme.\"",
        "Quiz 6 is the group final project: three groups, each with a "
        "leader and a co-leader.",
        "The worked example, group-stock-notes, is invented for this "
        "lecture; it is not a real group's repository.",
        "Two lecturers today, both presenting (not one \"helping set "
        "up\"): who presents which deck is still being decided; this "
        "deck does not assume an answer.",
    ),
)

AI_CLI_INTRO = deckkit.Content(
    title="What is an AI CLI tool?",
    lines=(
        "A command-line program that uses an AI model to write code, "
        "run commands and manage files for you.",
        "You type what you want in plain English; it does the typing "
        "of the actual commands.",
        "We will use Codex, OpenAI's own CLI tool, for this class.",
    ),
    accent="You do not need to already know how to code to use it.",
    origin="Both presenters",
    notes=(
        "\"AI CLI tool\" is not a Lim term; it is general software "
        "knowledge for this lecture only.",
        "CLI = command line interface: the terminal window, not a "
        "website or an app icon.",
        "Only the CLI is installed by hand (next two slides). Everything "
        "else in this deck, including Git itself, is a prompt to Codex.",
    ),
)

MAC_INSTALL_DO = ("Open Terminal: press Cmd+Space, type Terminal, press "
                 "Enter.",
                 "Paste the command below, press Enter, and wait for it "
                 "to finish.")
MAC_INSTALL_ACCENT = "curl -fsSL https://chatgpt.com/codex/install.sh | sh"

MAC_INSTALL_STEP = dict(
    title="Install Codex: macOS",
    kind="terminal",
    do_lines=MAC_INSTALL_DO,
    do_accent=MAC_INSTALL_ACCENT,
    term_lines=(
        "$ curl -fsSL https://chatgpt.com/codex/install.sh | sh",
        "Codex CLI 0.164.0 installed successfully.",
        "Current terminal: export PATH=... && codex",
    ),
    fallback=("Nothing printed for a long time? Check your internet "
              "connection; the download is small but needs one."),
    source_credit=None,
    presenter="Benjamin C. Sotelo",
    credit="verified today against the installer's own script text.",
    notes=(
        "Not re-run live: this build already has Codex installed "
        "(codex-cli 0.164.0, confirmed on the next slide), so this "
        "picture is the installer's own real end-of-run messages, read "
        "verbatim from releases.openai.com/codex/install.sh (fetched 25 "
        "Nov 2026), not a fresh capture: \"Codex CLI %s installed "
        'successfully.\" and \"Current terminal: $path_line && codex.\"',
        "Exact command quoted verbatim from both learn.chatgpt.com/"
        "codex/cli (macOS/Linux tab) and the openai/codex GitHub "
        "README, each fetched 25 Nov 2026 and showing the identical "
        "command.",
        "No prerequisite install (no Node.js, no Homebrew) is required "
        "for this standalone installer; the docs state none.",
        "An npm alternative exists (npm install -g @openai/codex) for "
        "anyone who already has Node.js, and a Homebrew cask (brew "
        "install --cask codex); neither is the default path here.",
    ),
)

MAC_ERROR_SHOT = dict(
    title="The error you will probably see: Mac",
    label="SCREENSHOT",
    term_lines=("~ % codex", "zsh: command not found: codex"),
    lines=(
        "Normal: PATH is not active in this terminal window yet.",
        "New terminal still fails? Run once: echo 'export PATH=\"$HOME/"
        ".local/bin:$PATH\"' >> ~/.zprofile",
    ),
    accent='Fix: export PATH="$HOME/.local/bin:$PATH" && codex',
    rare=('Rare: "no such file or directory" instead of "command not '
          'found" means the install did not finish; rerun the install '
          "command."),
    presenter="Benjamin C. Sotelo",
    credit="verified today on this Mac.",
    notes=(
        "Verified for real today: `zsh -c 'unset -v PATH; export "
        'PATH="/usr/bin:/bin"; codex\'` genuinely prints "command not '
        'found: codex" (exit 127) when PATH does not yet include '
        "~/.local/bin, the same condition a fresh install leaves a "
        "terminal in. The exact line shown here drops the \"1:\" index "
        "zsh adds only when a command runs via -c; typed directly at an "
        "interactive prompt it reads exactly as shown.",
        "The installer adds Codex to your PATH by editing ~/.zprofile "
        "(read verbatim from releases.openai.com/codex/install.sh, "
        "fetched 25 Nov 2026, its pick_profile function on darwin with "
        "zsh), but a terminal window already open does not re-read that "
        'file. The installer\'s own end-of-run message says exactly '
        'this: "Current terminal: export PATH=... && codex" / "Future '
        'terminals: open a new terminal and run: codex."',
        "The rare wording: \"command not found\" means codex is not yet "
        'on PATH (the normal case above); "no such file or directory" '
        "would mean the symlink in ~/.local/bin points at nothing, which "
        "only happens if the install itself did not finish; install.sh "
        "never prints that wording itself, so it is this general shell "
        "behaviour on a broken link, not a message the script prints.",
    ),
)

WIN_INSTALL_STEP = dict(
    title="Install Codex: Windows",
    kind="terminal",
    do_lines=(
        "Open PowerShell: press the Start key, type PowerShell, press "
        "Enter.",
        "Paste the command below into the new PowerShell window and "
        "press Enter.",
    ),
    do_accent=('powershell -ExecutionPolicy ByPass -c "irm '
               'https://chatgpt.com/codex/install.ps1 | iex"'),
    term_lines=(
        "PS> powershell -ExecutionPolicy ByPass -c \"irm ... | iex\"",
        "Codex CLI installed successfully.",
        "Future PowerShell windows: open a new window and run: codex",
    ),
    fallback=(f"Fails outright? Tyrone will set up WSL2 with you; the "
              "project's own docs list that as a supported path too."),
    presenter=f"Tyrone Miguel {TYRONE_SURNAME}",
    credit="verified today against the installer's own script text; no Windows machine here.",
    notes=(
        "Exact command quoted verbatim from github.com/openai/codex's "
        "README, fetched 25 Nov 2026 (a native Windows install, no "
        "WSL): this is the one we lead with.",
        "openai/codex's own docs/install.md, fetched 25 Nov 2026, lists "
        '"Windows 11 via WSL2" in its system requirements table: the '
        "project's own docs are not fully consistent on whether WSL is "
        "required, which is exactly why the fallback here is Tyrone "
        "setting up WSL2 by hand if the native installer fails.",
        "The two printed lines are install.ps1's own real end-of-run "
        "messages, read verbatim from releases.openai.com/codex/"
        "install.ps1 (fetched 25 Nov 2026), not a live capture: no "
        "Windows machine is available to this build.",
    ),
)

WIN_ERROR_SHOT = dict(
    title="The error you will probably see: Windows",
    label="ILLUSTRATION",
    term_lines=("PS> codex", "codex : term 'codex' is not recognized"),
    lines=(
        "The installer only updated new PowerShell windows, not this "
        "one.",
    ),
    accent="Fix: close this PowerShell window, open a brand-new one, then run: codex",
    presenter=f"Tyrone Miguel {TYRONE_SURNAME}",
    credit="not a live capture; no Windows machine here.",
    notes=(
        "install.ps1 (releases.openai.com/codex/install.ps1, fetched 25 "
        'Nov 2026) does update PATH, but the usual install command runs '
        'it as a child process via "-c", so the window the student is '
        "actually looking at never has its PATH refreshed; its own closing "
        "message only promises the NEXT PowerShell window, never the "
        'current one: "Future PowerShell windows: open a new PowerShell '
        'window and run: codex."',
    ),
)

SIGNIN_STEP = dict(
    title="Sign in to Codex",
    kind="doc",
    do_lines=(
        "In the same terminal, type: codex",
        "The first time, Codex asks you to sign in.",
    ),
    do_accent='Choose "Sign in with ChatGPT" and finish in your browser.',
    doc_site="chatgpt.com/codex/auth",
    doc_lines=(
        'learn.chatgpt.com/codex/cli: "the first time you run Codex, '
        'choose Sign in with ChatGPT or another available sign-in '
        'method."',
        "Codex is included across ChatGPT plans, including Free and "
        "Go; usage limits vary by plan.",
    ),
    fallback=("Browser did not open by itself? Codex prints a link; "
              "copy it into any browser yourself."),
    source_credit=None,
    presenter="both",
    credit="OpenAI's own docs, fetched today; not re-run live.",
    notes=(
        'learn.chatgpt.com/codex/cli, fetched 25 Nov 2026: "Open a '
        "project directory and run codex. The first time you run "
        'Codex, choose Sign in with ChatGPT or another available '
        'sign-in method."',
        "An API key is the other option the docs name; ChatGPT sign-in "
        "is simpler for this class and needs no separate key.",
        "help.openai.com/en/articles/11369540-codex-in-chatgpt, fetched "
        '25 Nov 2026, verbatim: "Codex is included across ChatGPT '
        'plans, including Free and Go. Usage limits vary by plan." Its '
        "Availability section adds one caveat: Codex Cloud specifically "
        '(a separate, hosted feature, not the CLI we are using today) '
        '"is not included with Free or Go." The CLI itself is on '
        "every plan.",
        "Not re-run live: this machine's Codex is already signed in and "
        "must stay that way (no sign-in or sign-out performed for this "
        "build), so the picture is a mockup of the described flow, not "
        "a captured browser screen.",
    ),
)

TRANSITION = deckkit.Content(
    title="From here, you just type prompts",
    lines=(
        "Codex is installed and signed in. That is the only thing "
        "installed by hand.",
        "Everything else, starting with Git itself, is a prompt you "
        "type, in plain English.",
        "Codex writes and runs the actual Git and GitHub commands for "
        "you.",
    ),
    accent=("Type a prompt, read what Codex plans to do, then approve "
            "it."),
    origin="Both presenters",
)

GIT_GITHUB_SHOT = dict(
    title="What are Git and GitHub?",
    label="ILLUSTRATION",
    presenter="both",
    credit=("Git keeps the history of every change to your project's files "
            "on your own computer; GitHub stores that history online so a "
            "group can share it, review it and merge it."),
)

WALKTHROUGH_INTRO = deckkit.Content(
    title="Our worked example: group-stock-notes",
    lines=(
        "Every slide from here uses one example: group-stock-notes, a "
        "shared README.md.",
        "Each teammate adds one line about a stock they are watching.",
        "Three people play a part: you lead; Alex and Jun are your "
        "teammates.",
    ),
    accent="One new thing happens per slide.",
    origin="Both presenters",
)

# --------------------------------------------------------------------------
# The walkthrough: one action per slide. "kind" is "terminal" (a real
# command captured on this machine today, or a mockup watermarked
# ILLUSTRATION when it is not), "doc" (a plain browser mockup), "dialog"
# (a macOS system-alert mockup) or "image" (a real third-party screenshot,
# a file under build/assets/github-docs-screenshots/). See
# build_special_lecture_deck1.py for exactly how each image is drawn.
# --------------------------------------------------------------------------

WALKTHROUGH = [
    dict(
        title="Prompt: check python3 works",
        kind="dialog",
        do_lines=(
            "Type this into Codex, before anything else today:",
        ),
        do_accent=('"Check whether python3 works on this computer. If '
                    'macOS asks to install the command line developer '
                    'tools, install them."'),
        dialog_title="Command Line Tools",
        dialog_message=('The "python3" command requires the command line '
                        "developer tools. Would you like to install the "
                        "tools now?"),
        dialog_buttons=("Not Now", "Install"),
        fallback=("the very first time anyone runs python3 (or git, next) "
                  "on a truly fresh Mac, macOS offers this same install, "
                  "which takes a few minutes and needs a mouse click; "
                  "Codex cannot click through it by itself. Doing this "
                  "once, before the lecture starts, means Codex is not "
                  "blocked waiting on it mid-class, including for deck 3's "
                  "tool, which needs python3 working."),
        credit="Apple's documented Command Line Tools prompt.",
        notes=(
            "Added per the captain's own fix: deck 3 already says python3 "
            "must work before class; this is that same step, in deck 1, "
            "next to the Git check it shares one dialog with.",
            "Real behaviour on a fresh Mac: this dialog, not an instant "
            "answer; this build machine already has the tools installed, "
            "so python3 --version here returns instantly.",
        ),
    ),
    dict(
        title="Prompt: check Git is installed",
        kind="dialog",
        do_lines=(
            "Type this into Codex:",
        ),
        do_accent=('"Check whether Git is installed on this computer. If '
                    'it is not, install it, then tell me how to confirm '
                    'it worked."'),
        dialog_title="Command Line Tools",
        dialog_message=('The "git" command requires the command line '
                        "developer tools. Would you like to install the "
                        "tools now?"),
        dialog_buttons=("Not Now", "Install"),
        fallback=("On a fresh Mac, expect this instead of an instant "
                  "answer: click Install and wait, often several "
                  "minutes, before Git exists at all. Once it finishes, "
                  "the same prompt gets a real answer: git version 2.50.1 "
                  "(Apple Git-155), as on this already-set-up Mac."),
        credit="Apple's documented Command Line Tools prompt.",
        notes=(
            "On a genuinely fresh Mac mini (what the captain is using "
            "tonight) this is what actually happens first, not the "
            "quick version-check this build's own real screenshot could "
            "show: this build machine already has the command line "
            "developer tools, so typing git here finished instantly. "
            "The fallback line (really the main point of this slide for "
            "him) is the dialog and the wait, not the quick answer.",
            'Dialog wording: \'The "git" command requires the command '
            "line developer tools. Would you like to install the tools "
            'now?\' with Install and Not Now, is the widely documented '
            "Xcode Command Line Tools first-run prompt (macOS triggers "
            "it from `git`, `make`, `clang` and other developer tools "
            "before Xcode or the standalone tools are present). Checked "
            "today against developer.apple.com's own Command Line Tools "
            "pages and Apple's archived Technical Note TN2339; neither "
            "quotes this exact sentence verbatim, so treat the wording "
            "as widely corroborated rather than an exact Apple citation, "
            "and verify it against the real fresh Mac mini tonight if a "
            "precise quote matters.",
            "Genuinely run today, for the real success case once the "
            "tools exist: `codex exec -s workspace-write -C "
            '<scratch-folder> "Check whether git is installed on this '
            'computer. If it is not, install it, then tell me how to '
            'confirm it worked."`, in a throwaway folder, nothing new '
            "installed (git was already present). Session id "
            "01a20f07-3f87-70b1-bf19-463204ef4d4a. Codex's real reply: "
            '"I\'ll check whether Git is available and print its '
            'version... Git is installed: git version 2.50.1 (Apple '
            'Git-155)."',
            "Tyrone's setup note: warn each student before they type "
            "anything that a fresh Mac will likely show this install "
            "prompt on the very first git-related step (this one, not "
            "the Codex install itself, which does not touch git); have "
            "them click Install and wait rather than assume something "
            "is broken. Expect this on the captain's own fresh Mac mini "
            "tonight too.",
        ),
    ),
    dict(
        title="Prompt: create a GitHub account and sign in",
        kind="doc",
        do_lines=(
            "Creating the account itself happens in your browser, not "
            "inside Codex.",
            "Go to github.com, sign up, then come back to the terminal "
            "and type:",
        ),
        do_accent=('"I just created a GitHub account. Help me sign in to '
                    'GitHub from this terminal."'),
        doc_site="github.com/signup",
        doc_lines=(
            "Enter an email, a password and a username; verify the "
            "email GitHub sends you.",
            "You do not have GitHub's own CLI yet; Codex offers to "
            "install it (gh) first. Approve it.",
            "Codex then runs gh auth login, which opens a browser tab "
            "to finish signing in.",
        ),
        fallback=('If signup is refused ("This email can\'t be used" or '
                  '"We couldn\'t create your account"), the docs say to '
                  "try another browser or network."),
        credit="GitHub's own docs, fetched today, not a live capture.",
        notes=(
            "docs.github.com/en/get-started/start-your-journey/"
            "creating-an-account-on-github, fetched 25 Nov 2026: create "
            "the account at github.com/signup (Google and Apple sign-in "
            "also offered), verify the email address, and the page "
            'warns about two exact errors, "This email can\'t be used" '
            'and "We couldn\'t create your account," with the fixes '
            "quoted in the fallback line.",
            "GitHub CLI install, fetched 25 Nov 2026 from github.com/"
            "cli/cli's own docs (install_macos.md / install_windows.md): "
            'macOS, Homebrew, "brew install gh"; Windows, WinGet, '
            '"winget install --id GitHub.cli --source winget" (that '
            "page also warns the installer changes PATH, so Windows "
            "Terminal users must open a brand-new window, not a new "
            "tab, the same PATH lesson as the Codex install itself).",
            "gh auth login, cli.github.com/manual/gh_auth_login, fetched "
            '25 Nov 2026, verbatim: "The default authentication mode is '
            'a web-based browser flow," and it stores the resulting '
            'token "securely in the system credential store." The exact '
            "interactive prompt wording was not confirmed against the "
            "docs, so none of it is quoted on the slide.",
            "A live capture of github.com/signup was attempted and "
            "abandoned: the real page served a bot-detection challenge "
            "(DataDome), which this build never attempts to pass. No "
            "account was created, no gh was installed, and no sign-in "
            "was performed, per the brief's own limits.",
        ),
    ),
    dict(
        title="Prompt: set your name and email",
        kind="terminal",
        do_lines=(
            "Every commit you make is labeled with a name and an "
            "email, for every project on this computer. Type this into "
            "Codex:",
        ),
        do_accent=('"Set up my Git identity for this computer with my '
                    'name and my email, so my commits are labeled '
                    'correctly."'),
        term_lines=(
            "$ git config --global user.name 'Alex Dela Cruz'",
            "$ git config --global user.email 'alex...@example.edu'",
            "$ git config --global --get-regexp 'user.(name|email)'",
            "user.name Alex Dela Cruz",
            "user.email alex.delacruz@example.edu",
        ),
        fallback=("If Codex says it is blocked, approve it, or run the "
                  "two lines it prints yourself."),
        credit="real git output, from this machine, today.",
        notes=(
            "Genuinely run today, with a safeguard: `GIT_CONFIG_GLOBAL="
            "<scratch-file> git config --global user.name 'Alex Dela "
            "Cruz'`, same for user.email, then `git config --global "
            "--get-regexp 'user.(name|email)'`, which printed exactly "
            "the two lines shown. GIT_CONFIG_GLOBAL tells git to treat "
            "a throwaway file as \"the\" global config for this one "
            "command only, so the real --global flag and the real git "
            "code path ran, genuinely, without touching this Mac's own "
            "~/.gitconfig (confirmed unchanged before and after). A "
            "student typing the prompt as written has no such "
            "safeguard and should not need one: on their own machine, "
            "--global is exactly the right scope, since no repository "
            "exists yet at this point in the walkthrough.",
            "The fallback line is also real, not invented: in this same "
            "exact folder, earlier testing with --local (since corrected "
            "to --global, the right scope here) hit a sandboxed `codex "
            "exec` call that could not write the config file and printed "
            "the same two config commands as its own suggested fix, "
            "which then worked when run directly. That sandbox refusal "
            "is a quirk of this captain's own Codex setup, not something "
            "most students will hit, so it is the fallback line here "
            "rather than the main picture.",
        ),
    ),
    dict(
        title="Leader prompt: create the group repository",
        kind="terminal",
        label="ILLUSTRATION",
        do_lines=(
            "Only the leader does this step, once per group.",
            "Type this into Codex:",
        ),
        do_accent=('"Create a new private GitHub repository called '
                    'group-stock-notes for our final project, with a '
                    'starting README."'),
        term_lines=(
            "$ gh repo create group-stock-notes --private --add-readme",
            "Created repository yourname/group-stock-notes",
        ),
        fallback=('No gh? On github.com: top right "+" icon, then "New '
                  'repository," name it, choose Private, check "Add a '
                  'README file," click "Create repository."'),
        credit="GitHub CLI's own docs, fetched today, not a live run.",
        notes=(
            "cli.github.com/manual/gh_repo_create, fetched 25 Nov 2026: "
            'synopsis "gh repo create [<name>] [flags]"; a non-private '
            "remote needs one of --public/--private/--internal, e.g. the "
            'page\'s own example "gh repo create my-project --public '
            '--clone"; the page also lists `--add-readme` ("Add a README '
            'file to the new repository") as a real flag. The exact '
            "success-message wording on the second line was not "
            "confirmed against a real run (no repository was created "
            "for this build, per the brief's own limits), so it is a "
            "reasonable paraphrase, not a verbatim quote.",
            "--add-readme is the fix for a gap the walkthrough had "
            "without it: the example's README.md (\"Our FIN1209 final "
            "project notes.\") needs to exist before anyone can add a "
            "line to it, and this is the one step that creates it.",
            "The fallback (browser) path is docs.github.com/en/"
            "repositories/creating-and-managing-repositories/creating-a-"
            'new-repository, fetched 25 Nov 2026: the "+" icon in the '
            'upper right (aria-label "Create something new"), then New '
            "repository; fields are an Owner dropdown, the repository "
            "name (letters, digits, `.`, `-`, `_` only), an optional "
            "description, a Public/Private choice and an \"Add a README "
            'file" checkbox, finished with Create repository.',
        ),
    ),
    dict(
        title="Leader prompt: invite your teammates",
        kind="terminal",
        label="ILLUSTRATION",
        do_lines=(
            "Still the leader, still once per group.",
            "You need each teammate's actual GitHub username (ask them "
            "to sign up first). Type this into Codex:",
        ),
        do_accent=('"Invite alexdelacruz and jun-santos to '
                    'group-stock-notes as collaborators."'),
        term_lines=(
            "$ gh api --method PUT repos/yourname/group-stock-notes/",
            "    collaborators/alexdelacruz",
            "$ gh api --method PUT repos/yourname/group-stock-notes/",
            "    collaborators/jun-santos",
        ),
        fallback=('No gh? On github.com: repository Settings, then '
                  '"Collaborators" in the Access section, "Add people," '
                  "search their username, then confirm."),
        credit="GitHub's own REST API docs, fetched today, not a live run.",
        notes=(
            "gh has no dedicated invite/collaborator command (checked "
            "the full command index at cli.github.com/manual/, fetched "
            "25 Nov 2026: gh repo's own subcommands are archive, "
            "autolink, clone, create, delete, deploy-key, edit, fork, "
            "gitignore, license, list, read-dir, read-file, rename, "
            "set-default, sync, unarchive, view, none of them this). The "
            "real mechanism is the REST API, docs.github.com/en/rest/"
            "collaborators/collaborators, fetched 25 Nov 2026, verbatim: "
            '"PUT /repos/{owner}/{repo}/collaborators/{username}"; `gh '
            "api` is the documented way to call any REST endpoint from "
            "the CLI, so Codex reaches for it here rather than a plain "
            "gh subcommand.",
            "alexdelacruz and jun-santos are invented GitHub usernames "
            "standing in for Alex's and Jun's real ones; a real prompt "
            "needs the real usernames, which is why the prompt text "
            "itself now says so rather than leaving it implicit.",
            "docs.github.com's own page also states a rate limit (50 "
            "invitations per repository per 24 hours) and that the "
            'invitee "must accept or decline."',
            "The fallback (browser) path is docs.github.com/en/account-"
            "and-profile/.../inviting-collaborators-to-a-personal-"
            'repository, fetched 25 Nov 2026: Settings (gear icon, or '
            '"more" kebab menu), Collaborators under Access, Add people, '
            'search the username, then "Add NAME to REPOSITORY."',
            "No one was invited for this build, per the brief's own "
            "limits.",
        ),
    ),
    dict(
        title="Member: accept the invite",
        kind="doc",
        do_lines=(
            "Alex and Jun each do this once, for their own invite.",
            "No Codex prompt needed; this happens in your inbox and "
            "browser.",
        ),
        do_accent="Open the email from GitHub and accept the invitation.",
        doc_site="(your email inbox)",
        doc_lines=(
            "GitHub emails every invitee a link to the invitation.",
            "Accepting it grants collaborator access to the "
            "repository.",
        ),
        fallback=("No email after a few minutes? Check spam, or ask the "
                  "leader to resend the invite from Settings."),
        credit="GitHub's own docs, fetched today, not a live capture.",
        notes=(
            "docs.github.com/en/repositories/managing-your-repositorys-"
            "settings-and-features/repository-access-and-collaboration/"
            'inviting-collaborators-to-a-personal-repository, fetched 25 '
            'Nov 2026, verbatim: "The user will receive an email inviting '
            "them to the repository. Once they accept your invitation, "
            'they will have collaborator access to your repository." The '
            "exact accept button/page was not found in GitHub's current "
            "docs today, and no GitHub Docs screenshot of it exists "
            "either (checked 25 Nov 2026), so this slide states only "
            "what is confirmed: an email invitation that must be "
            "accepted, nothing more specific.",
        ),
    ),
    dict(
        title="Prompt: clone the repository",
        kind="terminal",
        do_lines=("Once you have accepted the invite, type this into "
                  "Codex:",),
        do_accent='"Clone our group\'s repository to this computer."',
        term_lines=(
            "$ git clone <your-repo-URL> group-stock-notes",
            "Cloning into 'group-stock-notes'...",
            "done.",
        ),
        fallback=("\"Permission denied\" usually means the invite was not "
                  "accepted yet, or the URL was copied wrong."),
        credit="real git output; the URL stands in for your GitHub link.",
        notes=(
            "Genuinely run today: `git clone origin.git member-repo` "
            "against a local bare repository standing in for GitHub "
            '(no network reaches GitHub for this build), printed exactly '
            '"Cloning into \'member-repo\'...\\ndone." The folder name on '
            "the slide (group-stock-notes) is what a real clone of that "
            "named repository would print; the mechanism and wording are "
            "identical either way.",
        ),
    ),
    dict(
        title="Prompt: make a branch",
        kind="terminal",
        do_lines=("Type this into Codex:",),
        do_accent='"Create a new branch for my part of the work, called alex-notes."',
        term_lines=(
            "$ git checkout -b alex-notes",
            "Switched to a new branch 'alex-notes'",
        ),
        fallback=("A branch is your own copy of the project; nothing you "
                  "do on it touches main until you push and merge."),
        credit="real git output, from this machine, today.",
        notes=(
            "Genuinely run today in the local demo repo: `git checkout "
            "-b alex-notes` printed exactly \"Switched to a new branch "
            "'alex-notes'\".",
        ),
    ),
    dict(
        title="Change a file: add your line",
        kind="terminal",
        diff_mode=True,
        do_lines=(
            "Open README.md in any text editor, or ask Codex to add the "
            "line for you.",
            "Alex adds one line about the stock she is watching:",
        ),
        do_accent='"- Alex: NVDA keeps closing above its 5-day high..."',
        term_lines=(
            "$ git diff README.md",
            " Our FIN1209 final project notes.",
            "+- Alex: NVDA keeps closing above its 5-day high;",
            "+watching for a sell signal if RSI turns down.",
        ),
        fallback=("No + line? You edited the wrong file or in the wrong "
                  "folder; run git status to see what Git sees."),
        credit="real git diff output, from this machine, today.",
        notes=(
            "Genuinely run today: a real README.md edit in the local "
            "demo repo, then `git diff --no-color README.md`, which "
            "wraps the new line onto a second slide line only for "
            "width; the real one-line diff is reproduced faithfully. The "
            "diff's own `--- a/README.md` / `+++ b/README.md` header "
            "lines and two unchanged context lines are left off this "
            "picture to keep it short enough to read at full width from "
            "the back of the room; nothing shown is altered.",
            "The + line is drawn green, matching real diff output and "
            "the deck's own \"what's new\" convention for this example.",
        ),
    ),
    dict(
        title="Prompt: commit your change",
        kind="terminal",
        do_lines=("Type this into Codex:",),
        do_accent='"Commit my change with a clear message."',
        term_lines=(
            "$ git add README.md",
            "$ git commit -m 'Add my NVDA note'",
            "[alex-notes f6562f0] Add my NVDA note",
        ),
        fallback=('"nothing to commit" means git add was skipped, or the '
                  "file was not actually saved."),
        credit="real git output, from this machine, today.",
        notes=(
            "Genuinely run today in the local demo repo; the commit "
            "hash f6562f0 is the real one git printed. `git log "
            "--oneline` afterward showed f6562f0 Add my NVDA note then "
            "4dd0320 Start the group notes, confirmed but left off this "
            "picture to keep it short enough to read at full width from "
            "the back of the room.",
        ),
    ),
    dict(
        title="Prompt: push your branch",
        kind="terminal",
        do_lines=("Type this into Codex:",),
        do_accent='"Push my branch to GitHub."',
        term_lines=(
            "$ git push -u origin alex-notes",
            "To <your-repo-URL>",
            " * [new branch]      alex-notes -> alex-notes",
            "branch 'alex-notes' set up to track 'origin/alex-notes'.",
        ),
        fallback=("Asked for a username/password instead of your "
                  "browser? GitHub needs a sign-in token here; ask "
                  "Codex to help you sign in again."),
        credit="real git output; the URL stands in for your GitHub remote.",
        notes=(
            "Genuinely run today: `git push -u origin alex-notes` "
            "against the local bare stand-in printed exactly this "
            "(path replaced on the slide with <your-repo-URL> for "
            "clarity); the real run's path was a local .git folder, not "
            "GitHub, disclosed here.",
        ),
    ),
    dict(
        title="Prompt: open a pull request",
        kind="terminal",
        label="ILLUSTRATION",
        do_lines=("Type this into Codex:",),
        do_accent='"Open a pull request for my branch."',
        term_lines=(
            "$ gh pr create --title 'Add my NVDA note' \\",
            "    --body 'Adds my stock note to the shared README.'",
            "https://github.com/yourname/group-stock-notes/pull/1",
        ),
        fallback="No gh? On github.com, a yellow banner offers \"Compare & pull request\" after a push.",
        credit="GitHub CLI's own docs, fetched today, not a live run.",
        notes=(
            "cli.github.com/manual/gh_pr_create, fetched 25 Nov 2026: "
            'synopsis "gh pr create [flags]"; the page\'s own example, '
            '"gh pr create --title \\"The bug is fixed\\" --body '
            '\\"Everything works again\\""; and, verbatim, "Upon success, '
            'the URL of the created pull request will be printed," with '
            'its own worked example output "http://github.com/owner/'
            'repo/pull/1" (the docs\' own example uses http; a real '
            "GitHub link is always https, shown correctly here). --fill "
            "also exists, to use the commit message as the title/body "
            "instead of typing them.",
            "No pull request was opened for this build, per the "
            "brief's own limits.",
        ),
    ),
    dict(
        title="Review the pull request",
        kind="image",
        image_file="pr-review-changes-button.png",
        do_lines=(
            "A teammate, not the author, does this step.",
            "On the pull request page:",
        ),
        do_accent='Open "Files changed," click "Review changes."',
        fallback="Authors cannot approve their own pull request; ask a teammate.",
        source_credit="Source: GitHub Docs (CC BY 4.0)",
        credit="real GitHub Docs screenshot, CC BY 4.0, fetched today.",
        notes=(
            "docs.github.com/en/pull-requests/how-tos/review-pull-"
            "requests/reviewing-proposed-changes-in-a-pull-request, "
            'fetched 25 Nov 2026: open "Files changed," click "Review '
            'changes" above the diff, write a summary, choose Comment, '
            'Approve or "Request changes," then "Submit review." '
            '"Request changes" does not block merging unless a branch '
            "rule requires it, and the docs state authors cannot "
            "approve their own pull request.",
            "Picture: a real screenshot embedded in GitHub's own docs "
            "page above, licensed CC BY 4.0 (github.com/github/docs/"
            "blob/main/LICENSE), downloaded 25 Nov 2026, unmodified; "
            "see build/assets/github-docs-screenshots/SOURCE.md for the "
            "exact source URL. It shows a real pull request example "
            "(\"Adding sparkles #45834\"), not this deck's own group-"
            "stock-notes repository.",
        ),
    ),
    dict(
        title="Merge the pull request",
        kind="image",
        image_file="pr-merge-options.png",
        do_lines=("Once approved, on the same page:",),
        do_accent='Click "Merge pull request," then "Confirm merge."',
        fallback='Button greyed out? The review is not approved yet, or a check is still running.',
        source_credit="Source: GitHub Docs (CC BY 4.0)",
        credit="real GitHub Docs screenshot, CC BY 4.0, fetched today.",
        notes=(
            "docs.github.com/en/pull-requests/how-tos/merge-and-close-"
            'pull-requests/merging-a-pull-request, fetched 25 Nov 2026: '
            'scroll to the bottom of the pull request and click "Merge '
            'pull request," then confirm with "Confirm merge" ("Confirm '
            'squash and merge" / "Confirm rebase and merge" for those '
            "methods, chosen from the merge dropdown); the page then "
            "offers to delete the branch.",
            "Under the hood this performs the same fast-forward merge "
            "the leader's local demo showed earlier (git merge "
            "origin/alex-notes --no-edit): \"Updating 4dd0320..f6562f0, "
            'Fast-forward" in this build\'s real local repo.',
            "Picture: a real screenshot embedded in GitHub's own docs "
            "page above, licensed CC BY 4.0, downloaded 25 Nov 2026, "
            "unmodified; see build/assets/github-docs-screenshots/"
            "SOURCE.md for the exact source URL.",
        ),
    ),
    dict(
        title="Prompt: pull the latest",
        kind="terminal",
        do_lines=(
            "Back in your own clone, before you start new work. Type "
            "this into Codex:",
        ),
        do_accent='"Pull the latest changes from GitHub."',
        term_lines=(
            "$ git pull origin main",
            "Fast-forward",
            "$ cat README.md",
            "- Alex: NVDA keeps closing above its 5-day high...",
            "- Jun: MU's RSI dropped below 30 overnight...",
        ),
        fallback=('"Already up to date" is not a failure: it means '
                  "nothing new was merged since your last pull."),
        credit="real git output, from this machine, today.",
        notes=(
            "Genuinely run today: a second teammate's local clone ran "
            "`git pull origin main` against the local stand-in after "
            "the leader pushed Jun's note to main, printing exactly "
            '"Updating f6562f0..91c6846" then "Fast-forward" (the '
            "commit range left off this picture to keep it short enough "
            "to read at full width); the resulting README.md shown is "
            "the real final file, with both teammates' lines, the "
            "one-evolving-example payoff. Its first two lines (the "
            '"# Group Stock Notes" heading and the blank project-notes '
            "line) are also left off here for the same reason; both are "
            "unchanged from the very first commit, shown in full back "
            "on the \"change a file\" slide.",
        ),
    ),
]

# Every walkthrough step is OS-agnostic (it happens inside Codex once both
# presenters' runs have finished), so each is "both" unless a step above
# set its own presenter explicitly.
for _step in WALKTHROUGH:
    _step.setdefault("presenter", "both")

COLLAB_RULES = deckkit.Content(
    title="Working as a group on your final project",
    lines=(
        "The leader creates the repository, with a README, and invites "
        "the co-leader and members by their GitHub usernames.",
        "Everyone clones it, works on their own branch, never directly "
        "on the main branch.",
        "Finish a piece of work, then push and open a pull request "
        "(gh pr create) instead of pushing straight to main.",
        "A teammate reviews it and merges it; everyone then pulls the "
        "latest before starting new work.",
    ),
    accent=("Never edit the same file as a teammate without pulling "
            "first."),
    origin="Both presenters",
)

CLOSING = deckkit.Closing(
    title="Thank you",
    lines=(
        f"Thank you for joining today's special lecture, taught "
        f"together by Benjamin C. Sotelo and Tyrone Miguel "
        f"{TYRONE_SURNAME}.",
        "Install Codex, sign in, then keep this deck open: every prompt "
        "you need is on these slides.",
        "Questions anytime, in class or after.",
    ),
)
