# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:38:21 2019

@author: dcL
"""

import numpy as np
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(7,8,9),(10,11,12)])
print(a.sum(axis=1))
print(np.std(a))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(a.ravel())