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