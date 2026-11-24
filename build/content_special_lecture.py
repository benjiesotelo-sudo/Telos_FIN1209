"""Content for the FIN1209 special lecture: AI CLI tools, Git and GitHub.

Plain data, read by build_special_lecture.py. Not a textbook chapter, so it
does not use deckkit.Chapter/Section (parts, dividers, checks, answer keys):
those exist for a Lim chapter and nothing here claims to teach Lim. It still
uses deckkit's Content, TitleSlide and Closing slide types and its FEU visual
identity, because the lecture is taught in the same room from the same
projector as every other FIN1209 deck.

This edition is a real, hands-on walkthrough, one action per slide, built
around a single evolving example: "group-stock-notes", a shared README.md
each teammate adds one line to. Two kinds of evidence back it:

  * SCREENSHOT - genuinely run on this machine today, in a throwaway local
    folder (codex --version, git --version, git init/branch/add/commit/log,
    a real `codex exec` prompt). Nothing new was installed; nothing was
    pushed to GitHub, signed in or out of, or shared with anyone. Where the
    real workflow needs a GitHub remote, a local bare repository stands in
    for it, disclosed in that slide's notes. See build_special_lecture.py
    for the exact commands.
  * ILLUSTRATION - a step no local command can show (the installer's own
    run, GitHub sign-up, sign-in, invites, the pull request pages, anything
    on Windows): a plain mockup of the documented screen, built from
    GitHub's and OpenAI's own current documentation, fetched today and
    cited in that slide's notes. Never a live screenshot.

Every command and every citation was fetched or run today (25 Nov 2026),
not from memory. See each slide's speaker notes for its exact source.
"""

from __future__ import annotations

import deckkit

