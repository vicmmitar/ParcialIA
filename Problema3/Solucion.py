# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:36:28 2024

@author: vicmmitar
"""

import numpy as np
import pandas as pd

# Definir el separador personalizado
separador = ';'

# Cargar el archivo CSV con el separador personalizado en un DataFrame
df = pd.read_csv('./winequality-white.csv', delimiter=separador)

salida_esperada = df["quality"]

salida_esperada_one_hot = np.zeros((df["quality"].size, salida_esperada.max()+1))
#print(salida_esperada_one_hot)
salida_esperada_one_hot[np.arange(salida_esperada.size), salida_esperada] = 1
#print(salida_esperada_one_hot)

print(df.columns)

