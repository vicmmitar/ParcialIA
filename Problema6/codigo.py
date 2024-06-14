# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 22:31:15 2024

@author: vicmmitar
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


import numpy as np
import pandas as pd

# Definir el separador personalizado
separador = ';'

# Cargar el archivo CSV con el separador personalizado en un DataFrame
df = pd.read_csv('./winequality-white.csv', delimiter=separador)

print(df.iloc[:, :11])

# Cargamos el conjunto de datos Iris
iris = datasets.load_iris()
X = df.iloc[:, :11]  # Las entradas son las características de las flores Iris
y = df["quality"]  # La salida esperada es la especie de cada flor Iris

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

cn = encoder.classes_
cn = cn[:].astype(str)


# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el modelo de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenamos el modelo con los datos de entrenamiento
clf.fit(X_train, y_train)

# Realizamos predicciones en los datos de prueba
y_pred = clf.predict(X_test)

# Calculamos la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
plt.figure(dpi=1200)

fn = X.columns
#cn = y.unique().toarray()

plot_tree(clf, filled=True, feature_names=fn, class_names=cn)
plt.show()