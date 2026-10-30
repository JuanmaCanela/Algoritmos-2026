# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas: 
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

from graph import Graph

grafo = Graph(is_dir=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
grafo.add_vertex('cocina')
grafo.add_vertex('comedor')
grafo.add_vertex('cochera')
grafo.add_vertex('quincho')
grafo.add_vertex('baño 1')
grafo.add_vertex('baño 2')
grafo.add_vertex('habitación 1')
grafo.add_vertex('habitación 2')
grafo.add_vertex('sala de estar')
grafo.add_vertex('terraza')
grafo.add_vertex('patio')

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
grafo.add_edge(4, 'sala de estar', 'comedor')
grafo.add_edge(9, 'sala de estar', 'habitación 1')
grafo.add_edge(7, 'sala de estar', 'habitación 2')
grafo.add_edge(4, 'sala de estar', 'baño 1')
grafo.add_edge(8, 'sala de estar', 'terraza')
grafo.add_edge(5, 'patio', 'cocina')
grafo.add_edge(6, 'patio', 'quincho')
grafo.add_edge(9, 'patio', 'cochera')
grafo.add_edge(4, 'patio', 'terraza')
grafo.add_edge(7, 'patio', 'comedor')
grafo.add_edge(3, 'comedor', 'cocina')
grafo.add_edge(5, 'habitación 1', 'habitación 2')
grafo.add_edge(3, 'habitación 1', 'baño 1')
grafo.add_edge(4, 'habitación 2', 'baño 2')
grafo.add_edge(6, 'baño 1', 'baño 2')
grafo.add_edge(5, 'quincho', 'cochera')
grafo.add_edge(8, 'quincho', 'cocina')
grafo.add_edge(7, 'cochera', 'cocina')
grafo.add_edge(10, 'baño 2', 'terraza')

print()
print('-----B-----')
print()

grafo.show()

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
print()
print('-----C-----')
print()

arbol_minimo = grafo.kruskal('cocina')

metros_cable = 0
for arista in arbol_minimo.split(';'):
    origen, destino, metros = arista.split('-')
    print(f'{origen} - {destino}: {metros} m')
    metros_cable += int(metros)
print(f'Metros de cable necesarios para conectar todos los ambientes: {metros_cable} m')

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
print()
print('-----D-----')
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

camino, metros = camino_mas_corto(grafo, 'habitación 1', 'sala de estar')
print(f'Camino más corto: {" - ".join(camino)}')
print(f'Metros de cable de red necesarios entre el router y el Smart Tv: {metros} m')