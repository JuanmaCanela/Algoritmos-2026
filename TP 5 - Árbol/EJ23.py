# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tree import BinaryTree
from heap import HeapMax

criaturas = [
    {'nombre': 'Ceto', 'derrotado_por': None},
    {'nombre': 'Tifón', 'derrotado_por': 'Zeus'},
    {'nombre': 'Equidna', 'derrotado_por': 'Argos Panoptes'},
    {'nombre': 'Dino', 'derrotado_por': None},
    {'nombre': 'Pefredo', 'derrotado_por': None},
    {'nombre': 'Enio', 'derrotado_por': None},
    {'nombre': 'Escila', 'derrotado_por': None},
    {'nombre': 'Caribdis', 'derrotado_por': None},
    {'nombre': 'Euríale', 'derrotado_por': None},
    {'nombre': 'Esteno', 'derrotado_por': None},
    {'nombre': 'Medusa', 'derrotado_por': 'Perseo'},
    {'nombre': 'Ladón', 'derrotado_por': 'Heracles'},
    {'nombre': 'Águila del Cáucaso', 'derrotado_por': None},
    {'nombre': 'Quimera', 'derrotado_por': 'Belerofonte'},
    {'nombre': 'Hidra de Lerna', 'derrotado_por': 'Heracles'},
    {'nombre': 'León de Nemea', 'derrotado_por': 'Heracles'},
    {'nombre': 'Esfinge', 'derrotado_por': 'Edipo'},
    {'nombre': 'Dragón de la Cólquida', 'derrotado_por': None},
    {'nombre': 'Cerbero', 'derrotado_por': None},
    {'nombre': 'Cerda de Cromión', 'derrotado_por': 'Teseo'},
    {'nombre': 'Ortro', 'derrotado_por': 'Heracles'},
    {'nombre': 'Toro de Creta', 'derrotado_por': 'Teseo'},
    {'nombre': 'Jabalí de Calidón', 'derrotado_por': 'Atalanta'},
    {'nombre': 'Carcinos', 'derrotado_por': None},
    {'nombre': 'Gerión', 'derrotado_por': 'Heracles'},
    {'nombre': 'Cloto', 'derrotado_por': None},
    {'nombre': 'Láquesis', 'derrotado_por': None},
    {'nombre': 'Átropos', 'derrotado_por': None},
    {'nombre': 'Minotauro de Creta', 'derrotado_por': 'Teseo'},
    {'nombre': 'Harpías', 'derrotado_por': None},
    {'nombre': 'Argos Panoptes', 'derrotado_por': 'Hermes'},
    {'nombre': 'Aves del Estínfalo', 'derrotado_por': None},
    {'nombre': 'Talos', 'derrotado_por': 'Medea'},
    {'nombre': 'Sirenas', 'derrotado_por': None},
    {'nombre': 'Pitón', 'derrotado_por': 'Apolo'},
    {'nombre': 'Cierva de Cerinea', 'derrotado_por': None},
    {'nombre': 'Basilisco', 'derrotado_por': None},
    {'nombre': 'Jabalí de Erimanto', 'derrotado_por': None}
]


# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
arbol_criaturas = BinaryTree()

for criatura in criaturas:
    arbol_criaturas.insert_node(criatura['nombre'], {
        'derrotado_por': criatura['derrotado_por'],
        'descripcion': '',
        'capturada': None
    })

# a. listado inorden de las criaturas y quienes la derrotaron;
print()
print('-----A-----')
print()

def listar_inorden(root):
    if root is not None:
        listar_inorden(root.left)
        if root.other_values['derrotado_por'] is None:
            print(f'{root.value} - no fue derrotada')
        else:
            print(f'{root.value} - derrotada por {root.other_values["derrotado_por"]}')
        listar_inorden(root.right)

listar_inorden(arbol_criaturas.root)

# b. se debe permitir cargar una breve descripción sobre cada criatura;
print()
print('-----B-----')
print()

