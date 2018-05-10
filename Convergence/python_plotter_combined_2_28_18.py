# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

styles = ["-" , "--" , "-." , ":","-"]
colors = ["b" , "r" , "g" , "m","c"]
alphas = [1, 1, 1, 1, 0.50]

SimNames = [["M0004", "M0008"] , ["L0037", "L0038", "L0039", "L0040"]]

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
        
        path = "C:\\Users\\eagle\\Desktop\\Convergence\\" +str(order)+ "th_Order\\Data\\exportDataCombined_"+SimNames[k][j]+".dat"

        if progress is True:
            data_x = np.genfromtxt(path, usecols=(0))
            data_y = np.genfromtxt(path, usecols=(1))

            data_merger_x = np.genfromtxt(path, usecols=(2))
            data_merger_y = np.genfromtxt(path, usecols=(3))

            data_x = np.abs(data_x)
            data_y = np.abs(data_y)

            #plt.axvline(x = data_merger_x[0], ls = styles[j] , color = colors[j] , linewidth = lw)
            '''
            index_start = 0
            index_end = 0

            for i in range(len(data_x)):
                    if(data_x[i] >= 150):
                        index_start = i
                        break
    
            for i in range(len(data_x)):
                if(data_x[i] >= data_merger_x[0] + past_merger):
                    index_end = i
                    break
    
            split_data_x = np.split(data_x, [index_start, index_end])[1]
            split_data_y = np.split(data_y, [index_start, index_end])[1]
            
            split_data_x = split_data_x - data_merger_x[0]
            
            max_value = np.max(np.abs(split_data_y))
            min_value = np.min(abs(split_data_y))
            
            max_x_dists[k][j] = np.max(split_data_x)
            

            #plt.xlim([150,data_merger_x[0] + past_merger + (.5 * past_merger)])
            #plt.ylim([(-1 * max_value) - (.1 * max_value),max_value + (.1 * max_value)])
            #plt.ylim([-1,1])    
        
            nearest_ten_max = math.ceil(math.log10(max_value)) + 1
            nearest_ten_min = math.ceil(math.log10(min_value)) - 1
            
            nearest_ten_mins[k][j] = nearest_ten_min
            
            '''
        
            #plt.ylim([10**(nearest_ten_min), 10**(upper_limit_y)])

            plt.axes().set_yscale("log")
            
            plt.plot(data_x,data_y,ls = styles[j] , color = colors[j], alpha = alphas[j], linewidth = lw , label = SimNames[k][j])
            

            #lines[k][j], =

            #plt.title(SimNames[j], **csfont)
            plt.xlabel("Time [M]", **csfont)
            plt.ylabel("|Phase Error| [rad]", **csfont)
        
            #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Plots_2\\"+str(past_merger)+"_Past_Merger_Log\\"+str(order)+"th_Order\\"+SimNames[j]+"_ErrPlot.png")
            #plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Plots_2\\"+str(past_merger)+"_Past_Merger_Log\\"+str(order)+"th_Order\\"+SimNames[j]+"_ErrPlot.pdf")    
    
            #plt.clf()   
    
            print(SimNames[k][j]+" is done")
            
          
path = "C:\\Users\\eagle\\Desktop\\Convergence\\8th_Order\\Plots\\"       
          
plt.figure(1)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.legend(loc = 'best')
final_x_lim = np.max(max_x_dists[0])
#plt.xlim([150,final_x_lim+ (.5 * past_merger)])
#plt.xlim([-2200,final_x_lim+ (.5 * past_merger)])
final_ten_min = np.min(nearest_ten_mins[0])
#plt.ylim([10**(final_ten_min), 10**(upper_limit_y)])
plt.savefig(path + "Phase_Error_Others.png")
plt.savefig(path + "Phase_Error_Others.pdf")
#Phase_Error_q_4_and_half.png"

plt.figure(2)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.legend(loc = 'best')
final_x_lim = np.max(max_x_dists[1])
#plt.xlim([150,final_x_lim+ (.5 * past_merger)])
#plt.xlim([-2000,final_x_lim+ (.5 * past_merger)])
final_ten_min = np.min(nearest_ten_mins[1])
#plt.ylim([10**(final_ten_min), 10**(upper_limit_y)])
plt.savefig(path + "Phase_Error_q_5_and_half-2.png")
plt.savefig(path + "Phase_Error_q_5_and_half-2.pdf")
    

plt.show()
