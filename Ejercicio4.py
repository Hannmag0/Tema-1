"MCD a partir de dos números usando factores a partir de dos números"

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
    while a % divisor == 0:
        factores_a.append(divisor)
        a = a // divisor
    divisor += 1

# Obtener factores del segundo número
divisor = 2

while b > 1:
    while b % divisor == 0:
        factores_b.append(divisor)
        b = b // divisor
    divisor += 1

# Buscar factores comunes
factores_comunes = []

for factor in factores_a:
    if factor in factores_b:
        factores_comunes.append(factor)
        factores_b.remove(factor)

# Calcular el MCD multiplicando los factores comunes
mcd = 1

for factor in factores_comunes:
    mcd *= factor

# Mostrar resultados
print("Factores del primer número:", factores_a)
print("Factores del segundo número:", factores_b)
print("Factores comunes:", factores_comunes)
print("El MCD es:", mcd)