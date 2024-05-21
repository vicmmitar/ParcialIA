# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:36:27 2024

@author: vicmmitar
"""

import random
import numpy

individual = random.sample(range(5),5)
print(individual)
distancia = numpy.array([[0,2,4,3,6],[2,0,4,3,3],[4,4,0,7,3],[3,3,7,0,5],[6,3,3,5,0]])
suma=0
for i in range(len(individual)):
    if i==len(individual)-1:
        suma+=distancia[individual[i],individual[0]]
        print(i,0)
    else:
        suma+=distancia[individual[i],individual[i+1]]
        print(i, i+1)
print(suma)