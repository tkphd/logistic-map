from sympy import diff, lambdify, pi, sin, solve
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np

f = x * (1 - x)
df = diff(f, x)

try:
    z = solve(df, x)

    for root in z:
        print("Extremum at ", root, ": value is ", f.subs(x, root))
except:
    print("Could not solve for the extrema")

f = lambdify(x, f)
xi = np.linspace(0, 1, 101, endpoint=True)
yi = f(xi)

plt.plot(xi, xi * (1 - xi), label="$x(1-x)$")
plt.plot(xi, yi, label="$\sin^2(\pi x)$")
plt.savefig("f.png", dpi=400, bbox_inches="tight")
