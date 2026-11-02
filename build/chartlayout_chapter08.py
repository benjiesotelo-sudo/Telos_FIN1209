"""Chapter 8 reuses Chapter 7's measured chart layout unchanged.

Importing this module points that layout at Chapter 8's chart data, content
and figure sizes, then re-exports the pieces a content file uses. Nothing is
copied: badge placement, label lanes and the machine checks are Chapter 7's.
"""
import chartlayout_chapter07 as _layout

_layout.CHAPTER_DIR = 'chapter-08'
_layout.DATA_MODULE = 'charts_chapter08'
_layout.CONTENT_MODULE = 'content_chapter08'
# Chapter 7's layout caches nothing before this point, but clear it anyway.
_layout.layout.cache_clear()

from chartlayout_chapter07 import (CourseCheck, CourseFigureCheck, WidePair,  # noqa: E402,F401
                                   artwork, audit_pptx, book_crop, chart_slides,
                                   course_chart, course_slide_renderer,
                                   expand_chart_pages)

# Chapter 8's checks give their figure about half the slide (Chapter 7's column is 3.3 inches).
_layout.FIGURE_CHECK_W = 4.6

# One typeface for every answer line in this chapter: the plain check's answer
# slide would otherwise set its answer in Courier and the figure check's in Arial.
import deckkit as _dk  # noqa: E402
_dk.MONO_FONT = _dk.BODY_FONT
