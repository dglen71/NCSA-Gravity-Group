# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 23:58:24 2017

@author: Derek Glennon
"""

# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
###########################################################################################################
matplotlib.rcParams.update({'font.size': 17}) 
csfont = {'fontname':'Times New Roman'}

###############################################################
#LD2 and RK2
###############################################################


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)   
    
X = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(0))
    
LD2_start = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(1))
LD2_start_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(2))

ax1.plot(X, LD2_start, label = "LD2")
ax1.plot(X, LD2_start_Err, label = "LD2 Error")

ax1.set_title("LD2 Initial (2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)

LD2_end = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(3))
LD2_end_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(4))

ax2.plot(X, LD2_end, label = "LD2")
ax2.plot(X, LD2_end_Err, label = "LD2 Error")

ax2.set_title("LD2 Final (2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)

RK2_start = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(5))
RK2_start_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(6))

ax3.plot(X, RK2_start, label = "RK2")
ax3.plot(X, RK2_start_Err, label = "RK2 Error")

ax3.set_title("RK2 Initial (2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)

RK2_end = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(7))
RK2_end_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(8))

ax4.plot(X, RK2_end, label = "RK2")
ax4.plot(X, RK2_end_Err, label = "RK2 Error")

ax4.set_title("RK2 Final (2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)



    
ax1.legend(prop={'size': 15})
ax2.legend(prop={'size': 15})
ax3.legend(prop={'size': 15})
ax4.legend(prop={'size': 15})
    
            

manager = plt.get_current_fig_manager()
manager.window.showMaximized()

#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\FD_Circles.pdf")


###############################################################
#LD4 and RK4
###############################################################

matplotlib.rcParams.update({'font.size': 17}) 
csfont = {'fontname':'Times New Roman'}


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)   
    
LD4_start = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(9))
LD4_start_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(10))

ax1.plot(X, LD4_start, label = "LD4")
ax1.plot(X, LD4_start_Err, label = "LD4 Error")

ax1.set_title("LD4 Initial (4th Order in Time, 4th Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)

LD4_end = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(11))
LD4_end_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(12))

ax2.plot(X, LD4_end, label = "LD4")
ax2.plot(X, LD4_end_Err, label = "LD4 Error")

ax2.set_title("LD4 Final (4th Order in Time, 4th Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)

RK4_start = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(13))
RK4_start_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(14))

ax3.plot(X, RK4_start, label = "RK4")
ax3.plot(X, RK4_start_Err, label = "RK4 Error")

ax3.set_title("RK4 Initial (4th Order in Time, 4th Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)

RK4_end = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(15))
RK4_end_Err = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\start_final_PS.dat", usecols=(16))

ax4.plot(X, RK4_end, label = "RK4")
ax4.plot(X, RK4_end_Err, label = "RK4 Error")

ax4.set_title("RK4 Final (4th Order in Time, 4th Order Finite Differencing in Space)", **csfont, y = 1.03)
#ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)



    
ax1.legend(prop={'size': 15})
ax2.legend(prop={'size': 15})
ax3.legend(prop={'size': 15})
ax4.legend(prop={'size': 15})
    
            

manager = plt.get_current_fig_manager()
manager.window.showMaximized()

 

 
plt.show()
