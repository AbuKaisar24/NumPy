# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:47:13 2019

@author: dcL
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show()
ar=np.array([1,2,3])
print(np.log10(ar))