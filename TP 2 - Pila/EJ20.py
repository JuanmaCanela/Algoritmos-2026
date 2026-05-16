# Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son cantidad de pasos y dirección
# –suponga que el robot solo puede moverse en ocho direcciones: norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. 
# Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de partida, 
# retornando por el mismo camino que fue.

from stack import Stack

movimientos = Stack()

movimientos.push({'direccion': 'norte', 'pasos': 10})
movimientos.push({'direccion': 'este', 'pasos': 5})
movimientos.push({'direccion': 'noreste', 'pasos': 3})
movimientos.push({'direccion': 'sur', 'pasos': 2})


def direccion_contraria(direccion):
    opuestos = {
        'norte': 'sur',
        'sur': 'norte',
        'este': 'oeste',
        'oeste': 'este',
        'noreste': 'suroeste',
        'noroeste': 'sureste',
        'sureste': 'noroeste',
        'suroeste': 'noreste'
    }
    
    return opuestos[direccion]

# Recorrido que hizo el robot (en el orden que sucedió)
def mostrar_recorrido(pila):
    pila_aux = Stack()
    
    while pila.size() > 0:
        pila_aux.push(pila.pop())
    
    while pila_aux.size() > 0:
        movimiento = pila_aux.pop()
        print(movimiento)
        pila.push(movimiento)


print("Camino realizado:")
mostrar_recorrido(movimientos)

print()
print("Camino de regreso:")

while movimientos.size() > 0:
    movimiento = movimientos.pop()
    
    movimiento_vuelta = {
        'direccion': direccion_contraria(movimiento['direccion']),
        'pasos': movimiento['pasos']
    }
    
    print(movimiento_vuelta)