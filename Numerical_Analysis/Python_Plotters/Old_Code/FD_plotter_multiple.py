# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
from itertools import cycle
cycol = cycle('bgrcmy')
cycolEuler = cycle('bgrcmy')
cycolRK2 = cycle('bgrcmy')
cycolRK4 = cycle('bgrcmy')
cycolLD2 = cycle('bgrcmy')
cycolLD4 = cycle('bgrcmy')

cymark = cycle('.o^s*')
cymarkEuler = cycle('.o^s*')
cymarkRK2 = cycle('.o^s*')
cymarkRK4 = cycle('.o^s*')
cymarkLD2 = cycle('.o^s*')
cymarkLD4 = cycle('.o^s*')


#rs = [0.8,0.9,1,1.1,1.2]

rs = [0.9,1,1.1]
rs_RK4 = [1.4,1.5,1.6]

lower_limit = -2
upper_limit = 2

matplotlib.rcParams.update({'font.size': 32})
plt.rcParams["font.family"] = "Times New Roman"
csfont = {'fontname':'Times New Roman'}

#for i in range(len(rs)):
#
#    real_evals_euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_E_RK2_"+str(rs[i])+".dat", usecols=(0))
#    imag_evals_euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_E_RK2_"+str(rs[i])+".dat", usecols=(1))
#
#    real_evals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_E_RK2_"+str(rs[i])+".dat", usecols=(2))
#    imag_evals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_E_RK2_"+str(rs[i])+".dat", usecols=(3))
#    
#    real_evals_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_circle_LD2_"+str(rs[i])+".dat", usecols=(0))
#    imag_evals_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_circle_LD2_"+str(rs[i])+".dat", usecols=(1))    
#    
#    ###############################################################################
#    #Euler
#    plt.figure(1)    
#    
#    plt.plot(real_evals_euler, imag_evals_euler, c=next(cycolEuler),marker=next(cymarkEuler),ls='None', label = "Courant Number " + str(rs[i]))
#    
#    plt.xlim([lower_limit, upper_limit])
#    plt.ylim([lower_limit, upper_limit])
#
#    plt.axes().set_aspect(1)
#
#    plt.title("Euler(2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont)
#    plt.xlabel("Re("+"$\lambda$"+")", **csfont)
#    plt.ylabel("Im("+"$\lambda$"+")", **csfont)
#    
#    #Unit Circle
#    angle = np.arange(0, np.pi*2, 0.05)
#    r = 1
#
#    x = r * np.cos(angle)
#    y = r * np.sin(angle)
#    
#    plt.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)
#    
#      
#    #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_Euler_"+str(rs[i])+".png")
#    
#    #plt.clf()
#
#    ###############################################################################
#    #RK2
#    plt.figure(2)
#
#    plt.plot(real_evals_RK2, imag_evals_RK2, c=next(cycolRK2),marker=next(cymarkRK2),ls='None', label = "Courant Number " + str(rs[i]))
#    
#    plt.xlim([lower_limit, upper_limit])
#    plt.ylim([lower_limit, upper_limit])
#
#    plt.axes().set_aspect(1)
#
#    plt.title("RK2(2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont)
#    plt.xlabel("Re("+"$\lambda$"+")", **csfont)
#    plt.ylabel("Im("+"$\lambda$"+")", **csfont)
#
#    #Unit Circle
#    angle = np.arange(0, np.pi*2, 0.05)
#    r = 1
#
#    x = r * np.cos(angle)
#    y = r * np.sin(angle)
#    
#    plt.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)    
#    
#    #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_RK2_"+str(rs[i])+".png")
#    
#    #plt.clf()
#    
#    ###############################################################################
#    #LD2
#    plt.figure(3)
#
#    plt.plot(real_evals_LD2, imag_evals_LD2, c=next(cycolLD2),marker=next(cymarkLD2),ls='None', label = "Courant Number " + str(rs[i]))
#    
#    plt.xlim([lower_limit, upper_limit])
#    plt.ylim([lower_limit, upper_limit])
#
#    plt.axes().set_aspect(1)
#
#    plt.title("LD2(2nd Order in Time, 2nd Order Finite Differencing in Space)", **csfont)
#    plt.xlabel("Re("+"$\lambda$"+")", **csfont)
#    plt.ylabel("Im("+"$\lambda$"+")", **csfont)
#
#    #Unit Circle
#    angle = np.arange(0, np.pi*2, 0.05)
#    r = 1
#
#    x = r * np.cos(angle)
#    y = r * np.sin(angle)
#    
#    plt.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)    
#    
#    #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_RK2_"+str(rs[i])+".png")
#    
#    #plt.clf()
#    
#    
#    
#for i in range(len(rs_RK4)):
#    
#    ###############################################################################    
#    #RK4
#    
#    real_evals_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_circle_RK4_"+str(rs_RK4[i])+".dat", usecols=(0))
#    imag_evals_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_circle_RK4_"+str(rs_RK4[i])+".dat", usecols=(1))
#    
#    
#    plt.figure(4)
#
#    plt.plot(real_evals_RK4, imag_evals_RK4, c=next(cycolRK4),marker=next(cymarkRK4),ls='None', label = "Courant Number " + str(rs_RK4[i]))
#    
#    plt.xlim([lower_limit, upper_limit])
#    plt.ylim([lower_limit, upper_limit])
#
#    plt.axes().set_aspect(1)
#
#    plt.title("RK4(4th Order in Time, 4th Order Finite Differencing in Space)", **csfont)
#    plt.xlabel("Re("+"$\lambda$"+")", **csfont)
#    plt.ylabel("Im("+"$\lambda$"+")", **csfont)
#
#    #Unit Circle
#    angle = np.arange(0, np.pi*2, 0.05)
#    r = 1
#
#    x = r * np.cos(angle)
#    y = r * np.sin(angle)
#    
#    plt.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)    
#    
#    #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_RK2_"+str(rs[i])+".png")
#    
#    #plt.clf()
#    
#    ###############################################################################    
#    #LD4
#    
#    real_evals_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_circle_LD4_"+str(rs_RK4[i])+".dat", usecols=(0))
#    imag_evals_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_circle_LD4_"+str(rs_RK4[i])+".dat", usecols=(1))
#    
#    
#    plt.figure(5)
#
#    plt.plot(real_evals_LD4, imag_evals_LD4, c=next(cycolLD4),marker=next(cymarkLD4),ls='None', label = "Courant Number " + str(rs_RK4[i]))
#    
#    plt.xlim([lower_limit, upper_limit])
#    plt.ylim([lower_limit, upper_limit])
#
#    plt.axes().set_aspect(1)
#
#    plt.title("LD4 (4th Order in Time, 4th Order Finite Differencing in Space) Method", **csfont)
#    plt.xlabel("Re("+"$\lambda$"+")", **csfont)
#    plt.ylabel("Im("+"$\lambda$"+")", **csfont)
#
#    #Unit Circle
#    angle = np.arange(0, np.pi*2, 0.05)
#    r = 1
#
#    x = r * np.cos(angle)
#    y = r * np.sin(angle)
#    
#    plt.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)    
#    
#    #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_RK2_"+str(rs[i])+".png")
#    
#    #plt.clf()
#    
#    
#    
#plt.figure(1)
#plt.legend(loc = 1, prop={'size': 15})
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
##plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_Euler.pdf")
##plt.savefig("C:\Users\eagle\Box_Sync\!CFD\!Paper_1\\plot_Euler.pdf")  
#
#plt.figure(2)
#plt.legend(loc = 1, prop={'size': 15})
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_RK2.pdf")
##plt.savefig("C:\Users\eagle\Box Sync\!CFD\!Paper 1\\plot_RK2.pdf")
#
#plt.figure(3)
#plt.legend(loc = 2, prop={'size': 15})
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_LD2.pdf")
#
#plt.figure(4)
#plt.legend(loc = 2, prop={'size': 15})
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_RK4.pdf")
#
#plt.figure(5)
#plt.legend(loc = 2, prop={'size': 15})
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
#plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_LD4.pdf")
#
############################################################################################################
##Unit Circle for CN
#rs_unit = [1,10,20]
#fig, axes = plt.subplots(nrows=1, ncols=3, sharey=True, sharex=True)    
#    
#for i, ax in enumerate(axes.flat, start=1):
#    
#    ax.set(aspect=1, adjustable = 'box-forced')
#    
#    ###############################################################################
#    #Crank-Nicolson
#
#    real_evals_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_CN_"+str(rs_unit[i - 1])+".dat", usecols=(0))
#    imag_evals_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_CN_"+str(rs_unit[i - 1])+".dat", usecols=(1))  
#
#    ax.set_xlim([lower_limit, upper_limit])
#    ax.set_ylim([lower_limit, upper_limit])
#    
#    ax.plot(real_evals_CN, imag_evals_CN, 'bo')
#
#    ax.set_title("Crank-Nicolson Method With CFL Number = "+str(rs_unit[i - 1]), **csfont)
#    ax.set_xlabel("Re("+"$\lambda$"+")", **csfont)
#    ax.set_ylabel("Im("+"$\lambda$"+")", **csfont)
#    
#    #Unit Circle
#    angle = np.arange(0, np.pi*2, 0.05)
#    r = 1
#
#    x = r * np.cos(angle)
#    y = r * np.sin(angle)
#    
#    ax.plot(x,y , color = 'grey', ls = '--', alpha = 0.5)
#    
#    #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_CN_"+str(rs[i])+".png")
#
#    #plt.clf()
#
#manager = plt.get_current_fig_manager()
#manager.window.showMaximized()
##plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\plot_CN.pdf")
##plt.savefig("C:\Users\eagle\Box Sync\!CFD\!Paper 1\\plot_CN.pdf")

