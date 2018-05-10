# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

styles = ["-" , "--" , "-." , ":","-"]
colors = ["b" , "r" , "g" , "m","c"]
alphas = [0.5, 1, 1, 1, 0.50]

#SimNames = [["L0009", "L0010", "L0011" , "L0012", "L0013"] , ["L0014", "L0016", "L0029" , "L0032"]]

SimNames = [["L0010_N32", "L0010_N36", "L0010_N40"]]

lw = 3.0

max_x_dists = [[0,0,0,0,0],[0,0,0,0]]
nearest_ten_mins = [[0,0,0,0,0],[0,0,0,0]]
 
upper_limit_y = math.log10(40)

order = 8

past_merger = 150

matplotlib.rcParams.update({'font.size': 30})
csfont = {'fontname':'Times New Roman'}

for k in range(len(SimNames)):
    
    for j in range(len(SimNames[k])):
        
        plt.figure(k + 1)

        print(SimNames[k][j]+" is starting")    
    
        progress = True
        
        path = "C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Data_2_28_18\\"+SimNames[k][j]+ "\\" +SimNames[k][j]+ "_radially_extrapolated_strain_l2_m2.dat"

        if progress is True:
            data_x = np.genfromtxt(path, usecols=(0))
            data_y = np.genfromtxt(path, usecols=(1))
            
            plt.plot(data_x,data_y,ls = styles[j] , color = colors[j], alpha = alphas[j], linewidth = lw , label = SimNames[k][j])
            
            plt.xlabel("Time [M]", **csfont)
            plt.ylabel("|Phase Error| [rad]", **csfont)
        
    
            print(SimNames[k][j]+" is done")
            
            
plt.figure(1)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.legend(loc = 2)
#plt.savefig(path + "Phase_Error_1.png")
#plt.savefig(path + "Phase_Error_1.pdf")
#plt.savefig("C:\\Users\\eagle\\Desktop\\waveforms_combined_resolutions.png")

plt.figure(2)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.legend(loc = 2)
#plt.savefig(path + "Phase_Error_2.png")
#plt.savefig(path + "Phase_Error_2.pdf")
    

plt.show()
