# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n> / Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n> /Lab <X>/environment.yml
conda activate cspc

---
## PW1 - Lab B: Reproducible Foundations

**What I built:**
- a program that builds a plot based on data via matplotlib
- activated snakemake to build a new plot if data has changed.
 
**Tests:** all passing? yes

**Conclusion:**
- matplotlib is an convenient tool that helps with organising and visualising data. snakemake makes a little more efficient as it doesn't do extra work if data is the same.