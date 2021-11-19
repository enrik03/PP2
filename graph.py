import matplotlib.pyplot as plt


# first graph fun.
def graph(step, ke, pe, etotal):
    kke = plt.plot(step, ke, label='Kinetic Energy')

    ppe = plt.plot(step, pe, label='Potential Energy')

    eetotal = plt.plot(step, etotal, label='Total Energy')

    #plt.xlabel = ('steps')
    #plt.ylabel = ('Energy')

    
    plt.legend()
    plt.show()