# Arrays I

import numpy as np

# Array de dimension 0
mi_array = np.array(23)
print(mi_array)
# Salida: 23

print()

# Array de una dimension
mi_array = np.array([23, 42, 81])
print(mi_array)
# Salida: [23 42 81]

print()

# Array de dos dimensiones
mi_array = np.array([[23, 42, 81], [5, 7, 8]])
print(mi_array)
""" Salida:
[[23 42 81]
 [ 5  7  8]] """
 
print()
 
# Array de tres dimensiones
mi_array = np.array([[[23, 42, 81], [5, 7, 8]], [[12, 8, 27], [11, 13, 14]]])
print(mi_array)
""" Salida:
[[[23 42 81]  
  [ 5  7  8]] 

 [[12  8 27]  
  [11 13 14]]] """

print()

# ndim: imprime la dimension de un array
mi_array = np.array([[23, 42, 81], [5, 7, 8]])
print(mi_array.ndim)
# Salida: 2

print()

# Accedemos al ultimo elemento del array
mi_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(mi_array[9])
# Salida:  10

print()

# Tomamos desde el elemento 4 al 7 incluido
mi_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(mi_array[3:7]) # NOTA: El primer indice cuenta desde 0 y el segundo desde 1
# Salida: [4 5 6 7]

print()

# De la segunda fila de la matriz accedemos al tercer elemento
mi_array = np.array([[1, 2, 3], [4, 5, 6]])
print(mi_array[1, 2]) 
# Salida: 6

print()

# De la matriz de atras, de la primera de fila de la matriz, accedemos al segundo elemento
mi_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(mi_array[1, 0, 1])
# Salida: 8