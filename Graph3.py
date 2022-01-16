import matplotlib.pyplot as plt


# first graph fun.
def graph(step, ke, pe, etotal):
    # x = np.linspace(0, len(step))

    kke = plt.plot(step, ke, label='Kinetic Energy')

    ppe = plt.plot(step, pe, label='Potential Energy')

    eetotal = plt.plot(step, etotal, label='Total Energy')

    
    plt.xlabel('Steps')
    plt.ylabel('Energy')
    plt.title('Energy vs steps Graph')
    plt.grid()

    plt.legend()
    plt.show()


mylines = []


def data(
        r):  # this argument is for the total lines which are within the log.lammps file (The final line of the simulation updates)
    with open('log.lammps', 'rt') as myfile:  # open the file which we are going to graph
        for myline in myfile:
            #print(myline.split()[0])
            
            mylines.append(myline)  # Rewrite the file in a array
            #print(mylines[1])
            myline.split('_')[0]
    temp = []
    kee = []
    pee = []
    total = []

    i = int
    nw = 0
    while nw < 2:
        
        if nw == 0:
            ii = 104
                
        else:
            
            ii = 649 

        ev = r + ii + 1
        i = ii    
        nw += 1
        k = 0
        while k < 4:  # this loop selects a k-column
            while i < ev:  # this loop selects the lines, it begins in 104 (it depends with the file log.lammps)

                    # mylines[i].split()[k]
                if k == 0:

                    temp.append(int(mylines[i-1].split()[k]))  # so i create a new array for the temp steps
                    #print(temp)
                elif k == 1:
                    kee.append(float(mylines[i-1].split()[k]))  # this array is for the kinetic energy

                elif k == 2:
                    pee.append(float(mylines[i-1].split()[k]))  # this is for the potential

                elif k == 3:
                    total.append(float(mylines[i-1].split()[k]))  # total energy array

                i = i + 1
            k = k + 1
            i = ii
    # You can see that this fun. only selects 4 columns, because we only want to graph the energies in the log.lammps file

    # At the end we graph it
    return graph(temp, kee, pee, total)


# run = 100000 , thermo= 100
# the run is the final step, and the simulation run until 100000
def stp(run,thermo):  # with this ratio we have the final step, thermo is like the separation, every step is thermo*t; t = t + 1 (loop)
    step_t = run / thermo
    return data(step_t)


print(stp(50000, 100))
