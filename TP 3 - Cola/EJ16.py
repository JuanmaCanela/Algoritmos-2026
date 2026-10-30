# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio (1 - empleados, 2 - staff de tecnologías de la información “TI”, 3 - gerente), y resuelva la siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

from heap import HeapMin

cola_impresion = HeapMin()

# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
cola_impresion.arrive('Documento empleado 1', 1)
cola_impresion.arrive('Documento empleado 2', 1)
cola_impresion.arrive('Documento empleado 3', 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print()
print('-----B-----')
print()

prioridad, documento = cola_impresion.attention()
print(documento)

# c. cargue dos documentos del staff de TI.
cola_impresion.arrive('Documento TI 1', 2)
cola_impresion.arrive('Documento TI 2', 2)

# d. cargue un documento del gerente.
cola_impresion.arrive('Documento gerente 1', 3)

# e. imprima los dos primeros documentos de la cola.
print()
print('-----E-----')
print()

for i in range(2):
    prioridad, documento = cola_impresion.attention()
    print(documento)

# f. cargue dos documentos de empleados y uno de gerente.
cola_impresion.arrive('Documento empleado 4', 1)
cola_impresion.arrive('Documento empleado 5', 1)
cola_impresion.arrive('Documento gerente 2', 3)

# g. imprima todos los documentos de la cola de impresión.
print()
print('-----G-----')
print()

while cola_impresion.size() > 0:
    prioridad, documento = cola_impresion.attention()
    print(documento)