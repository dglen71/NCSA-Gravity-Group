# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:11:58 2017

@author: Derek Glennon
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:09:02 2017

@author: Derek Glennon
"""
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
from itertools import cycle
###########################################################################################################
#2x2 Grid Circle Plots for FDM
cycolRK2 = cycle('bgrcmy')
cycolRK4 = cycle('bgrcmy')
cycolLD2 = cycle('bgrcmy')
cycolLD4 = cycle('bgrcmy')

cymarkRK2 = cycle('.o^s*')
cymarkRK4 = cycle('.o^s*')
cymarkLD2 = cycle('.o^s*')
cymarkLD4 = cycle('.o^s*')

#rs2 = [.3, .5, .7]
#rs4 = [0.3, 0.5, 0.7]

rs2 = [.7]
rs4 = [.7]

lower_limit = -2
upper_limit = 2

matplotlib.rcParams.update({'font.size': 32}) 
csfont = {'fontname':'Times New Roman'}



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)   
    

ax1.set_aspect(aspect=1, adjustable = 'box-forced') 
ax2.set_aspect(aspect=1, adjustable = 'box-forced') 
ax3.set_aspect(aspect=1, adjustable = 'box-forced') 
ax4.set_aspect(aspect=1, adjustable = 'box-forced')    
#box-forced

for i in range(len(rs2)):
    
    real_evals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_RK2_FDM_"+str(rs2[i])+".dat", usecols=(0))
    imag_evals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_RK2_FDM_"+str(rs2[i])+".dat", usecols=(1))

    ax1.plot(real_evals_RK2, imag_evals_RK2, c=next(cycolRK2),marker=next(cymarkRK2),ls='None', label = "Courant Number " + str(rs2[i]))
    
    ax1.set_xlim([lower_limit, upper_limit])
    ax1.set_ylim([lower_limit, upper_limit])

    #plt.axes().set_aspect(1)

    #ax1.set_title("RK2 (2nd Order in Time, 2nd Order Fourier Pseudospectral in Space)", **csfont, y = 1.03)
    ax1.set_title("RK2 PS", **csfont, y = 1.03)
    ax1.set_xlabel("Re("+"$\lambda$"+")", **csfont)
    ax1.set_ylabel("Im("+"$\lambda$"+")", **csfont)
            
            

    #Unit Circle
    angle = np.arange(0, np.pi*2, 0.05)
    r = 1

    x = r * np.cos(angle)
    y = r * np.sin(angle)
    
    ax1.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)
    
    real_evals_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_LD2_FDM_"+str(rs2[i])+".dat", usecols=(0))
    imag_evals_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_LD2_FDM_"+str(rs2[i])+".dat", usecols=(1))

    ax2.plot(real_evals_LD2, imag_evals_LD2, c=next(cycolLD2),marker=next(cymarkLD2),ls='None', label = "Courant Number " + str(rs2[i]))
    
    ax2.set_xlim([lower_limit, upper_limit])
    ax2.set_ylim([lower_limit, upper_limit])

    #plt.axes().set_aspect(1)

    #ax2.set_title("LD2 (2nd Order in Time, 2nd Order Fourier Pseudospectral in Space)", **csfont, y = 1.03)
    ax2.set_title("LD2 PS", **csfont, y = 1.03)
    ax2.set_xlabel("Re("+"$\lambda$"+")", **csfont)
    ax2.set_ylabel("Im("+"$\lambda$"+")", **csfont)

    #Unit Circle
    angle = np.arange(0, np.pi*2, 0.05)
    r = 1

    x = r * np.cos(angle)
    y = r * np.sin(angle)
    
    ax2.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)   
            

for i in range(len(rs4)):
    
    real_evals_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_RK4_FDM_"+str(rs4[i])+".dat", usecols=(0))
    imag_evals_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_RK4_FDM_"+str(rs4[i])+".dat", usecols=(1))

    ax3.plot(real_evals_RK4, imag_evals_RK4, c=next(cycolRK4),marker=next(cymarkRK4),ls='None', label = "Courant Number " + str(rs4[i]))
    
    ax3.set_xlim([lower_limit, upper_limit])
    ax3.set_ylim([lower_limit, upper_limit])

    #plt.axes().set_aspect(1)

    #ax3.set_title("RK4 (4th Order in Time, 4th Order Fourier Pseudospectral in Space)", **csfont, y = 1.03)
    ax3.set_title("RK4 PS", **csfont, y = 1.03)
    ax3.set_xlabel("Re("+"$\lambda$"+")", **csfont)
    ax3.set_ylabel("Im("+"$\lambda$"+")", **csfont)

    #Unit Circle
    angle = np.arange(0, np.pi*2, 0.05)
    r = 1

    x = r * np.cos(angle)
    y = r * np.sin(angle)
    
    ax3.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)  
    
    
    
    real_evals_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_LD4_FDM_"+str(rs4[i])+".dat", usecols=(0))
    imag_evals_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_LD4_FDM_"+str(rs4[i])+".dat", usecols=(1))
    
    ax4.plot(real_evals_LD4, imag_evals_LD4, c=next(cycolLD4),marker=next(cymarkLD4),ls='None', label = "Courant Number " + str(rs4[i]))
    
    ax4.set_xlim([lower_limit, upper_limit])
    ax4.set_ylim([lower_limit, upper_limit])

    #plt.axes().set_aspect(1)

    #ax4.set_title("LD4 (4th Order in Time, 4th Order Fourier Pseudospectral in Space)", **csfont, y = 1.03)
    ax4.set_title("LD4 PS", **csfont, y = 1.03)
    ax4.set_xlabel("Re("+"$\lambda$"+")", **csfont)
    ax4.set_ylabel("Im("+"$\lambda$"+")", **csfont)

    #Unit Circle
    angle = np.arange(0, np.pi*2, 0.05)
    r = 1

    x = r * np.cos(angle)
    y = r * np.sin(angle)
    
    ax4.plot(x,y , color = 'grey', ls = '--', alpha = 0.5) 
    
#ax1.legend(loc = 2,prop={'size': 15})
#ax2.legend(prop={'size': 15})
#ax3.legend(loc = 2, prop={'size': 15})
#ax4.legend(prop={'size': 15})
    
            
#fig.tight_layout()
plt.subplots_adjust(left = None, bottom = None, right = None, top = None, wspace = 0, hspace = .3)

ax1.set_xticks([-2,-1,0,1,2])
ax1.set_yticks([-2,-1,0,1,2])

manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\Pseudospectral_Circles.pdf")

 

 
plt.show()

