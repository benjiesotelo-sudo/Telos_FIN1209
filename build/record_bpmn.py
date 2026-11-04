#!/usr/bin/env python3
"""Build the example flowchart shape by shape in bpmn.io and capture a frame after each step.

    .venv/bin/python build/record_bpmn.py

Uses the chrome-devtools-axi browser (a separate Chrome instance, not the user's). bpmn.io
is driven through its own modeling API, so every shape and arrow is really created in the
editor and really drawn by it; the newly created element is selected so the viewer can see
which one it is. Writes build/generated/video/web/bpmn-build-NN.png and bpmn-build.json
(the narration lines per frame, taken from the handout's own shape-to-lines table).
"""
import json, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activity_chapter07 as A  # noqa: E402
import flowchart_chapter07 as FC  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "build" / "generated" / "video" / "web"
CLI = "chrome-devtools-axi"


def axi(*args) -> str:
    r = subprocess.run([CLI, *args], capture_output=True, text=True)
    return r.stdout


def js(code: str) -> str:
    return axi("eval", code)


TYPES = {"start": "bpmn:StartEvent", "end": "bpmn:EndEvent", "task": "bpmn:Task", "xor": "bpmn:ExclusiveGateway"}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    d = FC.build()
    nodes = {n.id: n for n in d.nodes}
    flows = {f.id: f for f in d.edges}
    rows = [row for b in A.flow_section().blocks if getattr(b, 'title', '').startswith('Which lines') for row in b.rows]
    lines = {nid: row[2] for nid, row in zip(['Start', 'T1', 'T2', 'G1', 'T3', 'T4', 'G2', 'G3', 'T5', 'G4', 'T6', 'T7', 'T8', 'T9', 'End'], rows)}
    # creation order and, for each, the flows that become possible once it exists
    order = ["Start", "T1", "T2", "G1", "T3", "T4", "G2", "G3", "T5", "G4", "T6", "T7", "T8", "T9", "End"]
    made: set = set()
    frames = []
    axi("open", "https://demo.bpmn.io/new"); time.sleep(3)
    axi("resize", "1600", "900")
    js("""() => { const m=window.bpmnio.modeler; const reg=m.get('elementRegistry');
      reg.filter(e=>e.type==='bpmn:StartEvent').forEach(e=>m.get('modeling').removeShape(e));
      m.get('canvas').viewbox({x:-20,y:-35,width:1420,height:800}); return 'cleared' }""")
    ids: dict = {}
    for k, nid in enumerate(order, 1):
        n = nodes[nid]
        label = n.name
        code = f"""() => {{ const m=window.bpmnio.modeler; const f=m.get('elementFactory'), mo=m.get('modeling'),
          root=m.get('canvas').getRootElement(), sel=m.get('selection');
          const w={n.size[0]}, h={n.size[1]};
          const s=f.createShape({{type:'{TYPES[n.kind]}', width:w, height:h}});
          const sh=mo.createShape(s, {{x:{n.cx}, y:{n.cy}}}, root);
          mo.updateLabel(sh, {json.dumps(label)});
          window.__ids = window.__ids || {{}}; window.__ids['{nid}'] = sh;
          sel.select(sh); return sh.id }}"""
        js(code)
        made.add(nid)
        new_flows = []
        for fid, fl in flows.items():
            if fl.src in made and fl.dst in made and fid not in ids:
                ids[fid] = True
                new_flows.append(fid)
        for fid in new_flows:
            fl = flows[fid]
            js(f"""() => {{ const m=window.bpmnio.modeler; const mo=m.get('modeling');
               const a=window.__ids['{fl.src}'], b=window.__ids['{fl.dst}'];
               const c=mo.connect(a,b,{{type:'bpmn:SequenceFlow'}});
               {"mo.updateLabel(c, %s);" % json.dumps(fl.label) if fl.label else ""} return c.id }}""")
        time.sleep(0.6)
        path = OUT / f"bpmn-build-{k:02d}.png"
        axi("screenshot", str(path))
        frames.append({"frame": path.name, "shape": nid, "kind": n.kind, "name": label,
                       "lines": lines[nid],
                       "flows": [flows[f].label or "" for f in new_flows]})
        print(k, nid, label)
    (OUT / "bpmn-build.json").write_text(json.dumps(frames, indent=1))


if __name__ == "__main__":
    main()
