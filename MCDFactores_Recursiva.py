"MCD usando factores y función recursiva"

# Función recursiva para obtener los factores de un número
def obtener_factores(numero, divisor=2, factores=None):
    if factores is None:
        factores = []

    # Caso base
    if numero == 1:
        return factores

    # Si el divisor divide al número
    if numero % divisor == 0:
        factores.append(divisor)
        return obtener_factores(numero // divisor, divisor, factores)

    # Probar con el siguiente divisor
    return obtener_factores(numero, divisor + 1, factores)


# Pedir los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Obtener factores de ambos números
factores_a = obtener_factores(num1)
factores_b = obtener_factores(num2)

# Copia para poder eliminar factores sin afectar la lista original
factores_b_aux = factores_b.copy()

# Buscar factores comunes
factores_comunes = []

for factor in factores_a:
    if factor in factores_b_aux:
        factores_comunes.append(factor)
        factores_b_aux.remove(factor)

# Calcular el MCD multiplicando los factores comunes
mcd = 1

for factor in factores_comunes:
    mcd *= factor

# Mostrar resultados
print("Factores del primer número:", factores_a)
print("Factores del segundo número:", factores_b)
print("Factores comunes:", factores_comunes)
print("El MCD es:", mcd)