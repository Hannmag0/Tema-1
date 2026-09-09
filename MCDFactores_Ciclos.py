"MCD usando factores y ciclos"

# Pedir los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Guardar los valores para obtener sus factores
a = num1
b = num2

factores_a = []
factores_b = []

# Obtener factores del primer número
divisor = 2

while a > 1:
    if a % divisor == 0:
        factores_a.append(divisor)
        a = a // divisor
    else:
        divisor += 1

# Obtener factores del segundo número
divisor = 2

while b > 1:
    if b % divisor == 0:
        factores_b.append(divisor)
        b = b // divisor
    else:
        divisor += 1

# Copia para buscar factores comunes
factores_b_aux = factores_b.copy()

# Buscar factores comunes
factores_comunes = []

for factor in factores_a:
    if factor in factores_b_aux:
        factores_comunes.append(factor)
        factores_b_aux.remove(factor)

# Calcular el MCD
mcd = 1

for factor in factores_comunes:
    mcd *= factor

# Mostrar resultados
print("Factores del primer número:", factores_a)
print("Factores del segundo número:", factores_b)
print("Factores comunes:", factores_comunes)
print("El MCD es:", mcd)