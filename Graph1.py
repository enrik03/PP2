import matplotlib.pyplot as plt


# first graph fun.
def graph(step, ke, pe, etotal):
    kke = plt.plot(step, ke, label='Kinetic Energy')

    ppe = plt.plot(step, pe, label='Potential Energy')

    eetotal = plt.plot(step, etotal, label='Total Energy')

    #plt.xlabel = ('steps')
    #plt.ylabel = ('Energy')

    # kke.ylabel = ('Kenetic Energy')
    # ppe.ylabel = ('Potential Energy')
    # eetotal.ylabel = ('Total')
    plt.legend()
    plt.show()


mylines = []


def data(r):
    with open('log.lammps', 'rt') as myfile:
        for myline in myfile:
            # print(myline.split()[1])
            mylines.append(myline)
    temp = []
    kee = []
    pee = []
    total = []

    i = 91
    k = 0
    while k < 4:
        while i < r + 92:

            #print(mylines[i].split()[k])
            if k == 0:
                temp.append(mylines[i].split()[k])
                #print(temp)
            elif k == 1:
                kee.append(mylines[i].split()[k])
                #print(kee)
            elif k == 2:
                pee.append(mylines[i].split()[k])
                #print(pee)
            elif k == 3:
                total.append(mylines[i].split()[k])
                #print(total)
            i = i + 1
        k = k + 1
        i = 91
    #print(total)
    return graph(temp, kee, pee, total)


# run = 100000 , thermo = 100
def stp(run, thermo):
    step_t = run / thermo
    return data(step_t)


print(stp(100000, 100))
