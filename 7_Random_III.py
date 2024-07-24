# Random III
from numpy import random

# Ejemplo:
# choice(lista): Nos permite escoger aleatoriamente un elemento
# Generamos un ganador
lista_nombres = ["Alberto", "Alfonso", "Lucia", "Isabel", "Marcos", "Sergio"]
ganador = random.choice(lista_nombres)
print("El ganador del sorteo es " + ganador)
# Salida: El ganador del sorteo es Marcos

# Generamos tres ganadores
lista_nombres = ["Alberto", "Alfonso", "Lucia", "Isabel", "Marcos", "Sergio"]
ganador = random.choice(lista_nombres, size=(3))
print(ganador)
# Salida: ['Alfonso' 'Alfonso' 'Marcos']

# Generamos una matriz de 3 x 5, con elementos al azar
lista_nombres = ["Alberto", "Alfonso", "Lucia", "Isabel", "Marcos", "Sergio"]
ganador = random.choice(lista_nombres, size=(3, 5))
print(ganador)
""" Salida:
[['Alfonso' 'Alberto' 'Alberto' 'Alberto' 'Lucia']
 ['Isabel' 'Sergio' 'Marcos' 'Lucia' 'Marcos']
 ['Isabel' 'Sergio' 'Marcos' 'Isabel' 'Marcos']]
"""