"""The order in which the video types the example script, one clip at a time.

Shared by the recorder (which types it on screen) and the video scenes (which narrate it), so the
two cannot differ. Each step starts from the previous step's code and ends on its own: first the
throwaway check line of the last step is deleted, then new lines are typed in groups, each group
explained by explain_chapter07.GROUPS. Clip names: 02a-type, 02b-del, 02z-run.
"""
from __future__ import annotations

import re
import difflib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import difflib

import activity_chapter07_code as CODE
import explain_chapter07 as EX


def final_lines() -> list:
    return CODE.SCRIPT.read_text(encoding="utf-8").splitlines()


def stage_text(step: int) -> list:
    return CODE.stage_code(step).splitlines()


def norm(l: str) -> str:
    return re.sub(r" {2,}", " ", l.strip())


def step_plan(step: int) -> list:
    """The clips of one step, in typing order: deletions, groups of inserted lines (each with its explanation), the run."""
    prev = stage_text(step - 1) if step > 1 else []
    cur = stage_text(step)
    F = final_lines()
    # which final line each current line is (None for the throwaway print line)
    fm = {}
    sm = difflib.SequenceMatcher(None, [norm(x) for x in cur], [norm(x) for x in F], autojunk=False)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            fm[blk.a + k] = blk.b + k + 1
    clips = []
    # 1. deletions first, bottom to top, so an index never shifts under us
    sm = difflib.SequenceMatcher(None, [norm(x) for x in prev], [norm(x) for x in cur], autojunk=False)
    kept = list(prev)
    for tag, i1, i2, j1, j2 in reversed(sm.get_opcodes()):
        if tag in ("delete", "replace"):
            for i in range(i2 - 1, i1 - 1, -1):
                clips.append(dict(kind="delete", at=i))
                del kept[i]
    # 2. insertions, forward, against what is left
    sm = difflib.SequenceMatcher(None, [norm(x) for x in kept], [norm(x) for x in cur], autojunk=False)
    offset = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("insert", "replace"):
            groups = []
            for j in range(j1, j2):
                fl = fm.get(j)
                g = EX.group_for(fl) if fl else None
                key = ("temp",) if fl is None else (("g", g[1]) if g else None)
                if key is None and groups:
                    groups[-1]["lines"].append(cur[j]); continue
                if groups and groups[-1]["key"] == key:
                    groups[-1]["lines"].append(cur[j])
                elif key is None:
                    groups.append(dict(key=("g", 0), lines=[cur[j]], say=""))
                else:
                    groups.append(dict(key=key, lines=[cur[j]],
                                       say=EX.TEMP_SAY[step] if key == ("temp",) else g[3]))
            pos = j1
            for g in groups:
                clips.append(dict(kind="type", after=pos - 1, lines=g["lines"], say=g["say"], temp=g["key"] == ("temp",)))
                pos += len(g["lines"])
    return clips




def clip_names(step: int) -> list:
    """[(clip name, plan item)] for one step, ending with its run clip."""
    out, letters = [], iter("abcdefghijklmnopqrstuvwxyz")
    for c in step_plan(step):
        out.append((f"{step:02d}{next(letters)}-{'del' if c['kind'] == 'delete' else 'type'}", c))
    out.append((f"{step:02d}z-run", dict(kind="run")))
    return out
