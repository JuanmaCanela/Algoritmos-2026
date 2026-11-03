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
arbol = BinaryTree()

for criatura in criaturas:
    datos = {
        'derrotado_por': criatura['derrotado_por'],
        'descripcion': '',
        'capturada': None
    }

    arbol.insert_node(criatura['nombre'], datos)

# a. listado inorden de las criaturas y quienes la derrotaron;
print()
print('-----A-----')
print()

print("Criaturas y quienes las derrotaron:")
arbol.inorden(datos=True) 

# modifiqué el inorden de tree para que evalúe si hay datos que mostrar, quedó así:

# def inorden(self, datos=False) -> None:
        
#        def __inorden(root):
#            if root.left is not None:
#                __inorden(root.left)
#                if datos:
#                    print(root.value, root.other_values)
#                else:
#                    print(root.value, root.height)
#            if root.right is not None:
#                __inorden(root.right)

#        __inorden(self.root)

# b. se debe permitir cargar una breve descripción sobre cada criatura;
print()
print('-----B-----')
print()

def cargar_descripcion(nombre, descripcion):
    criatura = arbol.search(nombre)

    if criatura is not None:
        criatura.other_values['descripcion'] = descripcion
    else:
        print("No se encontro la criatura")

cargar_descripcion('Talos', 'Gigante de bronce que protegía la isla de Creta.')

# c. mostrar toda la información de la criatura Talos;
print()
print('-----C-----')
print()

print("Informacion de Talos:")

talos = arbol.search('Talos')

if talos is not None:
    print(talos.value, talos.other_values)

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print()
print('-----D-----')
print()

derrotas = {}

def contar_derrotas(raiz):
    if raiz is not None:
        derrotado_por = raiz.other_values['derrotado_por']

        if derrotado_por is not None:
            if derrotado_por not in derrotas:
                derrotas[derrotado_por] = 1
            else:
                derrotas[derrotado_por] += 1

        contar_derrotas(raiz.left)
        contar_derrotas(raiz.right)

contar_derrotas(arbol.root)

heap = HeapMax()

for personaje, cantidad in derrotas.items():
    heap.arrive(personaje, cantidad)

print("Los 3 personajes que derrotaron mas criaturas:")
print()

for i in range(3):
    prioridad, personaje = heap.attention()
    print(f"{personaje} - {prioridad} criaturas derrotadas")

# e. listar las criaturas derrotadas por Heracles;
print()
print('-----E-----')
print()

def mostrar_derrotadas_por(raiz, personaje):
    if raiz is not None:
        mostrar_derrotadas_por(raiz.left, personaje)

        if raiz.other_values['derrotado_por'] == personaje:
            print(raiz.value)

        mostrar_derrotadas_por(raiz.right, personaje)

print("Criaturas derrotadas por Heracles:")
print()
mostrar_derrotadas_por(arbol.root, 'Heracles')

# f. listar las criaturas que no han sido derrotadas;
print()
print('-----F-----')
print()

def mostrar_no_derrotadas(raiz):
    if raiz is not None:
        mostrar_no_derrotadas(raiz.left)

        if raiz.other_values['derrotado_por'] is None:
            print(raiz.value)

        mostrar_no_derrotadas(raiz.right)

print("Criaturas que no han sido derrotadas:")
print()
mostrar_no_derrotadas(arbol.root)

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;

criaturas_atrapadas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']

for nombre in criaturas_atrapadas:
    criatura = arbol.search(nombre)

    if criatura is not None:
        criatura.other_values['capturada'] = 'Heracles'

# i. se debe permitir búsquedas por coincidencia;
print()
print('-----I-----')
print()

buscado = input('Ingrese lo que quiere buscar: ')
arbol.proxy_search(buscado.lower())

# j. eliminar al Basilisco y a las Sirenas;
print()
print('-----J-----')
print()

print('Eliminado:', arbol.delete_node('Basilisco'))
print('Eliminado:', arbol.delete_node('Sirenas'))

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
print()

aves = arbol.search('Aves del Estínfalo')

if aves is not None:
    aves.other_values['derrotado_por'] = 'Heracles'

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;

ladon = arbol.search('Ladón')

if ladon is not None:
    datos = ladon.other_values
    arbol.delete_node('Ladón')
    arbol.insert_node('Dragón Ladón', datos)

# m. realizar un listado por nivel del árbol;
print()
print('-----M-----')
print()

print("Listado de criaturas por nivel:")
arbol.by_level()

# n. muestre las criaturas capturadas por Heracles.
print()
print('-----N-----')
print()

def mostrar_capturadas(raiz):
    if raiz is not None:
        mostrar_capturadas(raiz.left)

        if raiz.other_values['capturada'] == 'Heracles':
            print(raiz.value)

        mostrar_capturadas(raiz.right)

print("Criaturas capturadas por Heracles:")
mostrar_capturadas(arbol.root)