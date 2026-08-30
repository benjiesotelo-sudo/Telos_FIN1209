#!/usr/bin/env python3
"""Render an HTML file to PDF with headless Chrome, and count the result.

Shared by build/build_plan.py and build/build_lecture_notes.py. Both print
documents in this repository are HTML with real print CSS, and both go through
here.

**Do not replace this with the LibreOffice HTML path.** That is what collapsed
every table in an earlier notes PDF to one character per column. Chrome renders
the same engine the CSS was written for.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def render_pdf(html_path: Path, pdf_path: Path, chrome: Path = CHROME,
               timeout: float = 120.0) -> None:
    """Render with headless Chrome, then stop waiting for it.

    Chrome 151 writes the PDF within a few seconds and then, in --headless=new
    --print-to-pdf mode on macOS, frequently does not exit at all. Waiting on
    the process is therefore not a completion signal. What is: the file
    appearing, its size settling, and it ending in the PDF end-of-file marker.
    Once all three hold, the render is finished and Chrome is terminated.
    """
    if not chrome.exists():
        raise SystemExit(
            f"headless Chrome not found at {chrome}. Install Google Chrome or "
            "pass --chrome."
        )
    if pdf_path.exists():
        pdf_path.unlink()

    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            str(chrome),
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            "--no-pdf-header-footer",
            "--allow-file-access-from-files",
            f"--print-to-pdf={pdf_path}",
            html_path.resolve().as_uri(),
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        try:
            deadline = time.monotonic() + timeout
            last = -1
            stable = 0
            while time.monotonic() < deadline:
                time.sleep(0.5)
                if not pdf_path.exists():
                    if proc.poll() is not None:
                        raise SystemExit(
                            "Chrome exited without writing a PDF. Run the same "
                            "command by hand to see why."
                        )
                    continue
                size = pdf_path.stat().st_size
                if size == last and size > 0:
                    stable += 1
                    if stable >= 2 and _looks_complete(pdf_path):
                        return
                else:
                    stable = 0
                last = size
            raise SystemExit(
                f"Chrome did not finish a PDF within {timeout:.0f}s. The "
                f"in-page paginator may be looping; open {html_path} in a "
                "browser and check the console."
            )
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()


def _looks_complete(pdf_path: Path) -> bool:
    """A PDF Chrome has finished writing ends in its end-of-file marker."""
    with pdf_path.open("rb") as fh:
        fh.seek(max(0, pdf_path.stat().st_size - 2048))
        return b"%%EOF" in fh.read()


def page_count(pdf_path: Path) -> int:
    """Count pages without a PDF library: the page tree declares the total."""
    blob = pdf_path.read_bytes()
    counts = [int(m) for m in re.findall(rb"/Count\s+(\d+)", blob)]
    if counts:
        return max(counts)
    return len(re.findall(rb"/Type\s*/Page[^s]", blob))


if __name__ == "__main__":                                # pragma: no cover
    print(__doc__, file=sys.stderr)
