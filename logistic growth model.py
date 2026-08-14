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


import numpy as np
import matplotlib.pyplot as plt

# Numerical values
r = 0.3
K = 100
C0 = 10

time = np.linspace(0, 50, 100)

# Logistic growth solution
tumor = K / (1 + ((K - C0) / C0) * np.exp(-r * time))

# Plot
plt.plot(time, tumor)
plt.xlabel("Time")
plt.ylabel("Tumor Size")
plt.title("Logistic Tumor Growth Model")
plt.grid(True)
plt.savefig("logistic_growth.png", dpi=300, bbox_inches="tight")
plt.show()
