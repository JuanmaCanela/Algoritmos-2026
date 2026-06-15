#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su
# género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades: 
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel; 
# b. mostrar los nombre de los superhéroes femeninos; 
# c. mostrar los nombres de los personajes masculinos; 
# d. determinar el nombre del superhéroe del personaje Scott Lang; 
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S; 
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes. 

from queue_ import Queue

personajes = Queue()

personajes.arrive({
    'personaje': 'Tony Stark',
    'superheroe': 'Iron Man',
    'genero': 'M'
})

personajes.arrive({
    'personaje': 'Steve Rogers',
    'superheroe': 'Capitán América',
    'genero': 'M'
})

personajes.arrive({
    'personaje': 'Natasha Romanoff',
    'superheroe': 'Black Widow',
    'genero': 'F'
})

personajes.arrive({
    'personaje': 'Carol Danvers',
    'superheroe': 'Capitana Marvel',
    'genero': 'F'
})

personajes.arrive({
    'personaje': 'Scott Lang',
    'superheroe': 'Ant-Man',
    'genero': 'M'
})

personajes.arrive({
    'personaje': 'Stephen Strange',
    'superheroe': 'Doctor Strange',
    'genero': 'M'
})


# a) Determinar el nombre del personaje de la superhéroe Capitana Marvel; 

def personaje_capitana_marvel(cola):
    cantidad = cola.size()

    for i in range(cantidad):
        dato = cola.attention()

        if dato['superheroe'] == 'Capitana Marvel':
            print("Capitana Marvel es:", dato['personaje'])

        cola.arrive(dato)


# b) Mostrar los nombre de los superhéroes femeninos

def superheroes_femeninos(cola):
    cantidad = cola.size()

    print("Superhéroes femeninos:")

    for i in range(cantidad):
        dato = cola.attention()

        if dato['genero'] == 'F':
            print(dato['superheroe'])

        cola.arrive(dato)


# c) Mostrar los nombres de los personajes masculinos

def personajes_masculinos(cola):
    cantidad = cola.size()

    print("Personajes masculinos:")

    for i in range(cantidad):
        dato = cola.attention()

        if dato['genero'] == 'M':
            print(dato['personaje'])

        cola.arrive(dato)


# d) Determinar el nombre del superhéroe del personaje Scott Lang

def superheroe_scott_lang(cola):
    cantidad = cola.size()

    for i in range(cantidad):
        dato = cola.attention()

        if dato['personaje'] == 'Scott Lang':
            print("Scott Lang es:", dato['superheroe'])

        cola.arrive(dato)


# e) Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S

def nombres_con_s(cola):
    cantidad = cola.size()

    print("Datos cuyos nombres comienzan con S:")

    for i in range(cantidad):
        dato = cola.attention()

        if (dato['personaje'][0] == 'S'
                or dato['superheroe'][0] == 'S'):
            print(dato)

        cola.arrive(dato)


# f) Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes

def buscar_carol_danvers(cola):
    cantidad = cola.size()
    encontrado = False

    for i in range(cantidad):
        dato = cola.attention()

        if dato['personaje'] == 'Carol Danvers':
            encontrado = True
            print("Carol Danvers está en la cola.")
            print("Su superhéroe es:", dato['superheroe'])

        cola.arrive(dato)

    if not encontrado:
        print("Carol Danvers no está en la cola.")


personaje_capitana_marvel(personajes)

print()
superheroes_femeninos(personajes)

print()
personajes_masculinos(personajes)

print()
superheroe_scott_lang(personajes)

print()
nombres_con_s(personajes)

print()
buscar_carol_danvers(personajes)