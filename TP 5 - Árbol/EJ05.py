# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a) además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b) listar los villanos ordenados alfabéticamente;
# c) mostrar todos los superhéroes que empiezan con C;
# d) determinar cuántos superhéroes hay el árbol;
# e) Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
# f) listar los superhéroes ordenados de manera descendente;
# g) generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
#    I) determinar cuántos nodos tiene cada árbol;
#    II) realizar un barrido ordenado alfabéticamente de cada árbol.

from tree import BinaryTree

personajes = [
    {'nombre': 'Iron Man', 'is_villain': False},
    {'nombre': 'Captain America', 'is_villain': False},
    {'nombre': 'Thor', 'is_villain': False},
    {'nombre': 'Hulk', 'is_villain': False},
    {'nombre': 'Black Widow', 'is_villain': False},
    {'nombre': 'Hawkeye', 'is_villain': False},
    {'nombre': 'Spider-Man', 'is_villain': False},
    {'nombre': 'Black Panther', 'is_villain': False},
    {'nombre': 'Capitana Marvel', 'is_villain': False},
    {'nombre': 'Ant-Man', 'is_villain': False},
    {'nombre': 'Star-Lord', 'is_villain': False},
    {'nombre': 'Groot', 'is_villain': False},
    {'nombre': 'Dr Strange', 'is_villain': False},   # mal cargado a propósito (consigna e)
    {'nombre': 'Thanos', 'is_villain': True},
    {'nombre': 'Loki', 'is_villain': True},
    {'nombre': 'Ultron', 'is_villain': True},
    {'nombre': 'Hela', 'is_villain': True},
    {'nombre': 'Red Skull', 'is_villain': True},
    {'nombre': 'Killmonger', 'is_villain': True},
    {'nombre': 'Ego', 'is_villain': True}
]

# a) además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
arbol = BinaryTree()

for personaje in personajes:
    arbol.insert_node(personaje['nombre'], {'is_villain': personaje['is_villain']})

# b) listar los villanos ordenados alfabéticamente;
print()
print('-----B-----')
print()

print("Villanos ordenados alfabeticamente:")
arbol.inorden_villain()

# c) mostrar todos los superhéroes que empiezan con C;
print()
print('-----C-----')
print()

print("Superheroes que empiezan con C:")
arbol.inorden_hero_star_with('C')

# d) determinar cuántos superhéroes hay el árbol;
print()
print('-----D-----')
print()

print("Cantidad de superheroes:")
print(arbol.count_heroes())

# e) Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
print()
print('-----E-----')
print()

arbol.inorden()

print()
print("Nombre a corregir:")
arbol.proxy_search('strange')

personaje = arbol.search('Dr Strange')

if personaje is not None:
    datos = personaje.other_values
    arbol.delete_node('Dr Strange')
    arbol.insert_node('Doctor Strange', datos)

print()
arbol.inorden()

# f) listar los superhéroes ordenados de manera descendente;
print()
print('-----F-----')
print()

print("Superheroes ordenados de manera descendente:")
arbol.postorden_hero()

# g) generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
print()
print('-----G-----')
print()

arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def separar_personajes(root):
    if root is not None:
        if root.other_values['is_villain']:
            arbol_villanos.insert_node(root.value, root.other_values)
        else:
            arbol_heroes.insert_node(root.value, root.other_values)

        separar_personajes(root.left)
        separar_personajes(root.right)

separar_personajes(arbol.root)

#    I) determinar cuántos nodos tiene cada árbol;
def contar_nodos(root):
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)

print(f'Cantidad de superhéroes: {contar_nodos(arbol_heroes.root)}')
print(f'Cantidad de villanos: {contar_nodos(arbol_villanos.root)}')

#    II) realizar un barrido ordenado alfabéticamente de cada árbol.
print()
print('Superheroes ordenados alfabeticamente:')
arbol_heroes.inorden()

print()
print('Villanos ordenados alfabeticamente:')
arbol_villanos.inorden()