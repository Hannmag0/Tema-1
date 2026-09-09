# Ejercicio 2: Cálculo de una potencia usando ciclos

# Datos
base = 2
exponente = 5

# Acumulador
resultado = 1

# Calcular la potencia usando un ciclo
for i in range(exponente):
    resultado = resultado * base

# Mostrar resultado
print("La potencia es:", resultado)