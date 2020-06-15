#!python
#-*- coding: utf-8 -*-

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from os.path import isfile
plt.style.use('dark_background')

def logistic_map(r, x):
    # Any function with roots at 0 and 1, and a maximum
    # in-between with a value of 0.25
    return r * x * (1 - x)

grw_res = 12500 # points on [0,4]
its = 625 # points to plot
pkl_name = "logistic"
xmin = 1
xmax = 4

A = []

if isfile(pkl_name + ".npy"):
    A = np.load(pkl_name + ".npy")
else:
    A = np.zeros((grw_res, its))
    A[:, -1] = 0.5

plt.figure(figsize=(36, 9))

for i in tqdm(np.arange(1, grw_res)):
    r = xmin + ((xmax-xmin) * i) / grw_res

    for n in range(10):
        A[i,0] = logistic_map(r, A[i,-1])

        for j in np.arange(1, its):
            A[i,j] = logistic_map(r, A[i,j-1])

    x = r * np.ones(its)
    plt.scatter(x, A[i,:], s=0.04, c="white", marker=",", alpha=0.02)

plt.xlim([xmin, xmax])
plt.ylim([0,1])
plt.savefig("logistic.png", dpi=400, bbox_inches="tight")

np.save(pkl_name, A)
