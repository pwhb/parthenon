import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
H0_poor = 7.9e9  # 87% of 9.2B
H0_rich = 1.3e9  # 13% of 9.2B
N0 = 10_000
alpha = 0.01
beta_p = 0.00005  # 0.5% daily for poor
beta_r = 0.000005  # 0.05% daily for rich
mu = 0.00003      # Natural human mortality
delta = 0.0014    # Drifter mortality (0.14%/day)

# Time span (days from 2041–2047)
t_span = (0, 6*365)

# Differential equations
def model(t, y):
    H_p, H_r, N = y
    dH_pdt = -beta_p * N * H_p - mu * H_p
    dH_rdt = -beta_r * N * H_r - mu * H_r
    dNdt = alpha * (beta_p * H_p + beta_r * H_r) * N - delta * N
    return [dH_pdt, dH_rdt, dNdt]

# Initial conditions
y0 = [H0_poor, H0_rich, N0]

# Solve ODE
sol = solve_ivp(model, t_span, y0, max_step=1)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(sol.t, sol.y[0], label="Poor Population")
plt.plot(sol.t, sol.y[1], label="Rich Population")
plt.plot(sol.t, sol.y[2], label="Drifters", linestyle="--")
plt.yscale("log")
plt.xlabel("Days since 2041")
plt.ylabel("Population")
plt.title("Human-Drifter Dynamics")
plt.legend()
plt.grid()
plt.show()