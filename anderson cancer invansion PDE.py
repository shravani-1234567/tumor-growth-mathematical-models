import sympy as sp

x, y, t = sp.symbols('x y t')

Dc, gamma, alpha, beta, eta = sp.symbols(
    'Dc gamma alpha beta eta', positive=True
)

c = sp.Function('c')(x, y, t)
m = sp.Function('m')(x, y, t)
v = sp.Function('v')(x, y, t)

pde1 = sp.Eq(
    sp.diff(c, t),
    Dc * (sp.diff(c, x, 2) + sp.diff(c, y, 2))
    - gamma * (
        sp.diff(c * sp.diff(v, x), x)
        + sp.diff(c * sp.diff(v, y), y)
    )
)

pde2 = sp.Eq(
    sp.diff(m, t),
    sp.diff(m, x, 2) + sp.diff(m, y, 2)
    + alpha * c - beta * m
)

pde3 = sp.Eq(
    sp.diff(v, t),
    -eta * m * v
)

print(pde1)
print(pde2)
print(pde3)


import numpy as np
import matplotlib.pyplot as plt

# Spatial grid
x_vals = np.linspace(0, 10, 150)
y_vals = np.linspace(0, 10, 150)

X, Y = np.meshgrid(x_vals, y_vals)

# Initial cancer-cell concentration
c0 = np.exp(-((X - 5)*2 + (Y - 5)*2) / 2)

# Create a separate figure
fig = plt.figure(figsize=(8, 6))

plt.imshow(
    c0,
    extent=[0, 10, 0, 10],
    origin="lower",
    aspect="auto"
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Cancer Invasion PDE Model")

plt.colorbar(label="Cancer Cell Concentration")

# Save ONLY this graph
plt.savefig(
    "cancer_invasion.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)