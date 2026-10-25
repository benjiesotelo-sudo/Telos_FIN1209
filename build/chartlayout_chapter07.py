"""One measured layout for all Chapter 7 course charts.

Prices are data, not layout hints. Every OHLC label uses its real data
coordinate. Long sequences are paginated, never squeezed or downscaled.
This chapter-local renderer does not change the shared slide or chart kits.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
import math
import textwrap

import chartkit as ck
import deckkit as dk
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.transforms import Bbox

WIDTH, HEIGHT = ck.FIG_W, ck.FIG_H
FONT = 16.5
CAPTION = 'Prices and volume are invented for teaching.'


@dataclass
class CourseChart(dk.Chart):
    asset: str = ''
    page: int = 0
    display_letter: str = ''

    @property
    def filename(self):
        return f'chart-{self.asset}-{self.page}.png'

    @property
    def credit(self):
        return dk.chart_credit(self.display_letter)

    @property
    def name(self):
        return f'Chart {self.display_letter}'


def course_chart(asset, **kwargs):
    """Keep displayed owner letters while namespacing conflicting assets."""
    return CourseChart(asset=asset, display_letter=kwargs['letter'], **kwargs)


def page_specs(spec):
    if spec['special']:
        return ((0, 0, 0),)
    result = []
    for cell_index, cell in enumerate(spec['items']):
        count = max(max(len(p.bars), len(p.line), len(p.columns), 1) for p in cell.panes)
        # Three OHLC bars leave room for both side labels plus a level lane.
        step = 3 if any(p.bars for p in cell.panes) else count
        result.extend((cell_index, start, min(count, start + step)) for start in range(0, count, step))
    return tuple(result)


def artwork(data):
    return tuple(ck.ChartArt(letter=f'{key}-{page}', draw=draw,
                             kwargs=dict(key=key, page=page))
                 for key, spec in data.items()
                 for page in range(len(page_specs(spec))))


def expand_chart_pages(chapter):
    """Make the extra space explicit in the deck's slide sequence."""
    from charts_chapter07 import DATA
    serial = 0
    def expand(slides):
        nonlocal serial
        result = []
        for slide in slides:
            if isinstance(slide, CourseChart):
                for page in range(len(page_specs(DATA[slide.asset]))):
                    internal = chr(65 + serial // 26) + chr(65 + serial % 26)
                    serial += 1
                    result.append(replace(slide, page=page, letter=internal,
                                          notes=slide.notes or (slide.shows,),
                                          marks=layout(slide.asset, page)[1]))
            else:
                result.append(slide)
        return tuple(result)
    openers = expand(chapter.openers or ())
    sections = tuple(replace(section, slides=expand(section.slides)) for section in chapter.sections)
    return replace(chapter, openers=openers, sections=sections, closing=expand(chapter.closing))


def _overlaps(a, b):
    return a.x0 < b.x1 and b.x0 < a.x1 and a.y0 < b.y1 and b.y0 < a.y1


def _circle_box(cx, cy, radius, box):
    x = max(box.x0, min(cx, box.x1))
    y = max(box.y0, min(cy, box.y1))
    return math.hypot(x - cx, y - cy) < radius


def _assert_layout(fig, labels, bars):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = [t.get_window_extent(renderer).padded(2) for t in labels]
    for i, (label, box) in enumerate(zip(labels, boxes)):
        assert fig.bbox.contains(box.x0, box.y0) and fig.bbox.contains(box.x1, box.y1), (
            f'label outside chart: {label.get_text()}')
        assert not any(_overlaps(box, b) for b in boxes[:i]), (
            f'label overlap: {label.get_text()}')
        assert not any(_overlaps(box, line) for line in bars), (
            f'label crosses OHLC bar: {label.get_text()}')
        # Arial capitals at 16.5 pt have >=15 px of true ink at 100 dpi.
        # A rendered-PPTX raster audit also measures every actual label.
        assert label.get_fontsize() >= FONT
    return boxes


def _marks(fig, targets, specs, boxes, segments):
    """Compute exact data-anchored rings and touching, collision-free badges."""
    radius, badge_r = .048 * ck.DPI, .14 * ck.DPI
    circles = []
    result = []
    future = [(targets[tuple(s['target'])], radius) for s in specs if tuple(s['target']) in targets]
    for spec in specs:
        target = tuple(spec['target'])
        if target not in targets:
            continue
        cx, cy = targets[target]
        assert not any(_circle_box(cx, cy, radius, b) for b in boxes), (spec, 'ring crosses text')
        distance = radius + badge_r
        for angle in range(0, 360, 5):
            theta = math.radians(angle)
            bx, by = cx + distance * math.cos(theta), cy + distance * math.sin(theta)
            if not (badge_r + 2 <= bx <= fig.bbox.width - badge_r - 2 and badge_r + 2 <= by <= fig.bbox.height - badge_r - 2):
                continue
            if any(_circle_box(bx, by, badge_r + 1, b) for b in boxes + segments):
                continue
            if any(math.hypot(bx - x, by - y) < badge_r + r + 1 for ((x,y),r) in circles):
                continue
            if any(math.hypot(bx - x, by - y) < badge_r + r - .01 for ((x,y),r) in future):
                continue
            break
        else:
            raise AssertionError(f'No touching badge position for {spec}')
        circles.extend((((cx, cy), radius), ((bx, by), badge_r)))
        result.append(dk.Mark(spec['number'], 'circle',
                              (cx-radius)/fig.bbox.width, 1-(cy+radius)/fig.bbox.height,
                              (cx+radius)/fig.bbox.width, 1-(cy-radius)/fig.bbox.height,
                              color=spec['color'], at=(bx/fig.bbox.width, 1-by/fig.bbox.height), size=.28))
    return tuple(result)


def _target_specs(key, spec):
    # Explicit semantic anchors, independent of artwork dimensions.
    # The remaining entries are imported from the owners' marked drawings.
    return spec.get('targets', ())


@lru_cache(maxsize=128)
def layout(key, page=0):
    from charts_chapter07 import DATA
    spec = DATA[key]
    fig = plt.figure(figsize=(WIDTH, HEIGHT), dpi=ck.DPI)
    labels, segments, targets, levels, tips = [], [], {}, [], []
    def text(x, y, value, *, ha='center', va='center', color=ck.INK):
        artist = fig.text(x/WIDTH, y/HEIGHT, value, ha=ha, va=va,
                          fontsize=FONT, color=color, fontweight='bold',
                          fontfamily=dk.BODY_FONT)
        labels.append(artist)
        return artist
    def line(ax, x, y, **kwargs):
        artist, = ax.plot(x, y, **kwargs)
        return artist
    if spec['special'] == 'sentiment':
        for i, (trend, formation, result) in enumerate((
                ('Uptrend +4.0%', 'Bullish formation +2.0%', 'CONTINUATION'),
                ('Uptrend +4.0%', 'Bearish formation -2.0%', 'POTENTIAL REVERSAL'),
                ('Downtrend -4.0%', 'Bullish formation +2.0%', 'POTENTIAL REVERSAL'),
                ('Downtrend -4.0%', 'Bearish formation -2.0%', 'CONTINUATION'))):
            x, y = (3 if i%2==0 else 8.5), (2.9 if i<2 else 1.35)
            text(x,y+.45,trend, color=ck.GREEN_DEEP)
            text(x,y+.12,formation, color=ck.GREEN_DEEP)
            text(x,y-.35,result, color=ck.GOLD if 'REVERSAL' in result else ck.GREEN_DEEP)
            dot=Circle((x-2.2,y-.35),.025,transform=fig.dpi_scale_trans,color=ck.GREEN)
            fig.add_artist(dot)
            targets[0,i,'case']=((x-2.2)*ck.DPI,(y-.35)*ck.DPI)
    elif spec['special'] == 'characteristics':
        for y, number, title, meaning in ((2.8,'7','BRR','real body ÷ total range'),
                (1.35,'8','Angular symmetry and momentum','the angle and momentum change')):
            text(.5,y,number, color=ck.GOLD)
            text(1,y+.22,title,ha='left',color=ck.GREEN_DEEP)
            text(1,y-.22,meaning,ha='left',color=ck.MUTED)
    else:
        cell_index, start, end = page_specs(spec)[page]
        cell = spec['items'][cell_index]
        title = cell.name.replace('\n',' ')
        text(WIDTH/2,3.64,title,color=ck.GREEN_DEEP)
        note = cell.note.replace('\n',' ')
        if note:
            text(WIDTH/2,3.32,note,color=ck.MUTED)
        has_volume = any(p.columns for p in cell.panes) and any(p.bars or p.line for p in cell.panes)
        price_bottom = 1.65 if has_volume else 1.0
        price_top = 2.72
        left = 3.6 if any(p.strokes for p in cell.panes) else 2.1
        right = WIDTH - 1.5
        count = end-start
        xs = [left + (right-left) * i/max(1,count-1) for i in range(count)] if count>1 else [WIDTH/2]
        for pane_index, pane in enumerate(cell.panes):
            if pane.bars or pane.line:
                values = [v for b in pane.bars for v in (b.open,b.high,b.low,b.close)] + list(pane.line)
                values += [p[1] for s in pane.strokes for p in s.points]
                lo, hi = min(values),max(values)
                span = hi-lo or 1
                axis = fig.add_axes([0,price_bottom/HEIGHT,1,(price_top-price_bottom)/HEIGHT])
                axis.set_axis_off()
                axis.set_xlim(0,WIDTH)
                axis.set_ylim(lo,hi)
                def y_inches(y):
                    return price_bottom + (y-lo)/span*(price_top-price_bottom)
                def x_inches(x):
                    if count == 1:
                        return xs[0]
                    return xs[0]+(x-start)*(xs[-1]-xs[0])/(count-1)
                for index in range(start,end):
                    x=xs[index-start]
                    if pane.bars:
                        b=pane.bars[index]
                        for xx,yy in (((x,x),(b.low,b.high)),((x-.17,x),(b.open,b.open)),((x,x+.17),(b.close,b.close))):
                            artist=line(axis,xx,yy,color=ck.INK,lw=2.4,clip_on=False)
                            segments.append(artist.get_window_extent().padded(2))
                        text(x-.50,y_inches(b.open),f'O {b.open:.2f}',ha='right')
                        text(x+.50,y_inches(b.close),f'C {b.close:.2f}',ha='left')
                        tips.append((text(x,y_inches(b.high)+.19,f'H {b.high:.2f}',va='bottom'),1))
                        tips.append((text(x,y_inches(b.low)-.17,f'L {b.low:.2f}',va='top'),-1))
                        for name,xx,yy in (('open',x-.17,b.open),('high',x,b.high),('low',x,b.low),('close',x+.17,b.close),('range',x,(b.low+b.high)/2)):
                            targets[cell_index,index,name] = (xx*ck.DPI,y_inches(yy)*ck.DPI)
                    else:
                        y=pane.line[index]
                        targets[cell_index,index,'line']=(x*ck.DPI,y_inches(y)*ck.DPI)
                if pane.line:
                    line(axis,xs,pane.line[start:end],color=ck.INK,lw=2.4)
                for stroke in pane.strokes:
                    # Clip long sequences at page boundaries, preserving the
                    # original level value and global period numbering.
                    points = [(x_inches(x),y) for x,y in stroke.points]
                    if len({y for _,y in points}) == 1:
                        value=points[0][1]
                        line(axis,(.12,WIDTH-.2),(value,value),color=ck.MUTED,lw=.8,ls=(0,(4,4)),zorder=0)
                        for index,x in zip(range(start,end),xs):
                            targets[cell_index,index,'level:'+str(value)] = (x*ck.DPI,y_inches(value)*ck.DPI)
                        if stroke.label:
                            artist=text(.12,y_inches(value)+.06,stroke.label.replace('\n',' '),ha='left',va='bottom',color=ck.MUTED)
                            levels.append(artist)
                    else:
                        line(axis,[p[0] for p in points],[p[1] for p in points],color=ck.MUTED,lw=1,ls='--')
                if pane.bars:
                    for index,x in zip(range(start,end),xs):
                        text(x,.39,f'Bar {index+1}',color=ck.MUTED)
            elif pane.columns:
                bottom,top = (.60,.90) if has_volume else (.72,2.7)
                cols=pane.columns[start:end]
                lo,hi=min(0,min(cols)),max(cols)
                span=hi-lo or 1
                ax=fig.add_axes([0,bottom/HEIGHT,1,(top-bottom)/HEIGHT])
                ax.set_axis_off();ax.set_xlim(0,WIDTH);ax.set_ylim(lo,hi)
                ax.bar(xs,cols,width=.23,color=ck.GREEN)
                for index,x,value in zip(range(start,end),xs,cols):
                    y=bottom+(value-lo)/span*(top-bottom)
                    label=f'{value:g}m' if has_volume else f'{value:g}'
                    text(x,y+.07,label,va='bottom',color=ck.GREEN_DEEP)
                    targets[cell_index,index,'volume']=(x*ck.DPI,(bottom+(value/2-lo)/span*(top-bottom))*ck.DPI)
    text(WIDTH/2,.02,CAPTION,color=ck.MUTED,va='bottom')
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    for artist,direction in tips:
        x,y=artist.get_position()
        for pixels in range(int(.65*ck.DPI)):
            artist.set_position((x,y+direction*pixels/fig.bbox.height))
            box=artist.get_window_extent(renderer).padded(2)
            others=[t.get_window_extent(renderer).padded(2) for t in labels if t is not artist and t not in levels]
            if not any(_overlaps(box,b) for b in others+segments):
                break
    # Far-left level labels may advance upward, never horizontally away
    # from their level's left end. Actual renderer boxes determine the lane.
    for artist in levels:
        x,y=artist.get_position()
        for pixels in range(int(HEIGHT*ck.DPI)):
            artist.set_position((x,y+pixels/fig.bbox.height))
            box=artist.get_window_extent(renderer).padded(2)
            others=[t.get_window_extent(renderer).padded(2) for t in labels if t is not artist]
            if box.y1 < 3.15*ck.DPI and not any(_overlaps(box,b) for b in others+segments):
                break
        else:
            raise AssertionError(f'{key}: no level caption lane: {artist.get_text()}')
    try:
        boxes=_assert_layout(fig,labels,segments)
        marks=_marks(fig,targets,_target_specs(key,spec),boxes,segments)
    except AssertionError as error:
        plt.close(fig)
        raise AssertionError(f'{key} page {page+1}: {error}') from error
    plt.close(fig)
    return fig,marks


def draw(path, *, key, page=0, display_font=None):
    fig,_marks=layout(key,page)
    fig.savefig(path,dpi=ck.DPI,facecolor=ck.WHITE)
    return path
