# Arrays III
import numpy as np

# Ejemplo 1:
""" concatenate((arr1, arr2, ...), axis=0): sirve para concatenar o unir arreglos a lo largo de un eje especificado. 
arr1, arr2, ...: Son los arreglos que se desean concatenar. Deben ser proporcionados como una tupla.
axis: Especifica a lo largo de que eje se realizara la concatenacion. axis=0 para concatenar a lo largo de filas (verticalmente),
y axis=1 para concatenar a lo largo de columnas (horizontalmente).
"""
# Unimos dos arrays unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
# Salida: [1 2 3 4 5 6]

# Unimos dos arrays bidimensionales a lo largo de filas (Por defecto)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))
print(arr)
"""
Salida:
[[1 2] 
 [3 4] 
 [5 6] 
 [7 8]]
"""

# Unimos dos arrays bidimensionales a lo largo de filas con axis=0
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
"""
Salida:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

# Unimos dos arrays bidimensionales a lo largo de columnas con axis=1
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
"""
Salida:
[[1 2 5 6]
 [3 4 7 8]]
"""

print()

# Ejemplo 2:
""" array_split(array, indices_or_sections): se utiliza para dividir un array NumPy en sub-arrays de tamano igual o casi igual.
array: Es el array NumPy que se desea dividir en sub-arrays.
indices_or_sections: Puede ser un entero que indica el numero exacto de divisiones a realizar.
"""
# Dividimos un array en 3 partes
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
# Salida: [array([1, 2]), array([3, 4]), array([5, 6])]

# Dividimos un array en 4 partes
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
# Salida: [array([1, 2]), array([3, 4]), array([5]), array([6])]

print()

# Ejemplo 3:
# where(condicion): devuelve los indices de los elementos que cumplen una condicion especificada.
# Buscamos las posiciones donde se encuentra el elemento 4
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
# Salida: (array([3, 5, 6]),)

print()

# Ejemplo 4:
# sort(): ordena un array de menor a mayor
# Ordenamos un array de menor a mayor
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
# Salida: [0 1 2 3]