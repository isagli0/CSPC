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


## PW1 - Lab B:

**What I built:**
- a program that builds a plot based on data via matplotlib
- activated snakemake to build a new plot if data has changed.
 

**Conclusion:**
- matplotlib is an convenient tool that helps with organising and visualising data. snakemake makes a little more efficient as it doesn't do extra work if data is the same.



## PW2 - Lab A:

**What I built:**
- a program that helps with the analysis of the freefall motion via integration and further visualisation of processed data using matplotlib, numpy, scipy


**Tests:** all passing? yes


**Report and discussion** 

the calculated mean acceleration is -8.58 m/s^2. the error does not look bad: 12.5% is acceptable, it can be explained by air resistance and some other factors. but the standard deviation turned out to be 28.72 m/s^2.

this analysis shows that the deviation on the acceleration is high. it happens due to position data being a little noisy, and as you differentiate this noise gets worse, as differentiation with little intervals is sensitive to this: a difference in position can be relatively higher to the difference in time at some points, than at others. 


bonus part: the trajectory of motion is a nice lemniscate


**Conclusion:**

although results might look acceptable, even little noise in the source data can create massive deviation. differentiation massively amplifies noise.

## PW2 - Lab B:

**What I built:**

- a reproducable environment to analyze a variety of different experiments
- visual representation of the analysis (plots)
- a test for different methods of optimization
**Tests:** all passing? yes


**Report and discussion** 
part 2:
    A:
    all three methods worked well, even though gradient descent was a tiny bit off (2.9999963220107015), but this is an issue of the set desired error in a big way. both newton and slsqp both gave 3.0. this function has only one local extremum, so every method falls into it eventually.

    B:
    a) x0=0
       gradient descent: -1.3008343693148827
       newton: 0.16993844331159128, d2g=-5.653451105817997 - a minimum
       slsqp: -1.3006394477423422
       on this one gradient descent and slsqp agree

    b) x0=2
       gradient descent: 1.1309102497941645
       newton: 1.1309011226299859, d2g=9.347248189989148 - a maximum
       slsqp: -1.3006394477423422
       on this one gradient descent and newton agree

    the function has several stationary points, and from different starting points gradient descent and newton methods gave different results. however, the slsqp method turned out to be stable.

part 3:
    fitted k = 0.2617613705507395

part 4:
    equilibrium extent (newton): 0.6638476669609822
    equilibrium extent (SLSQP): 0.6638474284044567

part 5 (bonus):
    equivalence point: 50.00 mL
**Conclusion:**
some methods are sometimes better than others in a particular condition and none is universal