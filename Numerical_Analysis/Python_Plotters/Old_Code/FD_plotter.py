# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np

real_evals_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_1.dat", usecols=(0))
imag_evals_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_1.dat", usecols=(1))

real_evals_euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_1.dat", usecols=(2))
imag_evals_euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_1.dat", usecols=(3))

real_evals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_1.dat", usecols=(4))
imag_evals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_1.dat", usecols=(5))

matplotlib.rcParams.update({'font.size': 14})
csfont = {'fontname':'Times New Roman'}

###############################################################################
#Crank-Nicolson
plt.figure(1)

plt.plot(real_evals_CN, imag_evals_CN, 'bo')

plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])

plt.axes().set_aspect(1)

plt.title("Crank-Nicolson Using CFL Number = 1", **csfont)
plt.xlabel("Re("+"$\lambda$"+")", **csfont)
plt.ylabel("Im("+"$\lambda$"+")", **csfont)

###############################################################################
#Euler
plt.figure(2)

plt.plot(real_evals_euler, imag_evals_euler, 'bo')

#Fix problem with axes
#minx_euler = np.min(real_evals_euler)       
#maxx_euler = np.max(real_evals_euler)

#miny_euler = np.min(imag_evals_euler)
#maxy_euler = np.max(imag_evals_euler)

#plt.xlim([minx_euler,maxx_euler])
#plt.ylim([miny_euler,maxy_euler])

plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])

#print((maxx_euler - minx_euler) / (maxy_euler - miny_euler))
#aspect_euler = (maxx_euler - minx_euler) / (maxy_euler - miny_euler)

#plt.axes().set_aspect(aspect_euler)

plt.axes().set_aspect(1)

plt.title("Euler Using CFL Number = 1", **csfont)
plt.xlabel("Re("+"$\lambda$"+")", **csfont)
plt.ylabel("Im("+"$\lambda$"+")", **csfont)

###############################################################################
#RK2
plt.figure(3)

plt.plot(real_evals_RK2, imag_evals_RK2, 'bo')

#Fix limits on graph:
#minx_RK2 = np.min(real_evals_RK2)       
#maxx_RK2 = np.max(real_evals_RK2)

#miny_RK2 = np.min(imag_evals_RK2)
#maxy_RK2 = np.max(imag_evals_RK2)

#plt.xlim([minx_RK2,maxx_RK2])
#plt.ylim([miny_RK2,maxy_RK2])

plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])

#print((maxx_RK2 - minx_RK2) / (maxy_RK2 - miny_RK2))
#aspect_RK2 = (maxx_RK2 - minx_RK2) / (maxy_RK2 - miny_RK2)

#plt.axes().set_aspect(aspect_RK2)

plt.axes().set_aspect(1)

plt.title("TVD RK2 Using CFL Number = 1", **csfont)
plt.xlabel("Re("+"$\lambda$"+")", **csfont)
plt.ylabel("Im("+"$\lambda$"+")", **csfont)

###############################################################################

#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_CN_1.png")

plt.show()