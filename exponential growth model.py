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
import os

# Numerical values
lambda_value = 0.1
C0 = 10

# Time
time = np.linspace(0, 50, 200)

# Exponential tumor growth
tumor = C0 * np.exp(lambda_value * time)

# Create graphs folder automatically
os.makedirs("graphs", exist_ok=True)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(time, tumor, linewidth=2)

plt.xlabel("Time")
plt.ylabel("Tumor Size")
plt.title("Exponential Tumor Growth Model")
plt.grid(True)

# Save graph
plt.savefig("graphs/exponential_growth.png", dpi=300, bbox_inches="tight")

# Display graph
plt.show()