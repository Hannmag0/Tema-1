import re

telefono = input("Ingresa tu número de teléfono: ")

patron = r"^\d{2}\d{10}$"

if re.fullmatch(patron, telefono):
    print("Número de teléfono válido")
else:
    print("Número de teléfono no válido")