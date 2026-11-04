"""Write a small BPMN 2.0 diagram as a .bpmn file and as an SVG picture.

Knows nothing about any chapter. A diagram is plain data: nodes (start, end, task, xor gateway,
data object, text annotation, group) with a centre point, and edges (sequence flow, association,
data input, data output) with waypoints and an optional label. The same data feeds both outputs,
so the picture and the file cannot disagree. The .bpmn opens in bpmn.io with its layout intact.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from html import escape

SIZES = {"start": (36, 36), "end": (36, 36), "task": (130, 64), "xor": (50, 50), "data": (36, 50),
         "note": (200, 70), "group": (300, 300)}
TAG = {"start": "startEvent", "end": "endEvent", "task": "task", "xor": "exclusiveGateway",
       "data": "dataObjectReference", "note": "textAnnotation", "group": "group"}


@dataclass
class Node:
    id: str
    kind: str
    name: str
    cx: float
    cy: float
    lines: tuple[str, ...] = ()
    label_at: str = "below"
    w: float = 0
    h: float = 0

    @property
    def size(self):
        d = SIZES[self.kind]
        return (self.w or d[0], self.h or d[1])

    @property
    def box(self):
        w, h = self.size
        return self.cx - w / 2, self.cy - h / 2, w, h


@dataclass
class Edge:
    id: str
    src: str
    dst: str
    points: tuple[tuple[float, float], ...]
    label: str = ""
    kind: str = "flow"      # flow, assoc, datain, dataout


@dataclass
class Diagram:
    id: str
    name: str
    nodes: list[Node] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)

    def bounds(self):
        xs, ys = [], []
        for n in self.nodes:
            x, y, w, h = n.box
            xs += [x, x + w]; ys += [y, y + h]
        for e in self.edges:
            for px, py in e.points:
                xs.append(px); ys.append(py)
        return min(xs) - 20, min(ys) - 20, max(xs) + 20, max(ys) + 40


def _q(t: str) -> str:
    return escape(t, {'"': "&quot;"})


def to_bpmn(d: Diagram) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
           'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
           'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
           'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
           f'id="Definitions_{d.id}" targetNamespace="http://bpmn.io/schema/bpmn">']
    for n in d.nodes:
        if n.kind == "group":
            out.append(f'  <bpmn:category id="Cat_{n.id}"><bpmn:categoryValue id="CV_{n.id}" value="{_q(n.name)}" /></bpmn:category>')
    out.append(f'  <bpmn:process id="{d.id}" isExecutable="false">')
    node = {n.id: n for n in d.nodes}
    flows = [e for e in d.edges if e.kind == "flow"]
    inc = {n.id: [] for n in d.nodes}; outg = {n.id: [] for n in d.nodes}
    for e in flows:
        outg[e.src].append(e.id); inc[e.dst].append(e.id)
    datain = {}; dataout = {}
    for e in d.edges:
        if e.kind == "datain": datain.setdefault(e.dst, []).append(e)
        if e.kind == "dataout": dataout.setdefault(e.src, []).append(e)
    for n in d.nodes:
        if n.kind == "data":
            out.append(f'    <bpmn:dataObject id="DO_{n.id}" />')
    for n in d.nodes:
        if n.kind == "group":
            out.append(f'    <bpmn:group id="{n.id}" categoryValueRef="CV_{n.id}" />')
        elif n.kind == "note":
            out.append(f'    <bpmn:textAnnotation id="{n.id}"><bpmn:text>{_q(chr(10).join(n.lines))}</bpmn:text></bpmn:textAnnotation>')
        elif n.kind == "data":
            out.append(f'    <bpmn:dataObjectReference id="{n.id}" name="{_q(n.name)}" dataObjectRef="DO_{n.id}" />')
        else:
            out.append(f'    <bpmn:{TAG[n.kind]} id="{n.id}" name="{_q(n.name)}">')
            for i in inc[n.id]: out.append(f'      <bpmn:incoming>{i}</bpmn:incoming>')
            for o in outg[n.id]: out.append(f'      <bpmn:outgoing>{o}</bpmn:outgoing>')
            for e in datain.get(n.id, []):
                out.append(f'      <bpmn:dataInputAssociation id="{e.id}"><bpmn:sourceRef>{e.src}</bpmn:sourceRef></bpmn:dataInputAssociation>')
            for e in dataout.get(n.id, []):
                out.append(f'      <bpmn:dataOutputAssociation id="{e.id}"><bpmn:targetRef>{e.dst}</bpmn:targetRef></bpmn:dataOutputAssociation>')
            out.append(f'    </bpmn:{TAG[n.kind]}>')
    for e in flows:
        nm = f' name="{_q(e.label)}"' if e.label else ""
        out.append(f'    <bpmn:sequenceFlow id="{e.id}"{nm} sourceRef="{e.src}" targetRef="{e.dst}" />')
    for e in d.edges:
        if e.kind == "assoc":
            out.append(f'    <bpmn:association id="{e.id}" sourceRef="{e.src}" targetRef="{e.dst}" />')
    out.append('  </bpmn:process>')
    out.append(f'  <bpmndi:BPMNDiagram id="Diagram_{d.id}">')
    out.append(f'    <bpmndi:BPMNPlane id="Plane_{d.id}" bpmnElement="{d.id}">')
    for n in d.nodes:
        x, y, w, h = n.box
        extra = ' isMarkerVisible="true"' if n.kind == "xor" else ""
        out.append(f'      <bpmndi:BPMNShape id="{n.id}_di" bpmnElement="{n.id}"{extra}>')
        out.append(f'        <dc:Bounds x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" />')
        if n.kind in ("start", "end", "xor", "data"):
            lx = n.cx - 60; ly = n.cy + h / 2 + 4
            if n.label_at == "above": ly = n.cy - h / 2 - 31
            elif n.label_at == "aboveleft": lx = n.cx - 135; ly = n.cy - h / 2 - 31
            elif n.label_at == "belowleft": lx = n.cx - 135; ly = n.cy + h / 2 + 14
            elif n.label_at == "right": lx = n.cx + w / 2 + 4; ly = n.cy - 14
            out.append(f'        <bpmndi:BPMNLabel><dc:Bounds x="{lx:g}" y="{ly:g}" width="120" height="27" /></bpmndi:BPMNLabel>')
        out.append('      </bpmndi:BPMNShape>')
    for e in d.edges:
        out.append(f'      <bpmndi:BPMNEdge id="{e.id}_di" bpmnElement="{e.id}">')
        for px, py in e.points:
            out.append(f'        <di:waypoint x="{px:g}" y="{py:g}" />')
        out.append('      </bpmndi:BPMNEdge>')
    out += ['    </bpmndi:BPMNPlane>', '  </bpmndi:BPMNDiagram>', '</bpmn:definitions>', '']
    return "\n".join(out)


def to_svg(d: Diagram, scale: float = 1.0) -> str:
    x0, y0, x1, y1 = d.bounds()
    w, h = x1 - x0, y1 - y0
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:g} {y0:g} {w:g} {h:g}" '
         f'width="{w*scale:g}" height="{h*scale:g}" font-family="Helvetica, Arial, sans-serif" font-size="12">',
         '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" fill="#222"/></marker></defs>']
    # groups first, so everything else draws over them
    for n in d.nodes:
        if n.kind == "group":
            x, y, ww, hh = n.box
            s.append(f'<rect x="{x:g}" y="{y:g}" width="{ww:g}" height="{hh:g}" rx="14" fill="#f4f8f5" stroke="#1E5631" stroke-width="1.6" stroke-dasharray="10 5"/>')
            s.append(f'<text x="{x+12:g}" y="{y+22:g}" font-size="15" font-weight="bold" fill="#1E5631">{escape(n.name)}</text>')
    for e in d.edges:
        pts = " ".join(f"{px:g},{py:g}" for px, py in e.points)
        if e.kind == "assoc":
            s.append(f'<polyline points="{pts}" fill="none" stroke="#555" stroke-width="1.2" stroke-dasharray="2 3"/>')
        elif e.kind in ("datain", "dataout"):
            s.append(f'<polyline points="{pts}" fill="none" stroke="#222" stroke-width="1.3" stroke-dasharray="2 3" marker-end="url(#ar)"/>')
        else:
            s.append(f'<polyline points="{pts}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
        if e.label and e.kind == "flow":
            (ax, ay), (bx, by) = e.points[0], e.points[1]
            if ay == by:
                lx, ly = (ax + bx) / 2 - 8, ay - 7
            else:
                lx, ly = ax + 7, (ay + by) / 2 + 4
            s.append(f'<text x="{lx:g}" y="{ly:g}" font-size="12" font-weight="bold" fill="#8a1c1c">{escape(e.label)}</text>')
    for n in d.nodes:
        x, y, ww, hh = n.box
        if n.kind == "task":
            s.append(f'<rect x="{x:g}" y="{y:g}" width="{ww:g}" height="{hh:g}" rx="10" fill="#fff" stroke="#222" stroke-width="1.8"/>')
            ls = n.lines or (n.name,)
            top = n.cy - (len(ls) - 1) * 7 + 4
            for k, t in enumerate(ls):
                s.append(f'<text x="{n.cx:g}" y="{top + k * 14:g}" text-anchor="middle" font-size="12">{escape(t)}</text>')
        elif n.kind == "note":
            s.append(f'<path d="M{x+14:g},{y:g} L{x:g},{y:g} L{x:g},{y+hh:g} L{x+14:g},{y+hh:g}" fill="none" stroke="#555" stroke-width="1.4"/>')
            for k, t in enumerate(n.lines):
                s.append(f'<text x="{x+8:g}" y="{y+15+k*13.5:g}" font-size="11" fill="#222">{escape(t)}</text>')
        elif n.kind == "data":
            s.append(f'<path d="M{x:g},{y:g} L{x+ww-10:g},{y:g} L{x+ww:g},{y+10:g} L{x+ww:g},{y+hh:g} L{x:g},{y+hh:g} Z" fill="#fff" stroke="#222" stroke-width="1.5"/>')
            s.append(f'<path d="M{x+ww-10:g},{y:g} L{x+ww-10:g},{y+10:g} L{x+ww:g},{y+10:g}" fill="none" stroke="#222" stroke-width="1.2"/>')
            ls = n.lines or (n.name,)
            lx, anchor = (n.cx + ww / 2 + 6, "start") if n.label_at == "right" else (n.cx, "middle")
            ty = n.cy - (len(ls) - 1) * 7 + 4 if n.label_at == "right" else y + hh + 15
            for k, t in enumerate(ls):
                s.append(f'<text x="{lx:g}" y="{ty + k * 14:g}" text-anchor="{anchor}" font-size="11.5" font-weight="bold">{escape(t)}</text>')
        elif n.kind == "xor":
            s.append(f'<polygon points="{n.cx:g},{y:g} {x+ww:g},{n.cy:g} {n.cx:g},{y+hh:g} {x:g},{n.cy:g}" fill="#fff" stroke="#222" stroke-width="1.8"/>')
            s.append(f'<path d="M{n.cx-8:g},{n.cy-8:g} L{n.cx+8:g},{n.cy+8:g} M{n.cx+8:g},{n.cy-8:g} L{n.cx-8:g},{n.cy+8:g}" stroke="#222" stroke-width="2.4"/>')
            ls = n.lines or (n.name,)
            for k, t in enumerate(ls):
                ax, anchor = n.cx, "middle"
                if n.label_at == "above": ty = y - 8 - (len(ls) - 1 - k) * 14
                elif n.label_at == "belowleft": ax, anchor, ty = n.cx - 10, "end", y + hh + 28 + k * 14
                elif n.label_at == "aboveleft": ax, anchor, ty = n.cx - 24, "end", y - 4 - (len(ls) - 1 - k) * 14
                elif n.label_at == "right": ax, anchor, ty = n.cx + 32, "start", n.cy + 4 + (k - (len(ls) - 1) / 2) * 14
                else: ty = y + hh + 16 + k * 14
                s.append(f'<text x="{ax:g}" y="{ty:g}" text-anchor="{anchor}" font-size="11.5">{escape(t)}</text>')
        elif n.kind in ("start", "end"):
            sw = 1.8 if n.kind == "start" else 4.5
            s.append(f'<circle cx="{n.cx:g}" cy="{n.cy:g}" r="18" fill="#fff" stroke="#222" stroke-width="{sw}"/>')
            for k, t in enumerate(n.lines or (n.name,)):
                if n.label_at == "right":
                    s.append(f'<text x="{n.cx + 26:g}" y="{n.cy + 4 + (k - (len(n.lines or (n.name,)) - 1) / 2) * 14:g}" text-anchor="start" font-size="11.5">{escape(t)}</text>')
                else:
                    s.append(f'<text x="{n.cx:g}" y="{y+hh+16+k*14:g}" text-anchor="middle" font-size="11.5">{escape(t)}</text>')
    s.append('</svg>')
    return "\n".join(s)
