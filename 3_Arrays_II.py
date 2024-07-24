# Arrays II
import numpy as np

# Ejemplo 1:
# shape(): devuelve una tupla de enteros que indican el tamano del arreglo en cada dimension
# Arrays de 4 elementos
mi_array = np.array([1, 2, 3, 4])
print(np.shape(mi_array))
# Salida: (4,)

# Matriz de 2 filas y 4 columnas
mi_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.shape(mi_array))
# Salida: (2, 4)

print()

# Ejemplo 2:
# reshape(): sirve para cambiar la forma de un arreglo multidimensional sin cambiar sus datos.
# Array Original
mi_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(mi_array)
"""
Salida:
[[1 2 3 4] 
 [5 6 7 8]]
"""
# Array Modificado
mi_array = mi_array.reshape(4, 2)
print(mi_array)
"""
Salida:
[[1 2]     
 [3 4]     
 [5 6]     
 [7 8]]
"""

print()

# Ejemplo 3:
# Iteramos un array bidimensional 
mi_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 
for fila in mi_array: # For para cada una de las filas de la matriz
    print(fila)
"""
Salida:
[1 2 3 4]
[5 6 7 8]
"""

# Iteramos un array tridimensional 
mi_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) 
for matriz in mi_array: # For para recorrer cada una de las caras
    for fila in matriz: # For para recorrer cada una de las filas de la matriz
        print(fila)
"""
Salida:
[1 2 3]
[4 5 6]
[7 8 9]
[10 11 12]
"""

# Iteramos los elementos de un array tridimensional 
mi_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) 
for matriz in mi_array: # For para recorrer cada una de las caras
    for fila in matriz: # For para recorrer cada una de las filas de la matriz
        for elemento in fila: # For para recorrer cada una de las columnas de la matriz
            print(elemento)
"""
Salida:
1
2
3
4
5
6
7
8
9
10
11
12
"""