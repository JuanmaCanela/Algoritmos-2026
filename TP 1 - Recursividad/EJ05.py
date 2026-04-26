#Desarrollar una función que permita convertir un número romano en un número decimal.

romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romano_a_decimal(nro_romano):
    if len(nro_romano) == 0:
        return 0
    elif len(nro_romano) == 1:
        return romanos[nro_romano[0]]
    elif romanos[nro_romano[0]] < romanos[nro_romano[1]]:
        return romanos[nro_romano[1]] - romanos[nro_romano[0]] + romano_a_decimal(nro_romano[2:])
    else:
        return romanos[nro_romano[0]] + romano_a_decimal(nro_romano[1:])
    
print(romano_a_decimal('VII'))