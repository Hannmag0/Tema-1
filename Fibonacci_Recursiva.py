"Serie de Fibonacci con función recursiva"

# Función recursiva
def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Llamada recursiva
    return fibonacci(n - 1) + fibonacci(n - 2)


# Cantidad de términos
n = 10

print("Serie de Fibonacci:")

for i in range(n):
    print(fibonacci(i), end=" ")