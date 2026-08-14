import sympy as sp

t = sp.symbols('t')
phi, varphi = sp.symbols('phi varphi', positive=True)

c = sp.Function('c')
K = sp.Function('K')

ode = sp.Eq(
    sp.diff(K(t), t),
    phi*c(t) - varphi*K(t)*c(t)**(sp.Rational(2, 3))
)

print(ode)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.2
K0 = 100
A = 30
w = 0.1
C0 = 10

# Time
time = np.linspace(0, 50, 200)

# Dynamic carrying capacity
K = K0 + A * np.sin(w * time)

# Tumor growth
tumor = np.zeros_like(time)
tumor[0] = C0

for i in range(1, len(time)):
    dt = time[i] - time[i - 1]
    tumor[i] = tumor[i - 1] + dt * r * tumor[i - 1] * (
        1 - tumor[i - 1] / K[i]
    )

# Plot
plt.figure()
plt.plot(time, tumor)
plt.xlabel("Time")
plt.ylabel("Tumor Size")
plt.title("Dynamic Carrying Capacity Model")
plt.grid(True)
plt.savefig("dynamic capacity_growth.png", dpi=300, bbox_inches="tight")
plt.show()