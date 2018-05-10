# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:09:45 2017

@author: Derek Glennon
"""
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np


matplotlib.rcParams.update({'font.size': 25})
csfont = {'fontname':'Times New Roman'}

T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error.dat", usecols=(0))

error_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error.dat", usecols=(1))
error_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error.dat", usecols=(2))
error_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error.dat", usecols=(3))
error_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error.dat", usecols=(4))

plt.figure(1)

plt.semilogy(T, error_LD2 , 'b-', lw = 3, linestyle = '--', label = "LD2 FD2")

plt.semilogy(T, error_LD4, 'm-', lw = 3, alpha = 0.5, label = "LD4 FD4")

plt.semilogy(T, error_RK2, 'c-', lw = 3, alpha = 0.5, label = "RK2 FD2")

plt.semilogy(T, error_RK4, 'r-', lw = 3, alpha = 0.5, label = "RK4 FD4")

plt.legend(loc = 'best')

plt.xlabel("Time")
plt.ylabel("|Energy Error|")
#plt.title("Courant Number = 0.31831 & FD")


manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\FD_Energy_Error.pdf")



plt.figure(2)

T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error_Pseudospectral.dat", usecols=(0))

error_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error_Pseudospectral.dat", usecols=(1))
error_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error_Pseudospectral.dat", usecols=(2))
error_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error_Pseudospectral.dat", usecols=(3))
error_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Energy_Error_Pseudospectral.dat", usecols=(4))


plt.semilogy(T, error_LD2 , 'b-', lw = 3, linestyle = '--', label = "LD2 PS")

plt.semilogy(T, error_LD4, 'm-', lw = 3, alpha = 0.5, label = "LD4 PS")

plt.semilogy(T, error_RK2, 'c-', lw = 3, alpha = 0.5, label = "RK2 PS")

plt.semilogy(T, error_RK4, 'r-', lw = 3, alpha = 0.5, label = "RK4 PS")

plt.legend(loc = ([.68,.6]))

plt.xlabel("Time")
plt.ylabel("|Energy Error|")
#plt.title("Courant Number = 0.31831 & Fourier PS")


manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\Pseudospectral_Energy_Error.pdf")


plt.show()