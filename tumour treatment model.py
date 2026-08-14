import sympy as sp

t = sp.symbols('t')

Lam, xi, phi, varphi, upsilon = sp.symbols(
    'lambda xi phi varphi upsilon', positive=True
)

c = sp.Function('c')
K = sp.Function('K')
g = sp.Function('g')

ode1 = sp.Eq(
    c(t).diff(t),
    -Lam*c(t)*sp.log(c(t)/K(t)) - xi*c(t)
)

ode2 = sp.Eq(
    K(t).diff(t),
    phi*K(t)*c(t)*sp.Rational(2,3) - upsilon*K(t)*g(t)
)

print(ode1)
print(ode2)


import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.2
K = 100
C0 = 10
d = 0.1

# Time
time = np.linspace(0, 50, 200)

# Tumor growth with treatment
tumor = np.zeros_like(time)
tumor[0] = C0

for i in range(1, len(time)):
    dt = time[i] - time[i - 1]
    tumor[i] = tumor[i - 1] + dt * (
        r * tumor[i - 1] * (1 - tumor[i - 1] / K)
        - d * tumor[i - 1]
    )

# Plot
plt.figure()
plt.plot(time, tumor)
plt.xlabel("Time")
plt.ylabel("Tumor Size")
plt.title("Tumor Growth Under Treatment")
plt.grid(True)
plt.show()