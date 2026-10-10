"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
import scipy
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

x = 0.0
lr = 0.1
step = lr * df(x)
while abs(step) > 1e-6:
    step = lr * df(x)
    x -= step
print(f"2A:\nGradient descent result: {x}")

x_newton = newton(df, 0.0, fprime=d2f)
print(f"Newton result: {x_newton}")

x_slsqp = minimize(f, 0.0, method="SLSQP")
print(f"SLSQP result: {x_slsqp.x[0]}\n")



# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
x=0.0
lr = 0.01
step = lr * dg(x)
while abs(step) > 1e-6:
    step = lr * dg(x)
    x -= step
print(f"2B:\nGradient descent result from x0=0: {x}")
x_newton = newton(dg, 0.0, fprime=d2g)
print(f"Newton result from x0=0: {x_newton}, d2g={d2g(x_newton)}")
x_slsqp = minimize(g, 0.0, method="SLSQP")
print(f"SLSQP result from x0=0: {x_slsqp.x[0]}\n")

x=2.0
lr = 0.01
step = lr * dg(x)
while abs(step) > 1e-6:
    step = lr * dg(x)
    x -= step
print(f"Gradient descent result from x0=2: {x}")
x_newton = newton(dg, 2.0, fprime=d2g)
print(f"Newton result from x0=2: {x_newton}, d2g={d2g(x_newton)}")
x_slsqp = minimize(g, 2.0, method="SLSQP")
print(f"SLSQP result from x0=2: {x_slsqp.x[0]}")
