# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n> / Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n> /Lab <X>/environment.yml
conda activate cspc

---
## PW2 - Lab A: Reproducible Foundations

**What I built:**
- a program that helps with the analysis of the freefall motion via integration and further visualisation of processed data using matplotlib, numpy, scipy

**Report and discussion** 

the calculated mean acceleration is -8.58 m/s^2. the error does not look bad: 12.5% is acceptable, it can be explained by air resistance and some other factors. but the standard deviation turned out to be 28.72 m/s^2.

this analysis shows that the deviation on the acceleration is high. it happens due to position data being a little noisy, and as you differentiate this noise gets worse, as differentiation with little intervals is sensitive to this: a difference in position can be relatively higher to the difference in time at some points, than at others. 


bonus part: the trajectory of motion is a nice lemniscate

**Tests:** all passing? yes

**Conclusion:**

although results might look acceptable, even little noise in the source data can create massive deviation. differentiation massively amplifies noise.