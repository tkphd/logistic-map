#!python
# -*- coding: utf-8 -*-

import numpy as np
from tqdm import tqdm

xyz = "mandelbrot.pts"

its = 50000 # iteration cap
plt = 64    # points to plot
cap = 20    # max allowed value


rres = 5000
ires = 2000

rmin = -2
rmax = -0.75

imin = -np.pi / 4
imax = np.pi / 4

def mandelbrot(z, c):
    return z * z + c

def iterate(c):
    z = c
    q = [c]

    # Iterate the Mandelbrot Set
    for i in range(its - plt):
        z = mandelbrot(z, c)
        if abs(z) > cap:
            break

    for i in range(plt):
        z = mandelbrot(z, c)
        if abs(z) > cap:
            q = []
            break
        else:
            q.append(z)

    return q

pts = []
N = 0

# Mandelbrot set
for cr in tqdm(np.linspace(rmin, rmax, rres+1, endpoint=True)):
    for ci in np.linspace(imin, imax, ires+1, endpoint=True):
        c = complex(cr, ci)
        q = iterate(c)

        # Record the points
        if len(q) != 0:
            pts.append(q)
            N += len(q) - 1

# Write PTS file header
fh = open(xyz, "w")
fh.write("{0}\n".format(N))

# Save the points
for p in pts:
    if len(p) > 0:
        c = p.pop(0)
        for z in p:
            fh.write("{0} {1} {2}\n".format(c.real, c.imag, abs(z)))

fh.close()
