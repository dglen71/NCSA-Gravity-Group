# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

'''
data_x = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_J0005.dat", usecols=(0))
data_y1 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_J0005.dat", usecols=(1))
data_y2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_J0005.dat", usecols=(2))
data_y3 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_J0005.dat", usecols=(3))

data_merger_x = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_J0005.dat", usecols=(4))
data_merger_y = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_J0005.dat", usecols=(5))


plt.plot(data_x,data_y1)
plt.plot(data_x,data_y2)
plt.plot(data_x,data_y3)
plt.plot(data_merger_x,data_merger_y)
plt.xlim([150,np.max(data_x) + 50])

plt.title("J0005")
plt.xlabel("Time [M]")
plt.ylabel("Phase [rad]")
'''

#Just error not phase


data_x = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_E0001.dat", usecols=(0))
data_y = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_E0001.dat", usecols=(1))

data_merger_x = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_E0001.dat", usecols=(2))
data_merger_y = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\Convergence\\Python_Data\\8th_Order\\exportDataCombined_E0001.dat", usecols=(3))

plt.axvline(x = data_merger_x[0], c='r')

#plt.plot(data_x,data_y)
#plt.plot(data_merger_x,data_merger_y,'r')
#neg_merger_x = data_merger_x
#neg_merger_y = -1 * data_merger_y
#plt.plot(neg_merger_x,neg_merger_y,'r')


index_start = 0
index_end = 0

past_merger = 150

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
max_value = np.max(split_data_y)
min_value = np.min(abs(split_data_y))
print(min_value)

plt.xlim([150,data_merger_x[0] + past_merger + (.5 * past_merger)])
#plt.ylim([(-1 * max_value) + (.1 * max_value),max_value + (.1 * max_value)])

#plt.ylim([10**-5, 10**2])
#print(np.log(max_value))

nearest_ten_max = math.ceil(math.log10(max_value)) + 1
print(nearest_ten_max)

nearest_ten_min = math.ceil(math.log10(min_value)) - 1
print(nearest_ten_min)

plt.ylim([10**(nearest_ten_min), 10**(nearest_ten_max)])

#extra_merger_x = data_merger_x
#extra_merger_y = data_merger_y + np.max(data_merger_y)
#plt.plot(extra_merger_x,extra_merger_y,'r')

matplotlib.rcParams.update({'font.size': 16})
csfont = {'fontname':'Times New Roman'}

plt.plot(split_data_x,split_data_y)

plt.axes().set_yscale("log")


#plt.plot(data_merger_x,data_merger_y,'r')
#neg_merger_x = data_merger_x
#neg_merger_y = -1 * data_merger_y
#plt.plot(neg_merger_x,neg_merger_y,'r')


plt.title("E0001", **csfont)
plt.xlabel("Time [M]", **csfont)
plt.ylabel("Error", **csfont)

plt.show()

