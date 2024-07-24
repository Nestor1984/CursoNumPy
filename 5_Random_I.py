# Random I
from numpy import random # De la libreria numpy importamos el modulo random

# Ejemplo 1:
# randint(): Genera numeros enteros aleatorios dentro de un rango especificado.
# Generamos numeros enteros aleatorios del 0 al 9
for x in range(50):
    numero = random.randint(10)
    print(numero)
    
"""
Salida:
0
9
8
4
4
4
3
4
8
4
6
9
1
1
1
1
2
7
2
2
7
5
8
1
3
4
6
8
2
2
8
4
8
1
0
8
3
1
9
6
0
6
0
4
7
7
2
9
0
3
"""

print()

# Ejemplo 2:
# rand(): Genera numeros decimales aleatorios entre 0 y 1.
# Generamos un numero decimal entre 0 y 1 (Sin incluir el 1)
numero = random.rand()
print(numero)
# Salida: 0.0848725217412224

# Generamos un numero decimal entre 0 y 1 (Sin incluir el 1), con 3 decimales
numero = random.rand()
print(round(numero, 3))
# Salida: 0.379

# Generamos numeros aleatorios decimales entre 5 y 6 (Sin incluir el 6),  con 3 decimales
numero = random.rand()
print(round(numero, 3) + 5)
# Salida: 5.998