# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad
# de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:

from stack import Stack

pila_mcu = Stack()
pila_mcu.push({'nombre': 'Iron Man', 'peliculas': 10})
pila_mcu.push({'nombre': 'Captain America', 'peliculas': 9})
pila_mcu.push({'nombre': 'Thor', 'peliculas': 8})
pila_mcu.push({'nombre': 'Black Widow', 'peliculas': 7})
pila_mcu.push({'nombre': 'Hulk', 'peliculas': 6})
pila_mcu.push({'nombre': 'Rocket Raccoon', 'peliculas': 4})
pila_mcu.push({'nombre': 'Hawkeye', 'peliculas': 5})
pila_mcu.push({'nombre': 'Spider-Man', 'peliculas': 5})
pila_mcu.push({'nombre': 'Doctor Strange', 'peliculas': 4})
pila_mcu.push({'nombre': 'Black Panther', 'peliculas': 4})
pila_mcu.push({'nombre': 'Scarlet Witch', 'peliculas': 6})
pila_mcu.push({'nombre': 'Groot', 'peliculas': 4})


# a) Determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila
def posicion_personaje(pila, nombre_personaje):
    pila_aux = Stack()
    posicion = 1
    encontrado = False
    
    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje['nombre'] == nombre_personaje:
            encontrado = True
            break
        posicion += 1
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return posicion if encontrado else -1

posicion_rocket = posicion_personaje(pila_mcu, 'Rocket Raccoon')
posicion_groot = posicion_personaje(pila_mcu, 'Groot')
print(f"Rocket Raccoon está en la posición: {posicion_rocket}")
print(f"Groot está en la posición: {posicion_groot}")


print()
# b) Determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece
def mas_de_5_peliculas(pila):
    personajes = []
    pila_aux = Stack()
    
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['peliculas'] > 5:
            personajes.append({'Nombre': personaje['nombre'], 'Peliculas': personaje['peliculas']})
        pila_aux.push(personaje)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return personajes

print("Personajes que participaron en más de 5 películas y su cantidad de películas:", mas_de_5_peliculas(pila_mcu))


print()
# c) Determinar en cuantas películas participo la Viuda Negra (Black Widow):')
def viuda_negra(pila, nombre_personaje):
    pila_aux = Stack()
    cantidad_peliculas = 0
    
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'] == nombre_personaje:
            cantidad_peliculas = personaje['peliculas']
        pila_aux.push(personaje)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return cantidad_peliculas

peliculas_black_widow = viuda_negra(pila_mcu, 'Black Widow')
print(f"Black Widow participó en {peliculas_black_widow} películas")


print()
# d) Mostrar todos los personajes cuyos nombre empiezan con C, D y G:')
def iniciales_personajes(pila, iniciales):
    personajes = []
    pila_aux = Stack()
    
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'][0] in iniciales:
            personajes.append(personaje['nombre'])
        pila_aux.push(personaje)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return personajes

print("Personajes cuyos nombres empiezan con C, D y G:", iniciales_personajes(pila_mcu, ['C', 'D', 'G']))