# PP2
Second program in Lammps about diffusion (Data extracted from Eddy's thesis) 

Now i can select the number of atoms, size, and concentration( % ).

i also put a new command (minimize) in order to run the program on my laptop.

minimize etol ftol maxiter maxeval
etol = stopping tolerance for energy (unitless)

ftol = stopping tolerance for force (force units)

maxiter = max iterations of minimizer

maxeval = max number of force/energy evaluations

more info on https://docs.lammps.org/minimize.html

I didn't find the wall fuction but with the region fuction i made it well.
Thus i separated the particles A from the particles B (Bs are in the middle)
At a distant of 4 sigmas
