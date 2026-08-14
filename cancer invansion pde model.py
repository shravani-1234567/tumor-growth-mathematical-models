import sympy as sp

x, y, t = sp.symbols('x y t')

Dc, rho, delta, gamma = sp.symbols(
    'Dc rho delta gamma', positive=True
)

c = sp.Function('c')(x, y, t)
m = sp.Function('m')(x, y, t)
v = sp.Function('v')(x, y, t)

pde1 = sp.Eq(
    sp.diff(c, t),
    Dc * (
        sp.diff((1 - v) * sp.diff(c, x), x)
        + sp.diff((1 - v) * sp.diff(c, y), y)
    )
    + rho * c * (1 - c)
)

pde2 = sp.Eq(
    sp.diff(m, t),
    sp.diff(m, x, 2) + sp.diff(m, y, 2)
    + delta * (c - m)
)

pde3 = sp.Eq(
    sp.diff(v, t),
    v * (1 - v) - gamma * m * v
)

print(pde1)
print(pde2)
print(pde3)