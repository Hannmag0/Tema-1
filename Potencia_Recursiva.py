# Ejercicio 2: Cálculo de una potencia con función recursiva

# Datos
base = 2
exponente = 5

# Función recursiva
def calcular_potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    
    # Caso recursivo
    return base * calcular_potencia(base, exponente - 1)

# Calcular la potencia
resultado = calcular_potencia(base, exponente)

# Mostrar resultado
print("La potencia es:", resultado)