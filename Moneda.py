import re

moneda = input("Ingresa una cantidad: ")

patron = r"^\d+\.\d{2}$"

if re.fullmatch(patron, moneda):
    print("Cantidad válida")
else:
    print("Cantidad no válida")