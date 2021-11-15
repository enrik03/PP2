import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# first graph fun.
def klk(step,ke,pe,etotal):


    kke = plt.plot(step,ke, label = 'Kinetic Energy')

    ppe = plt.plot(step,pe, label = 'Potential Energy')

    eetotal = plt.plot(step,etotal, label = 'Total Energy')

    plt.xlabel = ('steps') 
    plt.ylabel = ('Energy')

    #kke.ylabel = ('Kenetic Energy')
    #ppe.ylabel = ('Potential Energy')
    #eetotal.ylabel = ('Total')






    plt.show()

print(klk([0,1,2,3,4,5],[0,2,4,6,8],[8,6,4,2,0],[8,8,8,8,8]))