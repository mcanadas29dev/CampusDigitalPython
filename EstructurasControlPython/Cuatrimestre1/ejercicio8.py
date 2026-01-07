"""8. Control de Intentos de Acceso: 
Utiliza un bucle while para pedir una contraseña al usuario. 
El programa debe permitir un máximo de 3 intentos; si el usuario acierta, 
usa break para salir del bucle y mostrar "Acceso concedido"
"""

PASSWORD = "Qmducqo2026"

intentos = 0

while intentos < 3:
    clave = input("Introduzca la contraseña: ")
    if clave == PASSWORD:
        print("Acceso concedido")
        break
   
    intentos += 1
else:
    print("Acceso denegado, Máximo numero de intentos alcanzado")