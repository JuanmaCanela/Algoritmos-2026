#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:


superheroes = [
    "Kang",
    "Hulk",
    "Black Widow",
    "Black Cat",
    "Iron Man",
    "Magneto",
    "Storm",
    "Venom",
    "Scarlet Witch",
    "Abomination",
    "Adam Warlock",
    "Angel",
    "Annihilus",
    "Ant Man",
    "Capitan America"
]


# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.

def buscar_capitan(lista, indice=0):
    if indice >= len(lista):
        return False
    elif lista[indice] == "Capitan America":
        return True
    else:
        return buscar_capitan(lista, indice + 1)


# funcion recursiva para listar los superheroes de la lista.

def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return

    print(lista[indice])
    listar_superheroes(lista, indice + 1)


# prueba

if buscar_capitan(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")

print()

print("Lista de superhéroes:")
listar_superheroes(superheroes)