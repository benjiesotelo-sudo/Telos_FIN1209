"""One measured layout for all Chapter 7 course charts.

Prices are data, not layout hints. Every OHLC label uses its real data
coordinate. Long sequences are paginated, never squeezed or downscaled.
This chapter-local renderer does not change the shared slide or chart kits.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
import math
import re

import chartkit as ck
import deckkit as dk
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
from matplotlib.textpath import TextPath

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
    if spec['owner']=='r3b' and spec['letter']=='LG':
        # Keep both crossing pairs intact rather than splitting the second
        # pair at a page boundary.
        return ((0,0,3),(0,3,6),(0,6,9),(0,9,11),(0,11,14))
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


def _segment_box(start, end, box):
    """Exact line/rectangle intersection, not the line's enclosing box."""
    x,y=start
    dx,dy=end[0]-x,end[1]-y
    lower,upper=0.,1.
    for p,q in ((-dx,x-box.x0),(dx,box.x1-x),(-dy,y-box.y0),(dy,box.y1-y)):
        if abs(p)<1e-12:
            if q<0:
                return False
        elif p<0:
            lower=max(lower,q/p)
        else:
            upper=min(upper,q/p)
        if lower>upper:
            return False
    return True


def _segment_distance(start, end, point):
    dx,dy=end[0]-start[0],end[1]-start[1]
    length=dx*dx+dy*dy
    t=max(0,min(1,((point[0]-start[0])*dx+(point[1]-start[1])*dy)/length)) if length else 0
    return math.hypot(point[0]-start[0]-t*dx,point[1]-start[1]-t*dy)


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
        ink = TextPath((0,0),label.get_text(),size=label.get_fontsize(),
                       prop=label.get_fontproperties()).get_extents().height*100/72
        assert ink >= 14, f'Glyph ink below safe 100 dpi threshold: {label.get_text()}: {ink:.2f}px'
    return boxes


