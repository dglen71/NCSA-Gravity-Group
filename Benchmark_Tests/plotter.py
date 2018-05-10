# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 23:18:35 2017

@author: Derek
"""
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
from itertools import cycle

cycol_opt= cycle('bgr')
cycol_max= cycle('bgr')
cymark = cycle('>o^s*D')

names = ["J0065", "J0069", "L0037", "P0001", "P0005", "P0009"]
res = [32,36,40]
nodes=[3,5,7,10,13,16]

for i in range(len(names)):
    
    mark = next(cymark)
    
    for j in range(len(res)):
        
        T_opt = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\Data\\"+names[i]+"_N"+str(res[j])+"_10..asc", usecols=(1))
        V_opt = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\Data\\"+names[i]+"_N"+str(res[j])+"_10..asc", usecols=(3))
        
        T_max = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\Data\\"+names[i]+"_N"+str(res[j])+"_16..asc", usecols=(1))
        V_max = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\Data\\"+names[i]+"_N"+str(res[j])+"_16..asc", usecols=(3))
        
        max_opt = np.max(V_opt)
        index_opt = 0
        for k in range(len(V_opt)):
            if V_opt[k] == max_opt:
                index_opt = k
                
        max_max = np.max(V_max)
        index_max = 0
        for k in range(len(V_max)):
            if V_max[k] == max_max:
                index_max = k

                
        plt.plot(10, max_opt, marker = mark, ms = 7, c = next(cycol_opt))
        plt.plot(16, max_max, marker = mark, ms = 10, c = next(cycol_max))

        

plt.xlim([9,17])

plt.show()


