import textwrap
# https://docs.python.org/3.10/library/textwrap.html#textwrap.wrap

textwrap.wrap(text, width=70)
# return list of linnes

textwrap.fill(text, width=70)
# paragraph, equal to "\n".join(wrap(text, ...))
