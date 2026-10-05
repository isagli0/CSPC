"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t, y = np.loadtxt('freefall.csv', delimiter=',', skiprows=1, unpack=True)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy? - mean acceleration is not close: it came out as -8.58 m/s^2, which gives 12.5% error with std of 28.72 m/s^2.
#                                                                           it is very noisy as the position had some noise, which got even worse after differentiation.
v = np.gradient(y, t)
a = np.gradient(v, t)
print(f"mean acceleration: {np.mean(a):.2f} m/s^2")
print(f"standard deviation of acceleration: {np.std(a):.2f} m/s^2")


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]
print(f"standard deviation of difference between position and recovered position: {np.std(y - y_recovered):.2f} m") #the deviation is 0.32 m, which is a good sign, as it is much less than 1 m.
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 18), sharex=True)
ax1.plot(t, y, label="Measured Position")
ax1.plot(t, y_recovered, label="Recovered Position", linestyle='--')
ax1.set_ylabel("Position (m)")
ax1.legend()

ax2.plot(t, v, label="Measured Velocity")
ax2.plot(t, v_recovered, label="Recovered Velocity", linestyle='--')
ax2.set_ylabel("Velocity (m/s)")
ax2.legend()

ax3.plot(t, a, label="Measured Acceleration")
ax3.plot(t, np.full_like(t, -9.81), label="True Acceleration", linestyle=':')
ax3.plot(t, np.full_like(t, np.std(a)), label="+1 Standard Deviation of Acceleration ", linestyle=':')
ax3.plot(t, np.full_like(t, -np.std(a)), label="-1 Standard Deviation of Acceleration", linestyle=':')
ax3.set_ylabel("Acceleration (m/s^2)")
ax3.set_xlabel("Time (s)")
ax3.legend()
plt.tight_layout()
plt.savefig("motion.png")

t,x,y = np.loadtxt('trajectory.csv', delimiter=',', skiprows=1, unpack=True)
v_x = np.gradient(x, t)
v_y = np.gradient(y, t)
v = np.sqrt(v_x**2 + v_y**2)

fig, (ax1) = plt.subplots(1, 1, figsize=(10, 6))
ax1.plot(x,y, label="Trajectory")
ax1.set_ylabel("x (m)")
ax1.set_xlabel("y (m)")
ax1.legend()
plt.tight_layout()
plt.savefig("trajectory.png")

fig, (ax1) = plt.subplots(1, 1, figsize=(10, 6))
ax1.plot(t, v, label="Speed")
ax1.set_ylabel("Speed (m/s)")
ax1.set_xlabel("Time (s)")
ax1.legend()
plt.tight_layout()
plt.savefig("speed.png")