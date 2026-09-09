# Ejercicio 1: Sumar los elementos de una lista con recursividad

numeros = [10, 20, 30, 40, 50]

def sumar_lista(lista):
    # Caso base: si la lista está vacía
    if len(lista) == 0:
        return 0
    
    # Caso recursivo
    return lista[0] + sumar_lista(lista[1:])

suma = sumar_lista(numeros)

print("La suma de los elementos es:", suma)