"Calcular el MCD de dos números usando el algoritmo de Euclides con recursividad"

# Función recursiva
def mcd(a, b):
    # Caso base
    if b == 0:
        return a

    # Llamada recursiva
    return mcd(b, a % b)


# Pedir los dos números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

# Calcular el MCD
resultado = mcd(a, b)

# Mostrar el resultado
print("El MCD es:", resultado)