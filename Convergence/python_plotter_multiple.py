# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

SimNames = ["E0001", "E0009", "E0013", "E0017", "E0021", "E0025", "F0002",
"F0010", "F0014", "F0018", "F0026", "G0003", "H0004", "H0011",
"H0015", "H0019", "H0027", "I0004", "I0012", "I0016", "I0020",
"I0028", "J0005", "J0006", "J0007", "J0008", "J0022", "J0037",
"J0038", "J0039", "J0040", "J0041", "J0042", "J0043", "J0044",
"J0045", "J0046", "J0047", "J0048", "J0049", "J0050", "J0051",
"J0052", "J0053", "J0054", "J0055", "J0056", "J0061", "J0062",
"J0063", "J0064", "J0065", "J0066", "J0067", "J0068", "K0001",
"K0002", "K0003", "K0004", "K0009", "K0010", "K0011", "K0012",
"K0017", "K0018", "K0019", "K0020", "K0024", "K0025", "K0026",
"K0027", "K0028", "L0017", "L0018", "L0019", "L0020", "L0037",
"L0038", "L0039", "L0040", "M0004", "M0008"]
  
#Not Finished
#"K0009", "K0010", "K0011", "K0012", 
# "K0025", "K0026", "K0027", "K0028",
#"L0017", "L0018", "L0019", "L0020",
# "L0037", "L0038", "L0039", "L0040",
# "M0004", "M0008"
  
#Wei Sims
#J0065, J0066, J0067
  
#Problem Sims
#J0024, J0068, J0023  
  
upper_limit_y = math.log10(40)
  
order = 8

past_merger = 150

for j in range(len(SimNames)):

    print(SimNames[j]+" is starting")  
    
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    
    progress = True
    
#    if past_merger is 50:
#        if SimNames[j] is "J0022" or SimNames[j] is "K0001" or SimNames[j] is "J0007":
#            progress = False
            
#    if past_merger is 60:
#        if SimNames[j] is "J0022" or SimNames[j] is "K0001" or SimNames[j] is "J0007":
#            progress = False 
            
#    if past_merger is 80:
#        if SimNames[j] is "J0022" or SimNames[j] is "K0001" or SimNames[j] is "J0007":
#            progress = False  
          
#    if past_merger is 100:
#        if SimNames[j] is "J0022" or SimNames[j] is "K0001" or SimNames[j] is "J0007"or SimNames[j] is "J0041":
#            progress = False

    if past_merger is 150:
        if SimNames[j] is "K0009" or SimNames[j] is "K0012" or SimNames[j] is "K0027" or SimNames[j] is "K0028" or SimNames[j] is "L0017" or SimNames[j] is "L0018" or SimNames[j] is "L0019" or SimNames[j] is "L0020" or SimNames[j] is "L0037" or SimNames[j] is "L0038" or SimNames[j] is "L0039" or SimNames[j] is "L0040" or SimNames[j] is "M0008":
            progress = False

    if progress is True:
        data_x = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data_2\\"+str(order)+"th_Order\\exportDataCombined_"+SimNames[j]+".dat", usecols=(0))
        data_y = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data_2\\"+str(order)+"th_Order\\exportDataCombined_"+SimNames[j]+".dat", usecols=(1))

        data_merger_x = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data_2\\"+str(order)+"th_Order\\exportDataCombined_"+SimNames[j]+".dat", usecols=(2))
        data_merger_y = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data_2\\"+str(order)+"th_Order\\exportDataCombined_"+SimNames[j]+".dat", usecols=(3))

        data_x = np.abs(data_x)
        data_y = np.abs(data_y)

        plt.axvline(x = data_merger_x[0], c='r')

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
        max_value = np.max(np.abs(split_data_y))
        min_value = np.min(abs(split_data_y))

        plt.xlim([150,data_merger_x[0] + past_merger + (.5 * past_merger)])
        #plt.ylim([(-1 * max_value) - (.1 * max_value),max_value + (.1 * max_value)])
        #plt.ylim([-1,1])    
        
        nearest_ten_max = math.ceil(math.log10(max_value)) + 1
        nearest_ten_min = math.ceil(math.log10(min_value)) - 1
        
                
        
        plt.ylim([10**(nearest_ten_min), 10**(upper_limit_y)])

        plt.axes().set_yscale("log")
    
        matplotlib.rcParams.update({'font.size': 16})
        csfont = {'fontname':'Times New Roman'}

        plt.plot(split_data_x,split_data_y)


        plt.title(SimNames[j], **csfont)
        plt.xlabel("Time [M]", **csfont)
        plt.ylabel("|Phase Error| [rad]", **csfont)
        
        plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Plots_2\\"+str(past_merger)+"_Past_Merger_Log\\"+str(order)+"th_Order\\"+SimNames[j]+"_ErrPlot.png")
        plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Plots_2\\"+str(past_merger)+"_Past_Merger_Log\\"+str(order)+"th_Order\\"+SimNames[j]+"_ErrPlot.pdf")    
    
        plt.clf()    
    
        print(SimNames[j]+" is done")
