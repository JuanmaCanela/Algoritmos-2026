#Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:

from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes


class SuperHero:

    def __init__(self, datos):
        self.name = datos["name"]
        self.real_name = datos["real_name"]
        self.first_appearance = datos["first_appearance"]
        self.short_bio = datos["short_bio"]
        self.is_villain = datos["is_villain"]
    
    def __str__(self):
        return (f"Nombre: {self.name}, "
            f"Nombre real: {self.real_name}, "
            f"Año: {self.first_appearance}, "
            f"Villano: {self.is_villain}")

lista = List()

for personaje in superheroes:
    lista.append(SuperHero(personaje))

# Listado ordenado de manera ascendente por nombre de los personajes.

print("a) Personajes ordenados por nombre:")
print()
def by_name(item):
        return item.name

lista.add_criterion("name", by_name)
lista.sort_by_criterion("name")

for personaje in lista:
    print(personaje.name)


# Determinar en que posicion esta The Thing y Rocket Raccoon.
print()
print("b) Posición de The Thing y Rocket Raccoon:")
print()

pos_thing = lista.search("The Thing", "name")
pos_rocket = lista.search("Rocket Raccoon", "name")

if pos_thing is not None:
    print("The Thing está en la posición:", pos_thing)

if pos_rocket is not None:
    print("Rocket Raccoon está en la posición:", pos_rocket)


# Listar todos los villanos de la lista.
print()
print("c) Villanos:")
print()

for personaje in lista:
    if personaje.is_villain:
        print(personaje.name)


# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

cola_villanos = Queue()

for personaje in lista:
    if personaje.is_villain:
        cola_villanos.arrive(personaje)

print()
print("d) Villanos aparecidos antes de 1980:")
print()

cantidad = cola_villanos.size()

for i in range(cantidad):
    villano = cola_villanos.attention()

    if villano.first_appearance < 1980:
        print(villano.name, "-", villano.first_appearance)

    cola_villanos.arrive(villano)


# Listar los superheores que comienzan con Bl, G, My, y W.
print()
print("e) Superhéroes que comienzan con Bl, G, My y W:")
print()

for personaje in lista:
    nombre = personaje.name

    if (nombre.startswith("Bl")
            or nombre.startswith("G")
            or nombre.startswith("My")
            or nombre.startswith("W")):

        print(nombre)


# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
print()
print("f) Personajes ordenados por nombre real:")
print()

def by_real_name(item):
    if item.real_name is None:
        return ""
    return item.real_name

lista.add_criterion("real_name", by_real_name)
lista.sort_by_criterion("real_name")

for personaje in lista:
    print(personaje.real_name, "-", personaje.name)


# Listado de superheroes ordenados por fecha de aparación.
print()
print("g) Personajes ordenados por fecha de aparición:")
print()

def by_first_appearance(item):
    return item.first_appearance

lista.add_criterion("first_appearance", by_first_appearance)

lista.sort_by_criterion("first_appearance")

for personaje in lista:
    print(personaje.first_appearance, "-", personaje.name)


# Modificar el nombre real de Ant Man a Scott Lang.
print()
print("h) Modificar nombre real de Ant Man:")
print()

pos = lista.search("Ant Man", "name")

if pos is not None:
    lista[pos].real_name = "Scott Lang"
    print("Datos actualizados:")
    print(lista[pos])
else:
    print("Ant Man no se encuentra en la lista.")


# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print()
print("i) Personajes cuya biografía contiene 'time-traveling' o 'suit':")
print()

for personaje in lista:
    biografia = personaje.short_bio.lower()

    if "time-traveling" in biografia or "suit" in biografia:
        print(personaje.name)


# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
print()
print("j) Eliminación de Electro y Baron Zemo:")
print()

pos = lista.search("Electro", "name")

if pos is not None:
    eliminado = lista.delete_value("Electro", "name")
    print("Se eliminó:")
    print(eliminado)
else:
    print("Electro no está en la lista.")

print()
pos = lista.search("Baron Zemo", "name")

if pos is not None:
    eliminado = lista.delete_value("Baron Zemo", "name")
    print("Se eliminó:")
    print(eliminado)
else:
    print("Baron Zemo no está en la lista.")