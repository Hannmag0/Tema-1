"Serie de Fibonacci utilizando ciclos"

# Cantidad de términos
n = 10

# Primeros dos términos
a = 0
b = 1

print("Serie de Fibonacci:")

# Ciclo para generar los términos
for i in range(n):
    print(a, end=" ")

    # Calcular el siguiente término
    siguiente = a + b

    # Actualizar valores
    a = b
    b = siguiente