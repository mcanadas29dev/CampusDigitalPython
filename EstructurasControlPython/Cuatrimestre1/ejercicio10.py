"""
10. Calculadora de Media Dinámica: 
Escribe un programa que pida números al usuario de forma continua usando un bucle while 
hasta que el usuario escriba la palabra "fin". Al terminar, el programa debe llamar a una función 
que calcule y devuelva la media aritmética de todos los números introducidos.
"""

def media_aritmetica(lista):
    suma_media = 0
    for num in lista:
        suma_media +=num
    return (suma_media / len(lista))
        


lista_numeros =[]  
opcion = None
while opcion != "fin":
    opcion = input("Introduzca un numero o 'fin' para terminar: ")
    if opcion.isdigit():
        lista_numeros.append(int(opcion))
   
print(f"La Media aritmetica de {lista_numeros} es {media_aritmetica(lista_numeros)} ")