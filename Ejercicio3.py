"Serie de Fibonacci"

# Cantidad de términos
n = 10

# Primeros dos términos
a = 0
b = 1

print("Serie de Fibonacci:")

for i in range(n):
    print(a, end=" ")
    
    # Calcular el siguiente término
    siguiente = a + b
    a = b
    b = siguiente