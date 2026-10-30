# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación: 
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

from graph import Graph

# h. debe utilizar un grafo no dirigido.
grafo = Graph(is_dir=False)

# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
grafo.add_vertex('Manjaro', 'pc')
grafo.add_vertex('Parrot', 'pc')
grafo.add_vertex('Fedora', 'pc')
grafo.add_vertex('Ubuntu', 'pc')
grafo.add_vertex('Mint', 'pc')
grafo.add_vertex('Red Hat', 'notebook')
grafo.add_vertex('Debian', 'notebook')
grafo.add_vertex('Arch', 'notebook')
grafo.add_vertex('Guaraní', 'servidor')
grafo.add_vertex('MongoDB', 'servidor')
grafo.add_vertex('Router 1', 'router')
grafo.add_vertex('Router 2', 'router')
grafo.add_vertex('Router 3', 'router')
grafo.add_vertex('Switch 1', 'switch')
grafo.add_vertex('Switch 2', 'switch')
grafo.add_vertex('Impresora', 'impresora')

# aristas (peso, origen, destino)
grafo.add_edge(40, 'Manjaro', 'Switch 2')
grafo.add_edge(12, 'Parrot', 'Switch 2')
grafo.add_edge(3, 'Fedora', 'Switch 2')
grafo.add_edge(5, 'MongoDB', 'Switch 2')
grafo.add_edge(56, 'Arch', 'Switch 2')
grafo.add_edge(61, 'Switch 2', 'Router 3')
grafo.add_edge(50, 'Router 3', 'Router 2')
grafo.add_edge(43, 'Router 3', 'Router 1')
grafo.add_edge(37, 'Router 2', 'Router 1')
grafo.add_edge(9, 'Router 2', 'Guaraní')
grafo.add_edge(25, 'Router 2', 'Red Hat')
grafo.add_edge(29, 'Router 1', 'Switch 1')
grafo.add_edge(17, 'Switch 1', 'Debian')
grafo.add_edge(18, 'Switch 1', 'Ubuntu')
grafo.add_edge(22, 'Switch 1', 'Impresora')
grafo.add_edge(80, 'Switch 1', 'Mint')


# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
print()
print('-----B-----')
print()

def barridos_notebooks(grafo):
    for notebook in ['Red Hat', 'Debian', 'Arch']:
        print(f'Barrido en profundidad desde {notebook}:')
        grafo.deep_show(notebook)
        print()
        print(f'Barrido en amplitud desde {notebook}:')
        grafo.amplitude_show(notebook)
        print()

barridos_notebooks(grafo)

# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
print()
print('-----C-----')
print()

def camino_mas_corto(grafo, origen, destino):
    paths = grafo.dijkstra(origen)
    camino = []
    costo = None

    while paths.size() > 0:
        valor = paths.pop()
        if valor[0] == destino:
            if costo is None:
                costo = valor[1]
            camino.append(valor[0])
            destino = valor[2]

    camino.reverse()
    return camino, costo

for origen in ['Manjaro', 'Red Hat', 'Fedora']:
    camino, costo = camino_mas_corto(grafo, origen, 'Impresora')
    print(f'Desde {origen}: {" - ".join(camino)} con un costo de {costo}')

# d. encontrar el árbol de expansión mínima;
print()
print('-----D-----')
print()

arbol_minimo = grafo.kruskal('Router 1')

peso_total = 0
for arista in arbol_minimo.split(';'):
    origen, destino, peso = arista.split('-')
    print(f'{origen} - {destino} (peso {peso})')
    peso_total += int(peso)
print(f'Peso total del árbol de expansión mínima: {peso_total}')

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
print()
print('-----E-----')
print()

menor_costo = None
mejor_pc = None
mejor_camino = None

for vertice in grafo:
    if vertice.other_values == 'pc':
        camino, costo = camino_mas_corto(grafo, vertice.value, 'Guaraní')
        if menor_costo is None or costo < menor_costo:
            menor_costo = costo
            mejor_pc = vertice.value
            mejor_camino = camino

print(f'La pc con el camino más corto a Guaraní es {mejor_pc}: {" - ".join(mejor_camino)} con un costo de {menor_costo}')

# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
print()
print('-----F-----')
print()

menor_costo = None
mejor_equipo = None
mejor_camino = None

pos_switch = grafo.search('Switch 1', 'value')
for arista in grafo[pos_switch].edges:
    pos = grafo.search(arista.destination, 'value')
    if grafo[pos].other_values == 'pc' or grafo[pos].other_values == 'notebook':
        camino, costo = camino_mas_corto(grafo, arista.destination, 'MongoDB')
        if menor_costo is None or costo < menor_costo:
            menor_costo = costo
            mejor_equipo = arista.destination
            mejor_camino = camino

print(f'La computadora del Switch 1 con el camino más corto a MongoDB es {mejor_equipo}: {" - ".join(mejor_camino)} con un costo de {menor_costo}')

# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
print()
print('-----G-----')
print()

grafo.delete_edge('Switch 1', 'Impresora')
grafo.add_edge(22, 'Router 2', 'Impresora')

barridos_notebooks(grafo)