"""
4. Generador de Tablas de Multiplicar: 
Crea una función que reciba un número como parámetro y, mediante un bucle for, imprima su tabla de multiplicar del 1 al 10 
con el formato "n x i = resultado"
"""

def tabla_multiplicar(numero):
    for x in range(1,11):
        print(f"{numero} X {x} = {int(numero) * x} ")
        
numero = (input("Introduzca un numero mayor que 0: "))
while not numero.isdecimal() or int(numero) < 0 or int(numero) == 0:
    numero = (input("Introduzca un numero mayor que 0: "))
tabla_multiplicar(numero)