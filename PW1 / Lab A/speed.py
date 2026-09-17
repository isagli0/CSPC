import decay
import time

N0 = 200000 # initial number of atoms
lam = 0.4 # the decay rate
dt = 0.05 # time step
steps = 200 # simulation steps

#pure python
start_pure = time.perf_counter()  # start the timer for pure python
decay.simulate_loop(N0, lam, dt=dt, steps=steps) # pure python simulation
end_pure = time.perf_counter() # end the timer for pure python
time_pure = end_pure - start_pure # calculate the time taken for pure python

# numpy
start_numpy = time.perf_counter() # start the timer for numpy
decay.simulate(N0, lam, dt=dt, steps=steps) # numpy simulation
end_numpy = time.perf_counter() # end the timer for numpy
time_numpy = end_numpy - start_numpy # calculate the time taken for numpy

ratio = time_pure/time_numpy # how many times faster is numpy than pure python
print(f"Pure Python time: {time_pure:.6f} seconds. \nNumPy time: {time_numpy:.6f} seconds.\nNumPy is {(ratio):.2f} times faster.")  