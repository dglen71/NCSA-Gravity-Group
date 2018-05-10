# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:38:28 2017

@author: Derek Glennon
"""

# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 25})
csfont = {'fontname':'Times New Roman'}

T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_FD.dat", usecols=(0))

error_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_FD.dat", usecols=(1))
error_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_FD.dat", usecols=(2))
error_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_FD.dat", usecols=(3))
error_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_FD.dat", usecols=(4))

plt.figure(1)

plt.semilogy(T, error_LD2 , 'b-', lw = 3, alpha = 0.5, label = "LD2 FD2")

plt.semilogy(T, error_LD4, 'm-', lw = 3, alpha = 0.5, label = "LD4 FD4")

plt.semilogy(T, error_RK2, 'orange', lw = 3, linestyle = '--', label = "RK2 FD2")

plt.semilogy(T, error_RK4, 'r-', lw = 3, linestyle = '--', label = "RK4 FD4")

plt.legend(loc = 'best')

plt.xlabel("Time")
plt.ylabel("$L^1$ Error")
#plt.title("Courant Number = 0.31831 & FD")

plt.ylim([10**(-11),10**(-1)])


manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\FD_L1_Error.pdf")



plt.figure(2)

T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(0))

error_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(1))
error_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(2))
error_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(3))
error_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(4))
error_LD6 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(5))
error_LD8 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS.dat", usecols=(6))


plt.semilogy(T, error_LD2 , 'b-', lw = 3, alpha = 0.5, label = "LD2 PS")

plt.semilogy(T, error_LD4, 'm-', lw = 3,  alpha = 0.5, label = "LD4 PS")

plt.semilogy(T, error_RK2, 'orange', lw = 3, linestyle = '--', label = "RK2 PS")

plt.semilogy(T, error_RK4, 'r-', lw = 3, linestyle = '--', label = "RK4 PS")

plt.semilogy(T, error_LD6, 'c-', lw = 3, alpha = 0.5, label = "LD6 PS")

#plt.semilogy(T, error_LD8, 'y-', lw = 3, alpha = 0.5, label = "LD8 Pseudospectral")

plt.legend(loc = ([.68,.54]))

plt.xlabel("Time")
plt.ylabel("$L^1$ Error")
#plt.title("Courant Number = 0.31831 & Fourier PS")

plt.ylim([10**(-15),10**(-4)])


manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\Pseudospectral_L1_Error.pdf")


plt.show()