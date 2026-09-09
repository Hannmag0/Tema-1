"Calcular el MCD de dos números usando el algoritmo de Euclides con ciclos"

# Pedir los dos números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

# Algoritmo de Euclides usando ciclo while
while b != 0:
    residuo = a % b
    a = b
    b = residuo

# Mostrar el resultado
print("El MCD es:", a)