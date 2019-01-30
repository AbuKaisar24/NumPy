# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:24:50 2019

@author: dcL
"""
import numpy as np
import matplotlib.pyplot as plt
 # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 4, 0.5
v = np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=10, density=1)       # matplotlib version (plot)
plt.show()