###########################################################################################################
#Max Eigenvalue PLots

rs_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(0))
maxevals_CN = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(1))

rs_Euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(2))
maxevals_Euler = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(3))

rs_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(4))
maxevals_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(5))

rs_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(6))
maxevals_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(7))      
    
rs_N = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(8))
maxevals_N = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max.dat", usecols=(9))       


plt.figure(7)

###########################################################################################################
#For Combined Plot
#plt.title("Max Eigenvalue vs CFL Number for Various Methods", **csfont)
plt.xlabel("Courant Number", **csfont)
plt.ylabel("Max "+"|$\lambda$|", **csfont)
#plt.xlim([0,2])
#plt.ylim([0,10])
plt.ylim([10**(-.1), 10**(1)])

###########################################################################################################
plt.semilogy(rs_CN, maxevals_CN , 'b-', lw = 3, linestyle = '--', label = "LD2 FD2")

plt.semilogy(rs_RK2, maxevals_RK2, 'm-', lw = 3, label = "RK2 FD2")

plt.semilogy(rs_RK4, maxevals_RK4, 'c-', lw = 3, label = "RK4 FD4")

plt.semilogy(rs_N, maxevals_N, 'r-', lw = 3, alpha = 0.5, label = "LD4 FD4")
    
 
plt.legend(loc = 2)

manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\Combined_Max_Eval_FD.pdf")


###########################################################################################################
#For FDM Combined Plot

plt.figure(8)

rs_LD2_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(0))
maxevals_LD2_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(1))

rs_Euler_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(2))
maxevals_Euler_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(3))

rs_RK2_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(4))
maxevals_RK2_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(5))

rs_RK4_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(6))
maxevals_RK4_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(7))      
    
rs_LD4_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(8))
maxevals_LD4_FDM = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\evals_max_FDM.dat", usecols=(9))


#plt.title("Max Eigenvalue vs CFL Number for Various Methods", **csfont)
plt.xlabel("Courant Number", **csfont)
plt.ylabel("Max "+"|$\lambda$|", **csfont)
#plt.xlim([0,2])
#plt.ylim([0,10])
plt.ylim([10**(-.1), 10**(1)])


plt.semilogy(rs_LD2_FDM, maxevals_LD2_FDM , 'b-', lw = 3, linestyle = '--', label = "LD2 PS")

plt.semilogy(rs_RK2_FDM, maxevals_RK2_FDM, 'm-', lw = 3, label = "RK2 PS")

plt.semilogy(rs_RK4_FDM, maxevals_RK4_FDM, 'c-', lw = 3, label = "RK4 PS")

plt.semilogy(rs_LD4_FDM, maxevals_LD4_FDM, 'r-', lw = 3, alpha = 0.5, label = "LD4 PS")
    
 
plt.legend(loc = 'best')

manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\Combined_Max_Eval_Pseudospectral.pdf")
 
 
 
plt.show()
    