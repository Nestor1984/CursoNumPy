# Random II
from numpy import random

# Ejemplo 1:
# Generamos numeros aleatorios del 0 al 10, en un array de 20 posiciones
numeros = random.randint(10, size=(20))
print(numeros)
# Salida: [4 6 1 2 6 6 8 2 0 4 2 6 2 1 2 4 4 4 9 4]

# Generamos numeros aleatorios del 0 al 10, en una matriz de 3 filas y 5 columnas
numeros = random.randint(10, size=(3, 5))
print(numeros)
""" Salida:
[[6 1 9 0 7] 
 [6 5 5 3 2] 
 [8 7 9 1 1]]
"""

print()

# Ejemplo 2:
# Generamos numeros aleatorios del 0 al 1 (Sin incluir el 1), en un array de 5 posiciones
numeros = random.rand(5)
print(numeros)
# Salida: [0.24815733 0.63308306 0.74452243 0.55717514 0.91467539]

# Generamos numeros aleatorios del 0 al 1 (Sin incluir el 1), en una matriz de 3 filas y 5 columnas
numeros = random.rand(3, 5)
print(numeros)
""" Salida:
[[0.10304888 0.46071692 0.26833851 0.43392527 0.83733673] 
 [0.42638752 0.07472448 0.85947317 0.51465343 0.0045946 ] 
 [0.47011568 0.01154111 0.20899122 0.4291861  0.75287576]]
"""