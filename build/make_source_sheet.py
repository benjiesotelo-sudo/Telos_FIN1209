#!/usr/bin/env python3
"""Rebuild the Google Sheet the activity's students pull their prices from.

    .venv/bin/python build/make_source_sheet.py                 # write the file
    .venv/bin/python build/make_source_sheet.py --upload        # and upload it

The activity has exactly one live dependency: a spreadsheet on the
instructor's Drive, shared "anyone with the link can view", holding both price
windows on two tabs called PartA and PartB. Students never edit it. They pull
from it with one IMPORTRANGE formula, which needs read access and nothing
more. Its id is printed on the worksheet, so it is also the one thing in this
repository that can be broken by somebody deleting a file.

This script is the recovery path. It builds the workbook from the committed
CSV files, so the tabs, the headers and the row counts are the same ones the
worksheet tells students to expect. With --upload it converts it to a Google
Sheet on the Drive rclone is configured for and shares it read only, then
prints the new id. Put that id into SOURCE_SHEET in
build/activity_chapter01.py and rebuild the PDFs.

The upload needs an OAuth token, and it takes it from `rclone config dump`
rather than asking for credentials of its own.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import mimetypes
import subprocess
import sys
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import activity_data as ad  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "build" / "generated" / "activity" / "source.xlsx"

SHEET_NAME = "FIN1209 Chapter 1 Activity - price data"

TABS = (("PartA", ad.PART_A), ("PartB", ad.PART_B))

SHEETS_MIME = "application/vnd.google-apps.spreadsheet"
XLSX_MIME = ("application/vnd.openxmlformats-officedocument"
             ".spreadsheetml.sheet")


def write_workbook(out: Path) -> Path:
    """One xlsx, one tab per window, FRED's own header on row 1."""
    import xlsxwriter

    out.parent.mkdir(parents=True, exist_ok=True)
    book = xlsxwriter.Workbook(str(out),
                               {"default_date_format": "yyyy-mm-dd"})
    date_format = book.add_format({"num_format": "yyyy-mm-dd"})
    for tab, series in TABS:
        sheet = book.add_worksheet(tab)
        sheet.write_row(0, 0, ["observation_date", series.fred_id])
        for row, (day, close) in enumerate(zip(series.dates, series.closes),
                                           start=1):
            sheet.write_datetime(row, 0, day, date_format)
            sheet.write_number(row, 1, close)
        sheet.set_column(0, 0, 14)
        sheet.set_column(1, 1, 12)
    book.close()
    return out


def _token() -> str:
    """rclone's live access token, refreshed by asking rclone to do something."""
    subprocess.run(["rclone", "about", "gdrive:"], capture_output=True)
    dump = subprocess.run(["rclone", "config", "dump"],
                          capture_output=True, text=True, check=True)
    remotes = json.loads(dump.stdout)
    if "gdrive" not in remotes:
        raise SystemExit(
            "rclone has no remote called gdrive, so this script cannot "
            "upload. Upload build/generated/activity/source.xlsx by hand: "
            "drop it into Drive, open it, File then Save as Google Sheets, "
            "and share the result to anyone with the link as a viewer."
        )
    return json.loads(remotes["gdrive"]["token"])["access_token"]


def _post(url: str, token: str, body: bytes, content_type: str) -> dict:
    request = urllib.request.Request(url, data=body, method="POST")
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("Content-Type", content_type)
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())


def upload(path: Path, name: str) -> str:
    """Convert the workbook to a Google Sheet and share it read only."""
    token = _token()
    boundary = f"fin1209-{uuid.uuid4().hex}"
    metadata = json.dumps({"name": name, "mimeType": SHEETS_MIME})
    parts = [
        f"--{boundary}\r\n".encode(),
        b"Content-Type: application/json; charset=UTF-8\r\n\r\n",
        metadata.encode() + b"\r\n",
        f"--{boundary}\r\n".encode(),
        f"Content-Type: {XLSX_MIME}\r\n\r\n".encode(),
        path.read_bytes(),
        f"\r\n--{boundary}--\r\n".encode(),
    ]
    created = _post(
        "https://www.googleapis.com/upload/drive/v3/files"
        "?uploadType=multipart&fields=id,name",
        token, b"".join(parts),
        f"multipart/related; boundary={boundary}")
    file_id = created["id"]

    # Viewer, never writer. A publicly editable sheet is one student away
    # from every other student's data being wrong.
    _post(f"https://www.googleapis.com/drive/v3/files/{file_id}/permissions",
          token, json.dumps({"role": "reader", "type": "anyone"}).encode(),
          "application/json")
    return file_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--name", default=SHEET_NAME)
    parser.add_argument("--upload", action="store_true",
                       help="convert it to a Google Sheet and share it read "
                            "only, then print the new spreadsheet id")
    args = parser.parse_args()

    path = write_workbook(args.out)
    for tab, series in TABS:
        print(f"{tab}: {series.fred_id}, {series.rows} rows, "
              f"A1:B{series.last_row}, {series.start} to {series.end}")
    print(f"workbook: {path}")

    if args.upload:
        file_id = upload(path, args.name)
        print(f"uploaded: {file_id}")
        print("next    : put that id into SOURCE_SHEET in "
              "build/activity_chapter01.py, then rebuild both PDFs.")
    else:
        print("upload  : not requested. Add --upload, or drop the file into "
              "Drive by hand and share it to anyone with the link as a "
              "viewer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
