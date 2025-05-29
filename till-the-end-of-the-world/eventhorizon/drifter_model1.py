import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters (enhanced for realistic collapse)
H0 = 9.2e9
H0_poor = 7.9e9       # Initial poor population (87% of 9.2B)
H0_rich = H0 - H0_poor       # Initial rich population (13% of 9.2B)
N0 = 10_000           # Initial drifter population
alpha = 0.008         # Adjusted downward for slower conversion
beta_p = 0.00004      # Poor infection rate (0.4% daily)
beta_r = 0.000004     # Rich infection rate (0.04% daily)
mu = 0.00003          # Natural mortality rate
delta = 0.0016        # Increased drifter mortality

# Time span (10 years for full collapse visualization)
t_span = (0, 10 * 365)

def model(t, y):
    H_p, H_r, N = y
    dH_pdt = -beta_p * N * H_p - mu * H_p
    dH_rdt = -beta_r * N * H_r - mu * H_r
    dNdt = alpha * (beta_p * H_p + beta_r * H_r) * N - delta * N
    return [dH_pdt, dH_rdt, dNdt]

# Solve with adaptive time stepping
sol = solve_ivp(
    model,
    t_span,
    y0=[H0_poor, H0_rich, N0],
    method="BDF",
    dense_output=True,
    rtol=1e-6,
    atol=1e-8
)

# Create smooth time points for plotting
t_plot = np.linspace(0, 3*365, 1000)  # First 3 years for detail
H_p, H_r, N = sol.sol(t_plot)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Top plot: Human populations (log scale)
ax1.semilogy(t_plot, H_p, label='Poor', color='#1f77b4', linewidth=2)
ax1.semilogy(t_plot, H_r, label='Rich', color='#ff7f0e', linewidth=2)
ax1.set_ylabel('Population (log scale)')
ax1.set_title('Human Population Dynamics')
ax1.grid(True, which="both", linestyle='--', alpha=0.7)
ax1.legend()

# Bottom plot: Drifter population (linear scale)
ax2.plot(t_plot, N, label='Drifters', color='#2ca02c', linewidth=2)
ax2.set_xlabel('Days since Emergence')
ax2.set_ylabel('Drifter Population')
ax2.set_title('Drifter Population Growth')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

# Add crisis timeline markers
crisis_days = [365, 730, 1095]  # 1, 2, 3 year marks
for day in crisis_days:
    ax1.axvline(day, color='gray', linestyle=':', alpha=0.5)
    ax2.axvline(day, color='gray', linestyle=':', alpha=0.5)

plt.tight_layout()

# Save and show plot
plt.savefig('population_dynamics.png', dpi=300, bbox_inches='tight')
plt.show()