import matplotlib.pyplot as plt
from graph import graph
mylines = []

def data(r): # this argument is for the total lines which are within the log.lammps file (The final line of the simulation updates)
    with open('log.lammps', 'rt') as myfile: # open the file which we are going to graph
        for myline in myfile:
            # print(myline.split()[1])
            mylines.append(myline) # Rewrite the file in a array
    temp = []
    kee = []
    pee = []
    total = []

    i = 91
    k = 0
    while k < 4: # this loop selects a k-column 
        while i < r + 92: # this loop selects the lines, it always begin with 91 (it depends with the file log.lammps)

            #print(mylines[i].split()[k])
            if k == 0:
                temp.append(int(mylines[i].split()[k])) # so i create a new array for the temp steps
                
            elif k == 1:
                kee.append(float(mylines[i].split()[k])) # this array is for the kinetic energy
                
            elif k == 2:
                pee.append(float(mylines[i].split()[k])) # this is for the potential
                
            elif k == 3:
                total.append(float(mylines[i].split()[k])) # total energy array
                
            i = i + 1
        k = k + 1
        i = 91
    #You can see that this fun. only selects 4 columns, because we only want to graph the energies in the log.lammps file

    # At the end we graph it
    return graph(temp, kee, pee, total)