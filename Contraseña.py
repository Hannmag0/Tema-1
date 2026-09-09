import re

contraseña = input("Ingresa tu contraseña: ")

patron = r"^(?=.{8,}$)(?=.*[A-Z])(?=.*#)(?=.*[^A-Za-z0-9]).*$"

if re.fullmatch(patron, contraseña):
    print("Contraseña segura")
else:
    print("Contraseña no válida")