import sympy as sp
t = sp.symbols('t')
lam,k = sp.symbols('lambda k', positive = True)
c = sp.Function('c')
ode = sp.Eq(c(t).diff(t),-lam*c(t)*sp.log(c(t)/k))
print(ode)
solution = sp.dsolve(ode)
print(solution)


import numpy as np
import matplotlib.pyplot as plt

K = 100
C0 = 10
b = 0.1

time = np.linspace(0, 50, 100)

tumor = K * np.exp(np.log(C0 / K) * np.exp(-b * time))

print("Gompertz Growth Model")
print("Graph is being generated...")

plt.figure()
plt.plot(time, tumor)
plt.xlabel("Time")
plt.ylabel("Tumor Size")
plt.title("Gompertz Tumor Growth Model")
plt.grid(True)
plt.savefig("gompertz_growth.png", dpi=300, bbox_inches="tight")
plt.show()
