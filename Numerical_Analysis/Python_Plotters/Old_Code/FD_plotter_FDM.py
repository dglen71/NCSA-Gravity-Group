# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np

#Energy Plots
T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FDM_Energy.dat", usecols=(0))

energy_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FDM_Energy.dat", usecols=(1))
energy_Euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FDM_Energy.dat", usecols=(2))
energy_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FDM_Energy.dat", usecols=(3))
energy_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FDM_Energy.dat", usecols=(4))
energy_N = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FDM_Energy.dat", usecols=(5))

matplotlib.rcParams.update({'font.size': 30})
csfont = {'fontname':'Times New Roman'}

plt.figure(1)

plt.title("Energy using Fourier Derivative Matrix for Various Method", **csfont)
plt.xlabel("Time", **csfont)
plt.ylabel("Energy", **csfont)

plt.xlim([0,10])
plt.ylim([3,8])

###############################################################################
#Crank-Nicolson
plt.plot(T, energy_CN, 'b-', linestyle = '--', lw = 3, label = "Crank-Nicolson")

#plt.xlim([0,10])
#plt.ylim([3.85,4.1])
#plt.ylim([0,8])

#plt.axes().set_aspect(1)

#plt.title("Energy using Fourier Derivative Matrix for Crank-Nicolson Method", **csfont)
#plt.xlabel("Time", **csfont)
#plt.ylabel("Energy", **csfont)

#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_FDM_Energy_CN.pdf")

###############################################################################

#Euler
plt.plot(T, energy_Euler, 'g-', lw = 3, label = "Euler")

#RK2
plt.plot(T, energy_RK2, 'm-', lw = 3, label = "RK2")

#RK4
plt.plot(T, energy_RK4, 'c-', lw = 3, label = "RK4")

###############################################################################
#New Method
#plt.figure(2)

plt.plot(T, energy_N, 'r-', lw = 5, alpha = 0.5, label = "New Method")

#plt.xlim([0,10])
#plt.ylim([3.85,4.1])
#plt.ylim([0,8])

#plt.axes().set_aspect(1)

#plt.title("Energy using Fourier Derivative Matrix for New Method", **csfont)
#plt.xlabel("Time", **csfont)
#plt.ylabel("Energy", **csfont)

#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_FDM_Energy_New.pdf")

###############################################################################


plt.legend()

manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_FDM_Energy_Combined.pdf")

plt.show()