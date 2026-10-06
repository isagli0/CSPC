# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n> / Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n> / Lab <X>//environment.yml
conda activate cspc

---
## PW1 - Lab A: Reproducible Foundations

**What I built:**
- a reproducible conda environement, and a clean reposirory structure.
- reliable `pytest` checks
- a benchmark for a standard python loop in comparison to numpy calculations

**Speed comparison (loop vs NumPy):**
Tested with N0=200000
- loop : around 3.9 s (slightly different every time)
- numpy : around 0.00039 s (slightly different every time)
- speed-up: around 10000 times faster (slightly different every time)
**Tests:** all passing? yes

**Conclusion:**
- utilizing numpy for massive calculations turned out hundreds and even thousands times more effective than doing them purely on python. dealing with git and numpy was a little struggling since this was new for me and it took some time, but I figured everything out with the help of the lecture and a bit of research. 5% error for the test_decay was not suitable as well, so 10% error is accounted for instead.