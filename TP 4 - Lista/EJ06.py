# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía,
# implementar la funciones necesarias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from list_ import List

superheroes = [
    {
      "nombre": "Spider-Man",
      "anio_aparicion": 1962,
      "casa": "Marvel",
      "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance en el Daily Bugle mientras protege Nueva York."
    },
    {
      "nombre": "Iron Man",
      "anio_aparicion": 1963,
      "casa": "Marvel",
      "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores y director de Stark Industries."
    },
    {
      "nombre": "Wolverine",
      "anio_aparicion": 1974,
      "casa": "Marvel",
      "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."
    },
    {
      "nombre": "Thor",
      "anio_aparicion": 1962,
      "casa": "DC",
      "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra. Miembro fundador de los Vengadores."
    },
    {
      "nombre": "Black Widow",
      "anio_aparicion": 1964,
      "casa": "Marvel",
      "biografia": "Natasha Romanoff fue entrenada desde niña en el programa Habitación Roja. Es una espía y agente de élite de S.H.I.E.L.D., experta en artes marciales y tecnología."
    },
    {
      "nombre": "Batman",
      "anio_aparicion": 1939,
      "casa": "DC",
      "biografia": "Bruce Wayne presenció el asesinato de sus padres de niño y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y entrenamiento físico para combatir el crimen. Usando un traje con muchas herramientas"
    },
    {
      "nombre": "Superman",
      "anio_aparicion": 1938,
      "casa": "DC",
      "biografia": "Kal-El fue enviado desde el planeta Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."
    },
    {
      "nombre": "Mujer Maravilla",
      "anio_aparicion": 1941,
      "casa": "DC",
      "biografia": "Diana, princesa de las Amazonas de la isla Temyscira, fue criada como guerrera. Porta el lazo de la verdad y las brazaletes indestructibles. Embajadora de paz y justicia."
    },
    {
      "nombre": "The Flash",
      "anio_aparicion": 1956,
      "casa": "DC",
      "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo durante un experimento. Obtuvo la capacidad de moverse a velocidades superlumínicas conectado a la Fuerza de la Velocidad."
    },
    {
      "nombre": "Green Lantern",
      "anio_aparicion": 1959,
      "casa": "DC",
      "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo. El anillo le permite crear construcciones de energía verde limitadas solo por su voluntad e imaginación."
    },
    {
      "nombre": "Dr Strange",
      "anio_aparicion": 1963,
      "casa": "DC",
      "biografia": "El Doctor Stephen Vincent Strange es un poderoso hechicero y miembro destacado de los Maestros de las Artes Místicas."
    },
    {
      "nombre": "Capitana Marvel",
      "anio_aparicion": 1968,
      "casa": "Marvel",
      "biografia": "La capitana Carol Susan Jane Danvers, princesa de Aladna, es una expiloto de la Fuerza Aérea de los Estados Unidos que, al exponerse a la energía del Teseracto mediante la destrucción del Motor de Velocidad Luz, obtuvo poderes cósmicos."
    },
    {
      "nombre": "Star-Lord",
      "anio_aparicion": 1976,
      "casa": "Marvel",
      "biografia": "Peter Jason Quill es un híbrido humano-celestial que fue secuestrado de la Tierra en 1988 por el Clan Saqueador de Yondu y criado como uno de sus miembros por Yondu, llegando a forjarse una reputación como el notorio forajido intergaláctico Star-Lord."
    }
]

class Superhero():
    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f'{self.name} - {self.year} - {self.house}'

def by_name(item):
    return item.name

list_heroes = List()
list_heroes.add_criterion('name', by_name)


for hero in superheroes:
    list_heroes.append(
        Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
    )

#a. eliminar el nodo que contiene la información de Linterna Verde;
print()
print('-----A-----')
print()
deleted_value = list_heroes.delete_value('Green Lantern', 'name')
print(f'Valor eliminado: {deleted_value}')


#b. mostrar el año de aparición de Wolverine;
print()
print('-----B-----')
print()

wolverine = list_heroes.search('Wolverine', 'name')
if wolverine is not None:
    print(f'El año de aparición de {list_heroes[wolverine].name} es {list_heroes[wolverine].year}')
else:
    print('No está en la lista')


#c. cambiar la casa de Dr. Strange a Marvel;
print()
print('-----C-----')
print()

dr_strange = list_heroes.search('Dr Strange', 'name')
if dr_strange is not None:
    list_heroes[dr_strange].house = 'Marvel'

print(list_heroes[dr_strange])


#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print()
print('-----D-----')
print()

print('Superhéroes con traje o armadura:')
list_heroes.filter_contain_on_bio(['traje', 'armadura'])


#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print()
print('-----E-----')
print()

print('Superhéroes que aparecieron antes de 1963:')
for hero in list_heroes:
    if hero.year < 1963:
        print(hero.name, hero.house)


#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print()
print('-----F-----')
print()

print('Casa a la que pertenece Capitana Marvel y Mujer Maravilla:')
cap_marvel = list_heroes.search('Capitana Marvel', 'name')
if cap_marvel is not None:
    print(f'{list_heroes[cap_marvel].name} pertenece a {list_heroes[cap_marvel].house}')

mujer_maravilla = list_heroes.search('Mujer Maravilla', 'name')
if mujer_maravilla is not None:
    print(f'{list_heroes[mujer_maravilla].name} pertenece a {list_heroes[mujer_maravilla].house}')


#g. mostrar toda la información de Flash y Star-Lord;
print()
print('-----G-----')
print()

print('Información de Flash y Star-Lord:')
for hero in list_heroes:
    if (hero.name == 'The Flash') or (hero.name == 'Star-Lord'):
        print(f'Nombre: {hero.name}')
        print(f'Año de aparición: {hero.year}')
        print(f'Casa: {hero.house}')
        print(f'Biografía: {hero.bio}')
        print()

#h. listar los superhéroes que comienzan con la letra B, M y S;
print()
print('-----H-----')
print()

print('Superhéroes que comienzan con la letra B, M y S:')
list_heroes.filter_start_with(('B', 'M', 'S'))


#i. determinar cuántos superhéroes hay de cada casa de comic.
print()
print('-----I-----')
print()

contador_marvel = 0
contador_dc = 0
for hero in list_heroes:
    if hero.house == 'Marvel':
        contador_marvel += 1
    elif hero.house == 'DC':
        contador_dc += 1
print(f'Cantidad de superhéroes que pertenecen a Marvel: {contador_marvel}')
print(f'Cantidad de superhéroes que pertenecen a DC: {contador_dc}')
#En la carga original hay 6 de Marvel y 7 de DC, pero con la eliminación de Linterna Verde (DC) y el cambio de Dr Strange (DC a Marvel) quedan 7 - 5


#Barrido de comprobación de cambios
print()
print('Lista de superhéroes:')
list_heroes.show()