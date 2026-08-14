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