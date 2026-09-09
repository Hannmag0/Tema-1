import re

nombre = input("Ingresa tu nombre: ")

patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"

if re.fullmatch(patron, nombre):
    print("Nombre válido")
else:
    print("Nombre no válido")