# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas derrotas y cantidad de batallas victorias.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

from list_ import List
from random import randint, choice


entrenadores = [

    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },

    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },

    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },

    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },

    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]


pokemons = [

    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },

    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },

    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },

    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },

    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },

    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },

    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },

    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },

    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },

    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },

    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },

    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },

    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },

    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    },

    {
        "nombre": "Tyrantrum",
        "nivel": 50,
        "tipo": "Roca",
        "subtipo": "Dragón"
    },

    {
        "nombre": "Terrakion",
        "nivel": 55,
        "tipo": "Roca",
        "subtipo": "Lucha"
    },

    {
        "nombre": "Wingull",
        "nivel": 15,
        "tipo": "Agua",
        "subtipo": "Volador"
    }
]


class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - Nivel: {self.nivel} - Tipo: {self.tipo} - Subtipo: {self.subtipo}'


class Entrenador:

    def __init__(self, nombre, torneos, derrotas, victorias):
        self.nombre = nombre
        self.torneos = torneos
        self.derrotas = derrotas
        self.victorias = victorias
        self.pokemons = []

    def __str__(self):
        return f'{self.nombre} - Torneos ganados: {self.torneos} - Victorias: {self.victorias} - Derrotas: {self.derrotas}'


def by_name(item):
    return item.nombre.lower()


lista_pokemons = List()

for pokemon in pokemons:
    lista_pokemons.append(Pokemon(pokemon['nombre'], pokemon['nivel'], pokemon['tipo'], pokemon['subtipo']))


lista_entrenadores = List()

for entrenador in entrenadores:
    lista_entrenadores.append(Entrenador(entrenador['nombre'], entrenador['torneos_ganados'], entrenador['batallas_perdidas'], entrenador['batallas_ganadas']))


lista_entrenadores.add_criterion('name', by_name)


for entrenador in lista_entrenadores:
    cantidad = randint(2, 5)
    for i in range(cantidad):
        pokemon = choice(lista_pokemons)
        entrenador.pokemons.append(pokemon)


# a. obtener la cantidad de Pokémons de un determinado entrenador;
print()
print('-----A-----')
print()

buscado = lista_entrenadores.search(input('Ingrese el nombre del entrenador a buscar:').lower(), 'name')
if buscado is not None:
    print(f'Cantidad de Pokémons de {lista_entrenadores[buscado].nombre}: {len(lista_entrenadores[buscado].pokemons)}')
else:
    print('No está en la lista')


# b. listar los entrenadores que hayan ganado más de tres torneos;
print()
print('-----B-----')
print()

print('Entrenadores que ganaron más de 3 torneos:')

for entrenador in lista_entrenadores:
    if entrenador.torneos > 3:
        print(f'{entrenador.nombre}: {entrenador.torneos}')


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print()
print('-----C-----')
print()

mas_torneos = lista_entrenadores[0]

for entrenador in lista_entrenadores:
    if entrenador.torneos > mas_torneos.torneos:
        mas_torneos = entrenador

mayor_nivel = mas_torneos.pokemons[0]

for pokemon in mas_torneos.pokemons:
    if pokemon.nivel > mayor_nivel.nivel:
        mayor_nivel = pokemon

print(f'Entrenador con más torneos ganados: {mas_torneos.nombre} con {mas_torneos.torneos} torneos.')
print(f'Pokémon de mayor nivel: {mayor_nivel}')


# d. mostrar todos los datos de un entrenador y sus Pokémos;
print()
print('-----D-----')
print()

for entrenador in lista_entrenadores:

    print()
    print(f'Nombre: {entrenador.nombre}')
    print(f'Torneos ganados: {entrenador.torneos}')
    print(f'Batallas derrotas: {entrenador.derrotas}')
    print(f'Batallas victorias: {entrenador.victorias}')

    print('Pokémons:')

    for pokemon in entrenador.pokemons:

        print(f'> {pokemon}')


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print()
print('-----E-----')
print()

