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

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')
lam = sp.symbols('lambda')
C = sp.Function('C')

ode = sp.Eq(C(t).diff(t), lam*C(t))
solution = sp.dsolve(ode)

print(solution)

# Numerical values for graph
lambda_value = 0.1
C0 = 10

time = np.linspace(0, 50, 100)
tumor = C0 * np.exp(lambda_value * time)

# Plot
plt.plot(time, tumor)
plt.xlabel("Time")
plt.ylabel("Tumor Size")
plt.title("Exponential Tumor Growth Model")
plt.grid(True)
plt.savefig("graphs/exponential_growth.png", dpi=300, bbox_inches="tight")
plt.show()
