# PP2
Second program in Lammps about diffusion (Data extracted from Eddy's thesis) 

Now i can select the number of atoms, size, and concentration( % ).

Wall functions added now. Only interact with soluto group (Particles B), and at a certain step the wall functions turn off. 

I separated the particles A from the particles B (Bs are in the middle).

I also put a write.data file to print the postion at time t = 0, and the velocities. 

The log.lammps file has the general information.

I can print the difussion coeficient of the system.

See the Leanord Jones potential that is used here: https://en.wikipedia.org/wiki/Lennard-Jones_potential




![Example_Energy_D Coefficient_Graph](https://user-images.githubusercontent.com/90353283/149673432-54067433-e38a-41fe-9348-13b836f37467.png)
