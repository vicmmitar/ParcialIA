# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 03:32:07 2024

@author: vicmmitar
"""

from itertools import permutations

def obtener_permutaciones(lista):
    longitud = len(lista)
    permutaciones = []
    for i in range(2, longitud + 1):
        permutaciones.extend(permutations(lista, i))
    return permutaciones

# Ejemplo de uso
lista = [0, 1, 2, 3, 4, 5, 6, 7]
print(obtener_permutaciones(lista))


