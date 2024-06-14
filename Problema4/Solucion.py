# -*- coding: utf-8 -*-
"""
Created on Tue May 21 06:37:00 2024

@author: vicmmitar
"""

import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos y relaciones (aristas)
# Estructura básica: G.add_edge('parent', 'child')

# Ejemplo con una familia ficticia
G.add_edge('Inocencio', 'Cristina')  # Inocencio es padre de Cristina
G.add_edge('Inocencio', 'Mercedes')   # Inocencio es padre de Mercedes
G.add_edge('Inocencio', 'Hilda')   # Inocencio es padre de Hilda
G.add_edge('Inocencio', 'Raul')   # Inocencio es padre de Raul
G.add_edge('Inocencio', 'Gonzalo')   # Inocencio es padre de Gonzalo
G.add_edge('Manuela', 'Cristina')   # Manuela es madre de Cristina
G.add_edge('Manuela', 'Mercedes')    # Manuela es madre de Mercedes
G.add_edge('Manuela', 'Hilda')   # Manuela es madre de Hilda
G.add_edge('Manuela', 'Raul')   # Manuela es madre de Raul
G.add_edge('Manuela', 'Gonzalo')   # Manuela es madre de Gonzalo

G.add_edge('Felipe', 'Rene')
G.add_edge('Felipe', 'Yola')
G.add_edge('Felipe', 'Zenobia')
G.add_edge('Felipe', 'Nelly')
G.add_edge('Felipe', 'Grover')
G.add_edge('Felipe', 'Fredy')
G.add_edge('Benita', 'Rene')
G.add_edge('Benita', 'Yola')
G.add_edge('Benita', 'Zenobia')
G.add_edge('Benita', 'Nelly')
G.add_edge('Benita', 'Grover')
G.add_edge('Benita', 'Fredy')

G.add_edge('Fredy', 'Victor')
G.add_edge('Cristina', 'Victor')

G.add_edge('Mercedes', 'Wilma')
G.add_edge('Winsor', 'Wilma')

G.add_edge('Gonzalo', 'Goni')
G.add_edge('Elena', 'Goni')

G.add_edge('Gonzalo', 'Jose')
G.add_edge('Elena', 'Jose')

G.add_edge('Hilda', 'Toto')
G.add_edge('Adolfo', 'Toto')

def get_parents(G, person):
    return list(G.predecessors(person))

def get_children(G, person):
    return list(G.successors(person))

def get_grandparents(G, person):
    parents = get_parents(G, person)
    grandparents = []
    for parent in parents:
        grandparents.extend(get_parents(G, parent))
    return grandparents

def get_grandchildren(G, person):
    children = get_children(G, person)
    grandchildren = []
    for child in children:
        grandchildren.extend(get_children(G, child))
    return grandchildren

def get_siblings(G, person):
    parents = get_parents(G, person)
    siblings = set()
    for parent in parents:
        siblings.update(get_children(G, parent))
    siblings.discard(person)
    return list(siblings)

def get_uncles_aunts(G, person):
    parents = get_parents(G, person)
    uncles_aunts = set()
    for parent in parents:
        uncles_aunts.update(get_siblings(G, parent))
    return list(uncles_aunts)

def get_cousins(G, person):
    uncles_aunts = get_uncles_aunts(G, person)
    cousins = set()
    for uncle_aunt in uncles_aunts:
        cousins.update(get_children(G, uncle_aunt))
    return list(cousins)
print("Padres de Victor:", get_parents(G, 'Victor'))
print("Hijos de Manuela:", get_children(G, 'Manuela'))
print("Abuelos de Victor:", get_grandparents(G, 'Victor'))
print("Nietos de Inocencio:", get_grandchildren(G, 'Inocencio'))
print("Hermanos de Cristina:", get_siblings(G, 'Cristina'))
print("Tíos y tías de Victor:", get_uncles_aunts(G, 'Victor'))
print("Primos de Wilma:", get_cousins(G, 'Wilma'))