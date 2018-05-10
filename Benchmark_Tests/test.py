# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:10:16 2017

@author: Derek
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from astropy.extern.six.moves.urllib import request

data = np.loadtxt("C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\J0065\\carpet-timing..asc")

#V = np.loadtxt("C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\J0065\\carpet-timing..asc")

f = open('C:\\Users\\eagle\\Desktop\\Research\\Benchmark_Tests\\J0065\\carpet-timing..asc', 'r')

f.read()



print(data[:,3])


plt.plot(data[:,1],data[:,3], "bo")

plt.show()

