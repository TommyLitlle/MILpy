# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:38:30 2016

@author: josemiguelarrieta
"""

import numpy as np

def MIL2SIL(*args):
    #Parameters
    args = list(args)
    bags = args[0] 
    labels = args[1] 

    bagT = [np.asmatrix(bag) for bag in bags]
    baglabT = np.asmatrix(labels).reshape((-1, 1))
    
    X = np.vstack(bagT)
    Y = np.vstack([float(cls) * np.matrix(np.ones((len(bags), 1)))
                               for bag, cls in zip(bagT, baglabT)])
    return X, Y