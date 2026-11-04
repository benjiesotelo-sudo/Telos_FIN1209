#!/usr/bin/env python3
"""Write the example flowchart: .bpmn, .svg and a one page PDF."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bpmnkit, chrome, flowchart_chapter07  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "chapter-07" / "activity" / "First Automation FIN1209"
STEM = "First Automation FIN1209 - Example Flowchart"

if __name__ == "__main__":
    d = flowchart_chapter07.build()
    (OUT / f"{STEM}.bpmn").write_text(bpmnkit.to_bpmn(d))
    svg = bpmnkit.to_svg(d, 1.0)
    (OUT / f"{STEM}.svg").write_text(svg)
    html = ("<!doctype html><html><head><meta charset='utf-8'><style>"
            "@page{size:A4 landscape;margin:10mm}body{margin:0}"
            "h1{font:600 16px Helvetica;margin:0 0 6px}svg{width:100%;height:auto}"
            "</style></head><body><h1>First Automation FIN1209: the example script as a BPMN flowchart</h1>"
            + svg + "</body></html>")
    tmp = REPO / "build" / "generated" / "flowchart.html"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(html)
    chrome.render_pdf(tmp, OUT / f"{STEM}.pdf")
    print("ok")
