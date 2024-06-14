# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:36:28 2024

@author: vicmmitar
"""

import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder

# Definir el separador personalizado
separador = ';'

# Cargar el archivo CSV con el separador personalizado en un DataFrame
df = pd.read_csv('./winequality-white.csv', delimiter=separador)

#-----------------One Hot Encoder--------------------------
clase= df["quality"].to_numpy()
clase_one_hot = OneHotEncoder().fit_transform(clase.reshape(-1,1)).toarray()
print(clase_one_hot)

#-----------------Escalado 2 ------------------------------
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_transformed = scaler.fit_transform(df)
print(data_transformed)

#-----------------Escalado 2 ------------------------------
from sklearn.preprocessing import MinMaxScaler
scaler2 = MinMaxScaler()
dato_escalado = scaler.fit_transform(df.iloc[:, :11])
print(dato_escalado)

#-----------------Escalado 3 ------------------------------
# se conserva los signos
from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
escalado3 = scaler.fit_transform(df.iloc[:, :11])
print(escalado3)

#-----------------Label encoder------------------------------
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
label_encoded = encoder.fit_transform(clase)
print(label_encoded)