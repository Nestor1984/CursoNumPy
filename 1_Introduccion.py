"""
NumPy (Numerical Python): es una biblioteca fundamental para el calculo cientifico en Python. Proporciona
soporte para arreglos multidimensionales y matrices, junto con una coleccion de funciones matematicas para
operar sobre estos arreglos.

array(): se utiliza para crear un arreglo (o matriz) multidimensional a partir de una secuencia de datos,
como una lista o una tupla.
"""

import numpy as np # Importamos la libreria numpy con el alias de np

# Creamos un arreglo unidimensional, pasandole como argumento una lista
mi_array = np.array([1, 2, 3]) 
print(mi_array)
# Salida: [1 2 3]

print()

# Creamos un arreglo bidimensional (una matriz), pasandole como argumento una lista 2D
mi_array_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(mi_array_2)
"""
Salida:
[[1 2 3]
 [4 5 6]]
"""