descripciones = {
    'Talos': 'Gigante de bronce que protegía la isla de Creta.',
    'Cerbero': 'Perro de tres cabezas que guarda la entrada al Hades.',
    'Hidra de Lerna': 'Serpiente acuática de varias cabezas que se regeneraban.',
    'Minotauro de Creta': 'Mitad hombre y mitad toro, encerrado en el laberinto de Creta.'
}

for nombre in descripciones:
    nodo = arbol_criaturas.search(nombre)
    if nodo is not None:
        nodo.other_values['descripcion'] = descripciones[nombre]
        print(f'Descripción cargada a {nombre}')

# c. mostrar toda la información de la criatura Talos;
print()
print('-----C-----')
print()

nodo = arbol_criaturas.search('Talos')
if nodo is not None:
    print(f'Criatura: {nodo.value}')
    print(f'Derrotada por: {nodo.other_values["derrotado_por"]}')
    print(f'Descripción: {nodo.other_values["descripcion"]}')
    print(f'Capturada por: {nodo.other_values["capturada"]}')

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print()
print('-----D-----')
print()

def contar_derrotas(root, contador):
    if root is not None:
        contar_derrotas(root.left, contador)
        heroe = root.other_values['derrotado_por']
        if heroe is not None:
            if heroe in contador:
                contador[heroe] += 1
            else:
                contador[heroe] = 1
        contar_derrotas(root.right, contador)

contador = {}
contar_derrotas(arbol_criaturas.root, contador)

heap_heroes = HeapMax()
for heroe in contador:
    heap_heroes.arrive(heroe, contador[heroe])

for i in range(3):
    cantidad, heroe = heap_heroes.attention()
    print(f'{heroe} - criaturas derrotadas: {cantidad}')

# e. listar las criaturas derrotadas por Heracles;
print()
print('-----E-----')
print()

def listar_por_campo(root, campo, valor):
    if root is not None:
        listar_por_campo(root.left, campo, valor)
        if root.other_values[campo] == valor:
            print(root.value)
        listar_por_campo(root.right, campo, valor)

listar_por_campo(arbol_criaturas.root, 'derrotado_por', 'Heracles')

# f. listar las criaturas que no han sido derrotadas;
print()
print('-----F-----')
print()

listar_por_campo(arbol_criaturas.root, 'derrotado_por', None)

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
print()
print('-----H-----')
print()

for nombre in ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']:
    nodo = arbol_criaturas.search(nombre)
    if nodo is not None:
        nodo.other_values['capturada'] = 'Heracles'
        print(f'{nombre} - capturada por {nodo.other_values["capturada"]}')

# i. se debe permitir búsquedas por coincidencia;
print()
print('-----I-----')
print()

texto = input('Ingrese lo que quiere buscar: ')
arbol_criaturas.proxy_search(texto.lower())

# j. eliminar al Basilisco y a las Sirenas;
print()
print('-----J-----')
print()

print('Eliminado:', arbol_criaturas.delete_node('Basilisco'))
print('Eliminado:', arbol_criaturas.delete_node('Sirenas'))

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
print()
print('-----K-----')
print()

nodo = arbol_criaturas.search('Aves del Estínfalo')
if nodo is not None:
    nodo.other_values['derrotado_por'] = 'Heracles'
    print(f'{nodo.value} - derrotada por {nodo.other_values["derrotado_por"]}')

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print()
print('-----L-----')
print()

valor, otros_valores = arbol_criaturas.delete_node('Ladón')
if valor is not None:
    arbol_criaturas.insert_node('Dragón Ladón', otros_valores)
    print(f'{valor} ahora es Dragón Ladón')

# m. realizar un listado por nivel del árbol;
print()
print('-----M-----')
print()

arbol_criaturas.by_level()

# n. muestre las criaturas capturadas por Heracles.
print()
print('-----N-----')
print()

listar_por_campo(arbol_criaturas.root, 'capturada', 'Heracles')