def _marks(fig, targets, specs, boxes, segments, groups):
    """Compute exact data-anchored rings and touching, collision-free badges."""
    ring_radius, badge_r = .048 * ck.DPI, .14 * ck.DPI
    circles = []
    result = []
    leaders = []
    future = [(targets[tuple(s['target'])], 0 if tuple(s['target']) in groups else ring_radius) for s in specs if tuple(s['target']) in targets]
    # Reserve a middle-of-bar badge before its high/low neighbours. Greedy
    # extreme-first placement can otherwise close both escape lanes.
    ordered=sorted(specs,key=lambda spec: 0 if spec['target'][2] in ('range','group') else 1)
    for spec in ordered:
        target = tuple(spec['target'])
        if target not in targets:
            continue
        cx, cy = targets[target]
        radius=0 if target in groups else ring_radius
        assert not any(_circle_box(cx, cy, radius, b) for b in boxes), (spec, 'ring crosses text')
        found = None
        # Try direct contact first. Firstmate's 012 instruction permits the
        # nearest clear badge joined to its ring by a same-colour hairline.
        for extra in range(0, int(2*ck.DPI), 4):
            distance = radius + badge_r + extra
            for angle in range(0, 360, 5):
                theta = math.radians(angle)
                ux,uy=math.cos(theta),math.sin(theta)
                bx, by = cx + distance * ux, cy + distance * uy
                if not (badge_r + 2 <= bx <= fig.bbox.width - badge_r - 2 and badge_r + 2 <= by <= fig.bbox.height - badge_r - 2):
                    continue
                if any(_circle_box(bx, by, badge_r + 1, b) for b in boxes + segments):
                    continue
                if any(math.hypot(bx - x, by - y) < badge_r + r + 1 for ((x,y),r) in circles):
                    continue
                if any(math.hypot(bx - x, by - y) < badge_r + r - .01 for ((x,y),r) in future):
                    continue
                start=(cx+radius*ux,cy+radius*uy)
                end=(bx-badge_r*ux,by-badge_r*uy)
                if extra and any(_segment_box(start,end,b.padded(1)) for b in boxes+segments):
                    continue
                if extra and any(_segment_distance(start,end,point)<r+1 for point,r in circles):
                    continue
                if extra and any(point != (cx,cy) and _segment_distance(start,end,point)<r+1 for point,r in future):
                    continue
                found=(bx,by,start,end,extra)
                break
            if found:
                break
        if found is None:
            raise AssertionError(f'No touching badge position for {spec}')
        bx,by,start,end,extra=found
        if extra:
            color='#'+str(dk.MARK_COLORS[spec['color']])
            fig.add_artist(Line2D((start[0]/ck.DPI,end[0]/ck.DPI),
                                  (start[1]/ck.DPI,end[1]/ck.DPI),
                                  transform=fig.dpi_scale_trans,color=color,lw=1))
            leaders.append((spec['number'],extra/ck.DPI))
        circles.extend((((cx, cy), radius), ((bx, by), badge_r)))
        bounds=groups.get(target,(cx-radius,cy-radius,cx+radius,cy+radius))
        result.append(dk.Mark(spec['number'], 'box' if target in groups else 'circle',
                              bounds[0]/fig.bbox.width, 1-bounds[3]/fig.bbox.height,
                              bounds[2]/fig.bbox.width, 1-bounds[1]/fig.bbox.height,
                              color=spec['color'], at=(bx/fig.bbox.width, 1-by/fig.bbox.height), size=.28))
    fig.chart_leaders=tuple(leaders)
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
    labels, segments, targets, levels, tips, groups = [], [], {}, [], [], {}
    def text(x, y, value, *, ha='center', va='center', color=ck.INK):
        artist = fig.text(x/WIDTH, y/HEIGHT, value, ha=ha, va=va,
                          fontsize=FONT, color=color, fontweight='bold',
                          fontfamily=dk.BODY_FONT)
        labels.append(artist)
        return artist

    def semantic_labels(pane,index):
        result=[]
        for note in pane.notes:
            if note.x!=index or not note.label:
                continue
            value=note.label.replace('\n',' ')
            # These old price callouts are now the four tick-anchored labels.
            if re.match(r'^(?:(?:next|first|second|middle|wide)\s+)?[OHLC]\s+\d',value,re.I):
                continue
            if re.match(r'^(?:open|high|low|close|prior low)\s+\d',value,re.I):
                continue
            result.append(value)
        return result
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
        if title:
            text(WIDTH/2,3.64,title,color=ck.GREEN_DEEP)
        note = cell.note.replace('\n',' ')
        if note:
            text(WIDTH/2,3.32,note,color=ck.MUTED)
        has_volume = any(p.columns for p in cell.panes) and any(p.bars or p.line for p in cell.panes)
        price_bottom = 1.55 if has_volume else 1.0
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
                        text(x,y_inches(y)+.19,f'{y:g}',va='bottom')
                for target,group in spec.get('groups',{}).items():
                    ci,first,last=group
                    if pane.bars and ci==cell_index and start<=first<=last<end:
                        members=pane.bars[first:last+1]
                        bottom=min(b.low for b in members)
                        top=max(b.high for b in members)
                        bounds=((x_inches(first)-1.45)*ck.DPI,(y_inches(bottom)-.45)*ck.DPI,
                                (x_inches(last)+1.45)*ck.DPI,(y_inches(top)+.45)*ck.DPI)
                        groups[target]=bounds
                        targets[target]=(bounds[2],(bounds[1]+bounds[3])/2)
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
                        semantic=semantic_labels(pane,index)
                        caption=f'Bar {index+1}' + (': '+'; '.join(semantic) if semantic else '')
                        artist=text(x,.39,caption,color=ck.MUTED)
                        fig.canvas.draw()
                        box=artist.get_window_extent(fig.canvas.get_renderer())
                        if box.x1>fig.bbox.width-3:
                            artist.set_position(((fig.bbox.width-3)/fig.bbox.width,.39/HEIGHT))
                            artist.set_ha('right')
                        elif box.x0<3:
                            artist.set_position((3/fig.bbox.width,.39/HEIGHT))
                            artist.set_ha('left')
                elif pane.line:
                    semantic=[f'Bar {i+1}: {label}' for i in range(start,end) for label in semantic_labels(pane,i)]
                    for volume in cell.panes:
                        if volume.columns:
                            semantic.extend(f'Bar {i+1}: {label}' for i,label in volume.tags if not re.match(r'^[0-9.]+m$',label))
                    if semantic:
                        text(WIDTH/2,.39,'; '.join(semantic),color=ck.MUTED)
            elif pane.columns:
                bottom,top = (.60,.80) if has_volume else (.72,2.7)
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
        for bounds in groups.values():
            x0,y0,x1,y1=bounds
            edges=(((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0)))
            assert not any(_segment_box(a,b,box) for a,b in edges for box in boxes), 'group box crosses text'
        marks=_marks(fig,targets,_target_specs(key,spec),boxes,segments,groups)
    except AssertionError as error:
        plt.close(fig)
        raise AssertionError(f'{key} page {page+1}: {error}') from error
    plt.close(fig)
    fig.chart_targets=targets
    return fig,marks


def draw(path, *, key, page=0, display_font=None):
    fig,_marks=layout(key,page)
    fig.savefig(path,dpi=ck.DPI,facecolor=ck.WHITE)
    return path


def audit_pptx(path, charts_dir):
    """Refuse a deck that scales the validated artwork below its contract."""
    import hashlib
    from pathlib import Path
    from pptx import Presentation
    from charts_chapter07 import DATA
    assets={hashlib.sha256((Path(charts_dir)/f'chart-{key}-{page}.png').read_bytes()).hexdigest(): (key,page)
            for key,spec in DATA.items() for page in range(len(page_specs(spec)))}
    presentation=Presentation(path)
    found=set()
    for page,slide in enumerate(presentation.slides,1):
        for shape in slide.shapes:
            if shape.shape_type != 13:
                continue
            key=assets.get(hashlib.sha256(shape.image.blob).hexdigest())
            if key is None:
                continue
            found.add(key)
            scale=shape.width/914400/WIDTH
            assert shape.width >= .55*presentation.slide_width, f'Slide {page}: chart is too narrow'
            assert scale >= .999, f'Slide {page}: chart text scaled below validated size'
    assert found==set(assets.values()), 'Missing chart pages in rendered deck'