TITLE = deckkit.TitleSlide(
    course="FIN1209 - Technical Analysis in Investment, FEU Manila",
    chapter="Special lecture",
    title="AI Tools, Git and GitHub for Your Final Project",
    subtitle=("A step-by-step walkthrough: Codex, Git and GitHub, one "
              "worked example the whole way"),
    presenter=("Benjamin C. Sotelo, with Tyrone Miguel Arriolado helping set "
               "up your computers today"),
    notes=(
        "This is a one-off special lecture, not a Lim chapter: everything "
        "about Codex, Git and GitHub is general tool knowledge, never "
        "presented as the textbook's.",
        "Quiz 6 is the group final project: three groups, each with a "
        "leader and a co-leader.",
        "The worked example, group-stock-notes, is invented for this "
        "lecture; it is not a real group's repository.",
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
    notes=(
        "\"AI CLI tool\" is not a Lim term; it is general software "
        "knowledge for this lecture only.",
        "CLI = command line interface: the terminal window, not a "
        "website or an app icon.",
    ),
)

MAC_INSTALL = deckkit.Content(
    title="Install Codex: macOS",
    lines=(
        "Open Terminal: press Cmd+Space, type Terminal, press Enter.",
        "Paste the command below, press Enter, and wait for it to "
        "finish.",
    ),
    accent="curl -fsSL https://chatgpt.com/codex/install.sh | sh",
    caption=("Source: learn.chatgpt.com/codex/cli and github.com/openai/"
             "codex's README, both fetched 25 Nov 2026, same command."),
    notes=(
        "Exact command quoted verbatim from both learn.chatgpt.com/"
        "codex/cli (macOS/Linux tab) and the openai/codex GitHub "
        "README, each fetched 25 Nov 2026 and showing the identical "
        "command.",
        "No prerequisite install (no Node.js, no Homebrew) is required "
        "for this standalone installer; the docs state none.",
        "An npm alternative exists (npm install -g @openai/codex) for "
        "anyone who already has Node.js, and a Homebrew cask (brew "
        "install --cask codex); neither is the default path here.",
        "Not re-run live: Codex is already installed on this machine "
        "(codex-cli 0.164.0, confirmed below), so this slide is the "
        "command itself, not a fresh install capture.",
    ),
)

WIN_INSTALL = deckkit.Content(
    title="Install Codex: Windows",
    lines=(
        "Open PowerShell: press the Start key, type PowerShell, press "
        "Enter.",
        "Paste the command below into the new PowerShell window and "
        "press Enter.",
    ),
    accent=('powershell -ExecutionPolicy ByPass -c "irm '
            'https://chatgpt.com/codex/install.ps1 | iex"'),
    caption=("Windows 10 or 11: the PowerShell installer above. If it "
             "fails, Tyrone will set up WSL2 with you."),
    notes=(
        "Exact command quoted verbatim from github.com/openai/codex's "
        "README, fetched 25 Nov 2026 (a native Windows install, no "
        "WSL): this is the one we lead with.",
        "openai/codex's own docs/install.md, fetched 25 Nov 2026, lists "
        '"Windows 11 via WSL2" in its system requirements table: the '
        "project's own docs are not fully consistent on whether WSL is "
        "required, which is exactly why today's fallback is Tyrone "
        "setting up WSL2 by hand if the native installer fails for "
        "anyone.",
        "No Windows machine is available to this build; everything on "
        "the two Windows slides is ILLUSTRATION, built from the cited "
        "docs, never a live capture.",
    ),
)

# The dedicated slides requested by name: the error expected right after
# install, one per operating system so each reads from the back of the
# room. The image is just the error itself, large; the fix is large actual
# slide text, not small caption text, per the readability review.
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

WIN_ERROR_SHOT = dict(
    title="The error you will probably see: Windows",
    label="ILLUSTRATION",
    term_lines=("PS> codex", "codex : term 'codex' is not recognized"),
    lines=(
        "The installer updates PATH in a CHILD PowerShell window; this "
        "window never saw it.",
    ),
    accent="Fix: close this PowerShell window, open a brand-new one, then run: codex",
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

SIGNIN = deckkit.Content(
    title="Sign in to Codex",
    lines=(
        "In the same terminal, type: codex",
        "The first time, Codex asks you to sign in.",
        'Choose "Sign in with ChatGPT" and finish in your browser.',
    ),
    accent=("Codex is included across ChatGPT plans, including Free "
            "and Go."),
    caption=("Usage limits vary by plan. Source: OpenAI help center, "
             '"Using Codex with your ChatGPT plan," fetched 25 Nov '
             "2026."),
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
        "build).",
    ),
)

TRANSITION = deckkit.Content(
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
)

# A dedicated picture slide, not a Content slide, so the flow itself is the
# teaching: your computer, push, GitHub, pull, a teammate's computer.
GIT_GITHUB_SHOT = dict(
    title="What are Git and GitHub?",
    label="ILLUSTRATION",
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
    accent="One new thing happens per slide; what's new reads in green.",
)

# --------------------------------------------------------------------------
# The walkthrough itself: one action per slide. "kind" is "terminal" (a real
# command captured on this machine today) or "doc" (no real screen is
# possible, so a plain mockup of GitHub's or OpenAI's own current
# documentation stands in, cited in notes, never presented as a live
# capture). See build_special_lecture.py for exactly how each image is
# drawn and build_special_lecture.py's module docstring for the real
# commands this is built from.
# --------------------------------------------------------------------------

WALKTHROUGH = [
    dict(
        title="Prompt: check Git is installed",
        kind="terminal",
        do_lines=("Type this into Codex:",),
        do_accent=('"Check whether Git is installed on this computer. If '
                    'it is not, install it, then tell me how to confirm '
                    'it worked."'),
        term_lines=(
            "$ git --version",
            "git version 2.50.1 (Apple Git-155)",
            "codex: Git is installed, version 2.50.1.",
        ),
        fallback=("If Git is missing, Codex installs it the normal way "
                  "for your OS (Homebrew on Mac, winget on Windows) and "
                  "reports the version the same way."),
        credit="real Codex output, from this machine, today.",
        notes=(
            "Genuinely run today: `codex exec -s workspace-write "
            '-C <scratch-folder> "Check whether git is installed on this '
            'computer. If it is not, install it, then tell me how to '
            'confirm it worked."`, in a throwaway folder, nothing new '
            "installed (git was already present). Session id "
            "01a20f07-3f87-70b1-bf19-463204ef4d4a. Codex's real reply: "
            '"I\'ll check whether Git is available and print its '
            'version... Git is installed: git version 2.50.1 (Apple '
            'Git-155)."',
            "Trimmed for the slide (full real transcript quoted in the "
            "line above): this machine's own hook and enterprise-config "
            "warning lines (SessionStart hooks, a web_search_mode "
            "override notice), specific to this captain's own Codex "
            "setup and not something a student on a vanilla install "
            "would see; and the exec/succeeded framing, condensed to the "
            "plain command and its real result so the picture reads "
            "large enough from the back of the room.",
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
            "No account was created, no gh was installed, and no sign-in "
            "was performed for this build, per the brief's own limits.",
        ),
    ),
    dict(
        title="Prompt: set your name and email",
        kind="terminal",
        do_lines=(
            "Every commit you make is labeled with a name and an "
            "email. Type this into Codex:",
        ),
        do_accent=('"Set up my Git identity for this repository with my '
                    'name and my email, so my commits are labeled '
                    'correctly."'),
        term_lines=(
            "$ git config --local user.name 'Alex Dela Cruz'",
            "$ git config --local user.email 'alex...@example.edu'",
            "$ git config --local --get-regexp 'user.(name|email)'",
            "user.name Alex Dela Cruz",
            "user.email alex.delacruz@example.edu",
        ),
        fallback=("If Codex says it is blocked, approve it, or run the "
                  "two lines it prints yourself."),
        credit="real git output, from this machine, today.",
        notes=(
            "Genuinely run today in the throwaway folder: `git config "
            "--local user.name 'Alex Dela Cruz'`, `git config --local "
            "user.email 'alex.delacruz@example.edu'`, then `git config "
            "--local --get-regexp 'user.(name|email)'`, which printed "
            "exactly the two lines shown.",
            "The fallback line is also real, not invented: in this exact "
            "folder, a sandboxed `codex exec` call (session id "
            "01a20f07-9c90-7521-abb0-dc0ad68315d7) could not write "
            ".git/config and printed the same two config commands shown "
            "above as its own suggested fix, which then worked when run "
            "directly. That sandbox refusal is a quirk of this "
            "captain's own Codex setup, not something most students will "
            "hit, so it is the fallback line here rather than the main "
            "picture; a student who does see it can simply approve the "
            "write when Codex asks, or run the two lines themselves.",
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
                    'group-stock-notes for our final project."'),
        term_lines=(
            "$ gh repo create group-stock-notes --private",
            "Created repository yourname/group-stock-notes",
        ),
        fallback=('No gh? On github.com: top right "+" icon, then "New '
                  'repository," name it, choose Private, click "Create '
                  'repository."'),
        credit="GitHub CLI's own docs, fetched today, not a live run.",
        notes=(
            "cli.github.com/manual/gh_repo_create, fetched 25 Nov 2026: "
            'synopsis "gh repo create [<name>] [flags]"; a non-private '
            "remote needs one of --public/--private/--internal, e.g. the "
            'page\'s own example "gh repo create my-project --public '
            '--clone." The exact success-message wording on the second '
            "line was not confirmed against a real run (no repository "
            "was created for this build, per the brief's own limits), so "
            "it is a reasonable paraphrase, not a verbatim quote.",
            "The fallback (browser) path is docs.github.com/en/"
            "repositories/creating-and-managing-repositories/creating-a-"
            'new-repository, fetched 25 Nov 2026: the "+" icon in the '
            'upper right (aria-label "Create something new"), then New '
            "repository; fields are an Owner dropdown, the repository "
            "name (letters, digits, `.`, `-`, `_` only), an optional "
            "description, and a Public/Private choice, finished with "
            "Create repository.",
        ),
    ),
    dict(
        title="Leader prompt: invite your teammates",
        kind="terminal",
        label="ILLUSTRATION",
        do_lines=("Still the leader, still once per group. Type this "
                  "into Codex:",),
        do_accent=('"Invite Alex and Jun to group-stock-notes as '
                    'collaborators."'),
        term_lines=(
            "$ gh api --method PUT repos/yourname/group-stock-notes/",
            "    collaborators/alex",
            "$ gh api --method PUT repos/yourname/group-stock-notes/",
            "    collaborators/jun",
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
            "docs today (the page this build expected to cite 404s), so "
            "this slide states only what is confirmed: an email "
            "invitation that must be accepted, nothing more specific.",
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
        kind="doc",
        do_lines=("Type this into Codex:",),
        do_accent='"Open a pull request for my branch."',
        doc_site="github.com/.../pull/new",
        doc_lines=(
            'A yellow banner offers "Compare & pull request."',
            'Type a title and description, then click "Create Pull '
            'Request."',
        ),
        fallback="No banner? Open the Pull requests tab and click New pull request yourself.",
        credit="GitHub's own docs, fetched today, not a live capture.",
        notes=(
            "docs.github.com/en/pull-requests/how-tos/create-pull-"
            "requests/creating-a-pull-request, fetched 25 Nov 2026: "
            'after pushing, GitHub shows a yellow banner with "Compare '
            '& pull request"; pick the base and compare branches, type '
            'a title and description, then click "Create Pull Request" '
            "(a draft option also exists).",
            "No pull request was opened for this build, per the "
            "brief's own limits.",
        ),
    ),
    dict(
        title="Review the pull request",
        kind="doc",
        do_lines=(
            "A teammate, not the author, does this step.",
            "On the pull request page:",
        ),
        do_accent='Open "Files changed," click "Review changes."',
        doc_site="github.com/.../pull/1/files",
        doc_lines=(
            'Choose Comment, Approve, or "Request changes," then '
            '"Submit review."',
        ),
        fallback="Authors cannot approve their own pull request; ask a teammate.",
        credit="GitHub's own docs, fetched today, not a live capture.",
        notes=(
            "docs.github.com/en/pull-requests/how-tos/review-pull-"
            "requests/reviewing-proposed-changes-in-a-pull-request, "
            'fetched 25 Nov 2026: open "Files changed," click "Review '
            'changes" above the diff, write a summary, choose Comment, '
            'Approve or "Request changes," then "Submit review." '
            '"Request changes" does not block merging unless a branch '
            "rule requires it, and the docs state authors cannot "
            "approve their own pull request.",
        ),
    ),
    dict(
        title="Merge the pull request",
        kind="doc",
        do_lines=("Once approved, on the same page:",),
        do_accent='Click "Merge pull request," then "Confirm merge."',
        doc_site="github.com/.../pull/1",
        doc_lines=(
            "GitHub then offers to delete the now-merged branch.",
        ),
        fallback='Button greyed out? The review is not approved yet, or a check is still running.',
        credit="GitHub's own docs, fetched today, not a live capture.",
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

COLLAB_RULES = deckkit.Content(
    title="How your group collaborates on your final project",
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
)

STOCK_DESK_INTRO = deckkit.Content(
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
)

# The two Stock Desk pictures. The first is a composite built at build
# time from two crops of the same screenshot (the chart, and the signal
# panel beside it), placed side by side so the combined picture is wide
# enough to fill the slide. The second is a made-up example position, not
# a real one: the earlier screenshot showed a test buy since deleted from
# the real tool, so this slide is now a plain illustration instead of a
# screenshot of something that no longer exists.
STOCK_DESK_SHOTS = [
    dict(
        title="Stock Desk: live prices and signals",
        label="SCREENSHOT",
        shows=("The chart and the signal panel: live prices, Chapter 8's "
               "signal rule and a session replay."),
        source_file="deployed-final-ipad.png",
        composite="chart_panel",
        credit=("My own tool, signed in with my own passphrase. Live Yahoo "
                "prices, Chapter 8's five-day-high / RSI / MACD signal "
                "rule, fundamentals from each company's own SEC filing, "
                "and a session replay."),
        notes=(
            "How I use it, for my own reference (not shown to the class): "
            "sign in with my passphrase, pick a stock from the watchlist, "
            'read "Last signal fired" and the live reading below it, then '
            "log a buy only if I decide to act on it; replay the last "
            "session to see the signals fire again. Full how-to: the "
            "firstmate home's data/stock-desk-answers/report.md section 2.",
            "Students never get the passphrase or access; this is a "
            "demonstration, never a class assignment.",
        ),
    ),
    dict(
        title="Stock Desk: logging a position (example)",
        label="ILLUSTRATION",
        composite="example_position",
        credit=("A made-up example, not a real position: Stock Desk's "
                "position card after logging a buy records the price, the "
                "stop and the target; the tool never places a trade, it "
                "only tracks one I decide to log myself."),
        notes=(
            "The real screenshot this slide used to show (a test buy on "
            "NVDA, logged while checking this feature) has since been "
            "deleted from the real tool, so an invented example replaces "
            "it, clearly labelled ILLUSTRATION rather than SCREENSHOT.",
        ),
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
