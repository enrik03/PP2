import matplotlib.pyplot as plt
from data import data

# run = 100000 , thermo = 100 
# the run is the final step, and the simulation run until 100000

def stp(run, thermo): # with this ratio we have the final step, thermo is like the separation, every step is thermo*t; t = t + 1 (loop)
    step_t = run / thermo
    return data(step_t)