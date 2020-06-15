# Logistic Maps

![The Logistic Map](thumbnail.png "The Logistic Map")

This repository contains code to generate and visualize the [logistic
map](https://en.wikipedia.org/wiki/Logistic_map) using Python. It
depends on matplotlib and sympy. To use this software, simply edit the
`logistic_map` function in [logistic.py](). The standard equation is

``` python
x * (1 - x)
```

For compatibility, please ensure that any replacement function has a
peak on the interval `[0, 1]` with a value of ¼. To achieve this, you
can use the helper function [peak.py](), which uses SymPy to attempt to
solve for local extrema and returns their values. Even if it cannot find
a solution, e.g., for transcendental functions, it will plot your
function as `f.png`.

Results are stored to `logistic.npy`. If it exists, it will be read back
in, so the map can simply resume from previous iterations. If you change
the function or resolution, it is recommended that you delete this file.
