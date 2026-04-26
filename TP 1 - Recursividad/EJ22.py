#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) 
#está atrapado, pero muy cerca está su mochila que contiene muchos objetos.

#Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#c. Utilizar un vector para representar la mochila.

mochila = ['pistola', 'botella', 'telefono', 'vendas', 'sable de luz']

def usar_la_fuerza(mochila, index=0, contador=0):
    if index >= len(mochila):
        return f'No se encontró el sable de luz. Se sacaron: {contador} objetos.'
    elif mochila[index] == "sable de luz":
        return f'Se encontró el sable de luz. Se sacaron: {contador+1} objetos.'
    else:
        return usar_la_fuerza(mochila, index+1, contador+1)

print(usar_la_fuerza(mochila))