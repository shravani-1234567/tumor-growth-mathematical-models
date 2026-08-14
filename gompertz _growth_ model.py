import sympy as sp
t = sp.symbols('t')
lam,k = sp.symbols('lambda k', positive = True)
c = sp.Function('c')
ode = sp.Eq(c(t).diff(t),-lam*c(t)*sp.log(c(t)/k))
print(ode)
solution = sp.dsolve(ode)
print(solution)
