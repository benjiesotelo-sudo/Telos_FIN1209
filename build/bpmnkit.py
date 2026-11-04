"""Write a small BPMN 2.0 diagram as a .bpmn file and as an SVG picture.

Knows nothing about any chapter. A diagram is plain data: nodes with a kind,
a name and a centre point, and edges with a source, a target, optional
waypoints and an optional label. The same data feeds both outputs, so the
picture and the file cannot disagree. The .bpmn file opens in bpmn.io and in
Camunda Modeler with its layout intact.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from html import escape

SIZES = {"start": (36, 36), "end": (36, 36), "task": (130, 70),
         "xor": (50, 50)}
TAG = {"start": "startEvent", "end": "endEvent", "task": "task",
       "xor": "exclusiveGateway"}


@dataclass
class Node:
    id: str
    kind: str          # start, end, task, xor
    name: str
    cx: float
    cy: float
    lines: tuple[str, ...] = ()   # task text, already wrapped
    label_at: str = "below"       # below, above, belowleft, aboveleft

    @property
    def size(self):
        return SIZES[self.kind]

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
        return min(xs) - 30, min(ys) - 30, max(xs) + 30, max(ys) + 50


def to_bpmn(d: Diagram) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
           'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
           'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
           'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
           f'id="Definitions_{d.id}" targetNamespace="http://bpmn.io/schema/bpmn">',
           f'  <bpmn:process id="{d.id}" isExecutable="false">']
    inc = {n.id: [] for n in d.nodes}
    outg = {n.id: [] for n in d.nodes}
    for e in d.edges:
        outg[e.src].append(e.id); inc[e.dst].append(e.id)
    for n in d.nodes:
        out.append(f'    <bpmn:{TAG[n.kind]} id="{n.id}" name="{escape(n.name, {chr(34): "&quot;"})}">')
        for i in inc[n.id]:
            out.append(f'      <bpmn:incoming>{i}</bpmn:incoming>')
        for o in outg[n.id]:
            out.append(f'      <bpmn:outgoing>{o}</bpmn:outgoing>')
        out.append(f'    </bpmn:{TAG[n.kind]}>')
    for e in d.edges:
        nm = f' name="{escape(e.label)}"' if e.label else ""
        out.append(f'    <bpmn:sequenceFlow id="{e.id}"{nm} sourceRef="{e.src}" targetRef="{e.dst}" />')
    out.append('  </bpmn:process>')
    out.append(f'  <bpmndi:BPMNDiagram id="Diagram_{d.id}">')
    out.append(f'    <bpmndi:BPMNPlane id="Plane_{d.id}" bpmnElement="{d.id}">')
    for n in d.nodes:
        x, y, w, h = n.box
        extra = ' isMarkerVisible="true"' if n.kind == "xor" else ""
        out.append(f'      <bpmndi:BPMNShape id="{n.id}_di" bpmnElement="{n.id}"{extra}>')
        out.append(f'        <dc:Bounds x="{x:g}" y="{y:g}" width="{w}" height="{h}" />')
        if n.kind != "task":
            lx = n.cx - 60; ly = n.cy + h / 2 + 4
            if n.label_at == "above":
                ly = n.cy - h / 2 - 31
            elif n.label_at == "aboveleft":
                lx = n.cx - 135; ly = n.cy - h / 2 - 31
            elif n.label_at == "belowleft":
                lx = n.cx - 135; ly = n.cy + h / 2 + 14
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
    for e in d.edges:
        pts = " ".join(f"{px:g},{py:g}" for px, py in e.points)
        s.append(f'<polyline points="{pts}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
        if e.label:
            (ax, ay), (bx, by) = e.points[0], e.points[1]
            s.append(f'<text x="{ax + (8 if bx != ax else 6):g}" y="{ay - 6 if by == ay else ay + 16:g}" '
                     f'font-size="12" font-weight="bold" fill="#8a1c1c">{escape(e.label)}</text>')
    for n in d.nodes:
        x, y, ww, hh = n.box
        if n.kind == "task":
            s.append(f'<rect x="{x:g}" y="{y:g}" width="{ww}" height="{hh}" rx="10" fill="#fff" stroke="#222" stroke-width="1.8"/>')
            ls = n.lines or (n.name,)
            top = n.cy - (len(ls) - 1) * 7 + 4
            for k, t in enumerate(ls):
                s.append(f'<text x="{n.cx:g}" y="{top + k * 14:g}" text-anchor="middle" font-size="11.5">{escape(t)}</text>')
        elif n.kind == "xor":
            s.append(f'<polygon points="{n.cx:g},{y:g} {x+ww:g},{n.cy:g} {n.cx:g},{y+hh:g} {x:g},{n.cy:g}" fill="#fff" stroke="#222" stroke-width="1.8"/>')
            s.append(f'<path d="M{n.cx-8:g},{n.cy-8:g} L{n.cx+8:g},{n.cy+8:g} M{n.cx+8:g},{n.cy-8:g} L{n.cx-8:g},{n.cy+8:g}" stroke="#222" stroke-width="2.4"/>')
            ls = n.lines or (n.name,)
            for k, t in enumerate(ls):
                ax, anchor = n.cx, "middle"
                if n.label_at == "above":
                    ty = y - 8 - (len(ls) - 1 - k) * 14
                elif n.label_at == "belowleft":
                    ax, anchor, ty = n.cx - 10, "end", y + hh + 28 + k * 14
                elif n.label_at == "aboveleft":
                    ax, anchor, ty = n.cx - 24, "end", y - 4 - (len(ls) - 1 - k) * 14
                else:
                    ty = y + hh + 16 + k * 14
                s.append(f'<text x="{ax:g}" y="{ty:g}" text-anchor="{anchor}" font-size="11.5">{escape(t)}</text>')
        else:
            sw = 1.8 if n.kind == "start" else 4.5
            s.append(f'<circle cx="{n.cx:g}" cy="{n.cy:g}" r="18" fill="#fff" stroke="#222" stroke-width="{sw}"/>')
            ls = n.lines or (n.name,)
            for k, t in enumerate(ls):
                ax, anchor = n.cx, "middle"
                if n.label_at == "above":
                    ty = y - 8 - (len(ls) - 1 - k) * 14
                elif n.label_at == "belowleft":
                    ax, anchor, ty = n.cx - 10, "end", y + hh + 28 + k * 14
                elif n.label_at == "aboveleft":
                    ax, anchor, ty = n.cx - 24, "end", y - 4 - (len(ls) - 1 - k) * 14
                else:
                    ty = y + hh + 16 + k * 14
                s.append(f'<text x="{ax:g}" y="{ty:g}" text-anchor="{anchor}" font-size="11.5">{escape(t)}</text>')
    s.append('</svg>')
    return "\n".join(s)
