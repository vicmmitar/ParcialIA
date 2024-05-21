# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:36:28 2024

@author: vicmmitar
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X = data.data
y = data.target
print(X.shape, y.shape)

for i in range(10):
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.2)
    print(ytest)
    
#---
# Labelencoder y onehotencoder
miY1 = ['juan', 'maria', 'julio']

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
pepo = LabelEncoder()
etiqueta = pepo.fit_transform(miY1)
print("---")
print(etiqueta)


miY2 = [['Juan',1],['Maria',2],['Juio',3]]
pepo = OneHotEncoder()
etiqueta = pepo.fit_transform(miY2)
print("---")
print(etiqueta)

print(etiqueta.toarray())