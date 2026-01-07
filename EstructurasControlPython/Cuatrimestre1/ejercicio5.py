"""
5. Validador de Contraseñas con Bucle: 
Diseña una función validar_contraseña(password) que verifique si una clave es segura. 
La función debe usar un bucle for para recorrer cada carácter y confirmar que contiene al menos un número 
(comprobando si el carácter está en la cadena "0123456789")
"""
CADENA = "0123456789"
def validar_contraseña(password):
    
    total_comprobación = 0
    for caracter in password:
        if caracter in CADENA:
            total_comprobación +=1
    return total_comprobación

password = input("Introduzca la contraseña con al menos 1 número (0-9): ")
total_numeros = validar_contraseña(password)
if total_numeros > 0:
    print(f"Contraseña valida, tiene {total_numeros} numeros")
else:
    print(f"Contraseña no es segura tiene {total_numeros} numeros ")