import re

matricula = input("Ingresa tu matrícula: ")

patron = r"^\d{9}$"

if re.fullmatch(patron, matricula):
    print("Matrícula válida")
else:
    print("Matrícula no válida")