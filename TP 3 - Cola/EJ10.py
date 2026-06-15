#Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora 
# de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue
from stack import Stack


notificaciones = Queue()

notificaciones.arrive({
    'hora': '12:30',
    'app': 'Twitter',
    'mensaje': 'Tu posteo "Aprendiendo Python" tiene 10 likes.'
})

notificaciones.arrive({
    'hora': '13:10',
    'app': 'Facebook',
    'mensaje': 'Tienes un nuevo comentario.'
})

notificaciones.arrive({
    'hora': '14:25',
    'app': 'Twitter',
    'mensaje': 'Tienes un nuevo mensaje.'
})

notificaciones.arrive({
    'hora': '18:00',
    'app': 'Instagram',
    'mensaje': 'Tienes una solicitud de amistad.'
})

notificaciones.arrive({
    'hora': '15:00',
    'app': 'Facebook',
    'mensaje': 'Python Fans Club llegó a 100 seguidores.'
})


# a) Escribir una función que elimine de la cola todas las notificaciones de Facebook

def eliminar_facebook(cola):
    cola_aux = Queue()

    while cola.size() > 0:
        notificacion = cola.attention()

        if notificacion['app'] != 'Facebook':
            cola_aux.arrive(notificacion)

    return cola_aux


# b) Escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;

def twitter_python(cola):
    cantidad = cola.size()

    for i in range(cantidad):
        notificacion = cola.attention()

        if (notificacion['app'] == 'Twitter'
                and 'Python' in notificacion['mensaje']):
            print(notificacion)

        cola.arrive(notificacion)


# c) Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.


def dentro_rango(hora):
    return '11:43' <= hora <= '15:57'


def notificaciones_rango(cola):
    pila = Stack()

    cantidad = cola.size()

    for i in range(cantidad):
        notificacion = cola.attention()

        if dentro_rango(notificacion['hora']):
            pila.push(notificacion)

        cola.arrive(notificacion)

    return pila


print('Notificaciones de Twitter que contienen "Python":')
twitter_python(notificaciones)

print()

notificaciones = eliminar_facebook(notificaciones)

print("Cola sin notificaciones de Facebook:")
notificaciones.show()

print()

pila_rango = notificaciones_rango(notificaciones)

print("Cantidad de notificaciones entre 11:43 y 15:57:")
print(pila_rango.size())

print()

print("Notificaciones guardadas en la pila:")
while pila_rango.size() > 0:
    print(pila_rango.pop())