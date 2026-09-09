import re

correo = input("Ingresa tu correo electrónico: ")

patron = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"

if re.fullmatch(patron, correo):
    print("Correo válido")
else:
    print("Correo no válido")