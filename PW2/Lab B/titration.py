"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
V, pH = np.loadtxt('titration.csv', delimiter=',', skiprows=1, unpack=True)

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
eq_index = np.argmax(slope)
eq_vol = V[eq_index]
print(f"Equivalence point volume: {eq_vol} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(V, pH, 'b-', label='pH vs Volume')
ax1.axvline(x=eq_vol, color='r', linestyle='--', label=f'Equivalence Point: {eq_vol:.2f} mL')
ax1.set_xlabel('Volume of Base Added (mL)')
ax1.set_ylabel('pH')
ax1.legend()
ax1.grid(True)

ax2.plot(V, slope, 'g-', label='Slope vs Volume')
ax2.axvline(x=eq_vol, color='r', linestyle='--', label=f'Equivalence Point: {eq_vol:.2f} mL')
ax2.set_xlabel('Volume of Base Added (mL)')
ax2.set_ylabel('Slope')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("titration.png")
