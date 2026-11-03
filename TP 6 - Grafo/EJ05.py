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

print("Barrido en profundidad desde Red Hat:")
grafo.deep_show('Red Hat')

print()
print("Barrido en amplitud desde Red Hat:")
grafo.amplitude_show('Red Hat')

print()
print("Barrido en profundidad desde Debian:")
grafo.deep_show('Debian')

print()
print("Barrido en amplitud desde Debian:")
grafo.amplitude_show('Debian')

print()
print("Barrido en profundidad desde Arch:")
grafo.deep_show('Arch')

print()
print("Barrido en amplitud desde Arch:")
grafo.amplitude_show('Arch')

# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;
print()
print('-----C-----')
print()

def camino_impresora(origen):
    paths = grafo.dijkstra(origen)
    destino = 'Impresora'
    peso_total = None
    camino = []

    while paths.size() > 0:
        valor = paths.pop()

        if valor[0] == destino:
            if peso_total is None:
                peso_total = valor[1]

            camino.append(valor[0])
            destino = valor[2]

    camino.reverse()

    print()
    print("Camino desde", origen, "hasta la impresora:")
    print(" - ".join(camino), "Costo:", peso_total)

camino_impresora('Manjaro')
camino_impresora('Red Hat')
camino_impresora('Fedora')

# d. encontrar el árbol de expansión mínima;
print()
print('-----D-----')
print()

print("Arbol de expansion minima:")
print(grafo.kruskal('Manjaro'))

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
print()
print('-----E-----')
print()

def camino_hasta(origen, destino):
    paths = grafo.dijkstra(origen)
    peso_total = None
    camino = []

    while paths.size() > 0:
        valor = paths.pop()

        if valor[0] == destino:
            if peso_total is None:
                peso_total = valor[1]

            camino.append(valor[0])
            destino = valor[2]

    camino.reverse()

    return peso_total, camino

pcs = ['Manjaro', 'Parrot', 'Fedora', 'Ubuntu', 'Mint']

menor_costo = None
mejor_pc = None
mejor_camino = []

for pc in pcs:
    costo, camino = camino_hasta(pc, 'Guaraní')

    print()
    print("Desde", pc, "hasta Guaraní:")
    print(" - ".join(camino), "Costo:", costo)

    if menor_costo is None or costo < menor_costo:
        menor_costo = costo
        mejor_pc = pc
        mejor_camino = camino

print()
print("La PC con el camino mas corto es:", mejor_pc)
print("Camino:", " - ".join(mejor_camino))
print("Costo total:", menor_costo)

# f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
print()
print('-----F-----')
print()

computadoras = ['Debian', 'Ubuntu', 'Mint']

menor_costo = None
mejor_computadora = None
mejor_camino = []

for computadora in computadoras:
    costo, camino = camino_hasta(computadora, 'MongoDB')

    print()
    print("Desde", computadora, "hasta MongoDB:")
    print(" - ".join(camino), "Costo:", costo)

    if menor_costo is None or costo < menor_costo:
        menor_costo = costo
        mejor_computadora = computadora
        mejor_camino = camino

print()
print("La computadora con el camino mas corto es:", mejor_computadora)
print("Camino:", " - ".join(mejor_camino))
print("Costo total:", menor_costo)

# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
print()
print('-----G-----')
print()

grafo.delete_edge('Switch 1', 'Impresora')
grafo.add_edge(22, 'Router 2', 'Impresora')

print()
print("Barrido en profundidad desde Red Hat:")
grafo.deep_show('Red Hat')

print()
print("Barrido en amplitud desde Red Hat:")
grafo.amplitude_show('Red Hat')

print()
print("Barrido en profundidad desde Debian:")
grafo.deep_show('Debian')

print()
print("Barrido en amplitud desde Debian:")
grafo.amplitude_show('Debian')

print()
print("Barrido en profundidad desde Arch:")
grafo.deep_show('Arch')

print()
print("Barrido en amplitud desde Arch:")
grafo.amplitude_show('Arch')