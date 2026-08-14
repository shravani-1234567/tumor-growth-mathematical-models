import sympy as sp
#define variables
t = sp.symbols('t')
lam = sp.symbols('lambda',positive=True)
c = sp.Function('c')
# differential equation
ode = sp.Eq(c(t).diff(t), lam*c(t))
#solve
solution = sp.dsolve(ode)
print(solution) 
