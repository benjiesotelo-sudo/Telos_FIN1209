# Chapter 7 foundation

This folder holds the foundation scaffold for Lim (2016), Chapter 7, “Bar
Chart Analysis”. The approved source map and outline are in the instructor's
plan folder outside the public repository.

The committed build is the placeholder teaching deck. The textbook figures
are copyrighted and are never committed. The 39 extracted figures live in
`assets/figures/` only on the artwork build machine.

Build the committed foundation deck:

```
.venv/bin/python build/build_chapter7.py
```

Build the artwork deck outside the repository:

```
.venv/bin/python build/build_chapter7.py \
    --with-figures \
    --out ~/FIN1209-Chapter-07-with-figures-and-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-07-with-figures-and-charts.pptx
```

The full deck is built only after the outline and the three sample ideas are
approved. This scaffold includes the bearish and bullish key reversal sample,
the exhaustion versus pin bar comparison, and a separate key reversal check
and answer sequence.
