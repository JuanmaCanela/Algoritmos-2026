# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# - cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# - hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# - determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# - cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# - calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# - indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph

grafo = Graph(is_dir=False)

# personajes y episodios en los que aparecieron
grafo.add_vertex('Luke Skywalker', [3, 4, 5, 6, 7, 8, 9])
grafo.add_vertex('Darth Vader', [3, 4, 5, 6])
grafo.add_vertex('Yoda', [1, 2, 3, 5, 6, 8])
grafo.add_vertex('Boba Fett', [2, 5, 6])
grafo.add_vertex('C-3PO', [1, 2, 3, 4, 5, 6, 7, 8, 9])
grafo.add_vertex('Leia', [3, 4, 5, 6, 7, 8, 9])
grafo.add_vertex('Rey', [7, 8, 9])
grafo.add_vertex('Kylo Ren', [7, 8, 9])
grafo.add_vertex('Chewbacca', [3, 4, 5, 6, 7, 8, 9])
grafo.add_vertex('Han Solo', [4, 5, 6, 7, 9])
grafo.add_vertex('R2-D2', [1, 2, 3, 4, 5, 6, 7, 8, 9])
grafo.add_vertex('BB-8', [7, 8, 9])

# conexiones y cantidad de episodios compartidos
grafo.add_edge(4, 'Luke Skywalker', 'Leia')
grafo.add_edge(3, 'Luke Skywalker', 'Darth Vader')
grafo.add_edge(2, 'Luke Skywalker', 'Yoda')
grafo.add_edge(4, 'Leia', 'Han Solo')
grafo.add_edge(5, 'Leia', 'C-3PO')
grafo.add_edge(6, 'C-3PO', 'R2-D2')
grafo.add_edge(1, 'Yoda', 'Darth Vader')
grafo.add_edge(4, 'Han Solo', 'Chewbacca')
grafo.add_edge(3, 'Rey', 'Kylo Ren')
grafo.add_edge(2, 'Rey', 'BB-8')
grafo.add_edge(2, 'Boba Fett', 'Darth Vader')
grafo.add_edge(1, 'Leia', 'Rey')
grafo.add_edge(3, 'Chewbacca', 'R2-D2')
grafo.add_edge(1, 'BB-8', 'C-3PO')

# - hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print("-----")

print()
print("Arbol de expansion minimo desde C-3PO:")
print(grafo.kruskal('C-3PO'))

print()
print("Arbol de expansion minimo desde Yoda:")
print(grafo.kruskal('Yoda'))

print()
print("Arbol de expansion minimo desde Leia:")
print(grafo.kruskal('Leia'))

# - determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
print("-----")

mayor = 0
pares = []

for vertice in grafo:
    for arista in vertice.edges:
        if vertice.value < arista.destination:
            if arista.weight > mayor:
                mayor = arista.weight
                pares = [[vertice.value, arista.destination]]
            elif arista.weight == mayor:
                pares.append([vertice.value, arista.destination])

print()
print("Mayor cantidad de episodios compartidos:", mayor)
print()
print("Pares de personajes:")

for par in pares:
    print(par[0], "-", par[1])

# - calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
print("-----")

# Camino mas corto desde C-3PO hasta R2-D2
paths = grafo.dijkstra('C-3PO')
destino = 'R2-D2'
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
print("Camino mas corto desde C-3PO hasta R2-D2:")
print(" - ".join(camino), "Costo:", peso_total)


# Camino mas corto desde Yoda hasta Darth Vader
paths = grafo.dijkstra('Yoda')
destino = 'Darth Vader'
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
print("Camino mas corto desde Yoda hasta Darth Vader:")
print(" - ".join(camino), "Costo:", peso_total)

# - indicar qué personajes aparecieron en los nueve episodios de la saga.
print("-----")

print()
print("Personajes que aparecieron en los nueve episodios:")

for vertice in grafo:
    if len(vertice.other_values) == 9:
        print(vertice.value)