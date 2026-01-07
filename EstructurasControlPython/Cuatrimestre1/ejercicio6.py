"""
6. Cálculo de Factorial: Crea una función para calcular el factorial de un número entero 
(por ejemplo, 5! = 54321). Debes usar un bucle (ya sea for o while) para realizar el producto acumulado 
y devolver el valor total
"""

def factorial(numero):
    total = 1
    while numero > 0:
        total *=numero
        numero -=1
        factorial(numero)
    return total

try:
    numero = input("Introduzca un numero para calcular el factorial ")
    while not numero.isdecimal() or int(numero) < 0 or int(numero) == 0:
        numero = input("Introduzca un numero para calcular el factorial ")
    print (f"El factorial de {numero} es {factorial(int(numero))} ")
except:
    print("Debe introdudir un numero")
finally:
    print (f"FIN DEL PROGRAMA ")
   

