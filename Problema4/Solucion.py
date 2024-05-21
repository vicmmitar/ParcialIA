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
G.add_edge('Inocencio', 'Cristina')  # Juan es padre de Carlos
G.add_edge('Inocencio', 'Mercedes')   # Juan es padre de Maria
G.add_edge('Manuela', 'Cristina')   # Ana es madre de Carlos
G.add_edge('Manuela', 'Mercedes')    # Ana es madre de Maria
G.add_edge('Fredy', 'Victor')  # Carlos es padre de Luis
#G.add_edge('Carlos', 'Eva')   # Carlos es padre de Eva
G.add_edge('Cristina', 'Victor')   # Sofia es madre de Luis
#G.add_edge('Sofia', 'Eva')    # Sofia es madre de Eva
G.add_edge('Mercedes', 'Wilma')  # Maria es madre de Pedro
G.add_edge('Mercedes', 'Wilma')  # David es padre de Pedro
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