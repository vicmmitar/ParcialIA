# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:51:30 2024

@author: vicmmitar
"""

import pandas as pd

# Definir el separador personalizado
separador = ';'

# Cargar el archivo CSV con el separador personalizado en un DataFrame
df = pd.read_csv('./winequality-white.csv', delimiter=separador)

# Realizar operaciones con el DataFrame cargado
print(df.quantile(.75))

import csv
import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort

def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


# funcion que devuelve el quartil
def cuartil(array, a):
    
    array = quicksort(array)
    q=(a*(len(array)+1))/4
    parte_entera = int(q)
    parte_decimal = abs(q) - abs(int(q))
    q=array[parte_entera-1]+(parte_decimal*(array[parte_entera]-array[parte_entera-1]))

    return q

# funcion que calcula el percentil
def percentil(array, k):
    array = quicksort(array)
    frec = [[],[],[]]
    x = array[0]
    f = 0
    fa=0
    for i in array:
        if i==x:
            f+=1
        else:
            fa += f    
        
        if(i>x):
            x = i
            frec[0].append(x)
            frec[1].append(f)
            f=1
            frec[2].append(fa)
    frec[1].append(f)
    frec[2].append(fa+1)
    #print(frec)
    pos = k*len(array)
    #print(pos)
    for i in range(len(frec[2])-1):
        if(frec[2][i]>pos):
            #print(frec[2][i])
            break
        anterior = frec[2][i]
        fi = frec[1][i]
        li = frec[0][i]
    
    return li 

def volcarPercentil(array, p):
    array = quicksort(array)
    volcado = []
    for i in array:
        if(i <= p):
            volcado.append(i)
        else:
            break
    print(volcado)
    return volcado

# Abrir el archivo CSV en modo lectura
with open('./winequality-white.csv', 'r') as file:
    # Crear un lector CSV
    reader = csv.reader(file)
    #fixed acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality = []
    nombres = []
    bd = [[],[],[],[],[],[],[],[],[],[],[],[]]
    idx = 0
    # Leer cada fila del archivo CSV
    for fila in reader:
        # Procesar los datos de cada fila
        datos = fila[0].split(";")
        for i in range(len(datos)):
            if(idx<=0):
                nombres.append(datos[i])
            else:
                bd[i].append(float(datos[i]))
        idx+=1
    cuartil3 = []
    percentil80 = []
for i in bd:
    cuartil3.append(cuartil(i, 3))
    percentil80.append(percentil(i, 0.8))
    
print("Cuartil 3")
for i in range(len(nombres)-1):
    print(nombres[i],":",cuartil3[i])
    
print(df.quantile(.8))
    
print("Percentil 80")
for i in range(len(nombres)-1):
    print(nombres[i],":",percentil80[i])

print("Cuartil 3 NUMPY")
for i in range(len(nombres)-1):
    print(nombres[i],":",np.percentile(bd[i], 75))
    
print("Percentil 80 NUMPY")
for i in range(len(nombres)-1):
    print(nombres[i],":",np.percentile(bd[i], 80))

media = df.mean()
mediana = df.median()
moda = df.mode()
print(media,mediana,moda)

import matplotlib.pyplot as plt
plt.style.use("bmh")            #Declaración del estilo
#Opción 2
plt.plot()                      #Creación de una gráfica de línea

x_values = df['fixed acidity'].unique()
y_values = df['fixed acidity'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.show()
plt.close('all')