print('Entrenadores que ganaron más del 79% de las batallas:')

for entrenador in lista_entrenadores:
    total_batallas = entrenador.victorias + entrenador.derrotas
    porcentaje = entrenador.victorias * 100 / total_batallas

    if porcentaje > 79:
        print(f'{entrenador.nombre} - {round(porcentaje, 2)} %')


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print()
print('-----F-----')
print()

print('Entrenadores con Pokémons de tipo fuego/planta o agua/volador:')
for entrenador in lista_entrenadores:
    for pokemon in entrenador.pokemons:
        if ((pokemon.tipo == 'Fuego' and pokemon.subtipo == 'Planta') or (pokemon.tipo == 'Agua' and pokemon.subtipo == 'Volador')):
            print(f'{entrenador.nombre} > {pokemon}')


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print()
print('-----G-----')
print()

def promedio_nivel(entrenador):
    suma = 0
    for pokemon in entrenador.pokemons:
        suma += pokemon.nivel
    return suma / len(entrenador.pokemons)

buscado = lista_entrenadores.search(input('Ingrese el nombre del entrenador a buscar:'), 'name')
if buscado is not None:
    print(f'Promedio de nivel de los Pokémons de {lista_entrenadores[buscado].nombre}: {round(promedio_nivel(lista_entrenadores[buscado]), 2)}')
else:
    print('No está en la lista')



# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print()
print('-----H-----')
print()

nombre_pokemon = input('Ingrese el nombre del Pokémon para buscar cuántos entrenadores lo tienen: ')

contador = 0

for entrenador in lista_entrenadores:
    for pokemon in entrenador.pokemons:
        if pokemon.nombre.lower() == nombre_pokemon.lower():
            contador += 1
            break


print(f'Cantidad de entrenadores que tienen a {nombre_pokemon.capitalize()}: {contador}')


# i. mostrar los entrenadores que tienen Pokémons repetidos;
print()
print('-----I-----')
print()

print('Entrenadores que tienen Pokémons repetidos:')

for entrenador in lista_entrenadores:
    repetidos = False
    for i in range(len(entrenador.pokemons)):
        for j in range(i + 1, len(entrenador.pokemons)):
            if entrenador.pokemons[i].nombre == entrenador.pokemons[j].nombre:
                repetidos = True

    if repetidos:
        print(entrenador.nombre)


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
print()
print('-----J-----')
print()

print('Entrenadores que tienen a Tyrantrum, Terrakion o Wingull:')

pokemon_buscados = ['Tyrantrum', 'Terrakion', 'Wingull']

for entrenador in lista_entrenadores:
    encontrado = False
    for pokemon in entrenador.pokemons:
        if pokemon.nombre in pokemon_buscados:
            encontrado = True
    if encontrado:
        print(entrenador.nombre)


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
print()
print('-----K-----')
print()

nombre_entrenador = input('Ingrese el nombre del entrenador: ').lower()

nombre_pokemon = input('Ingrese el nombre del Pokémon: ').lower()

entrenador_encontrado = None

for entrenador in lista_entrenadores:
    if entrenador.nombre.lower() == nombre_entrenador.lower():
        entrenador_encontrado = entrenador


if entrenador_encontrado is not None:
    pokemon_encontrado = None
    for pokemon in entrenador_encontrado.pokemons:
        if pokemon.nombre.lower() == nombre_pokemon.lower():
            pokemon_encontrado = pokemon

    if pokemon_encontrado is not None:
        print()
        print('El entrenador tiene ese Pokémon.')
        print()
        print('Datos del entrenador:')
        print(entrenador_encontrado)
        print()
        print('Datos del Pokémon:')
        print(pokemon_encontrado)

    else:
        print(f'El entrenador {entrenador_encontrado.nombre}, no tiene al Pokémon {nombre_pokemon.capitalize()}')

else:
    print('No se encontró al entrenador.')
