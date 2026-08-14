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