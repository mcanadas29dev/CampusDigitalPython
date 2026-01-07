"""
2. Suma Acumulada del 1 al 100: Escribe un programa que utilice un acumulador dentro de un bucle for 
para calcular la suma de todos los números del 1 al 100. Para hacerlo más profesional, encapsula esta 
lógica en una función que devuelva el resultado final.

"""

def sumar():
    acumulado = 0
    for x in range(1,101):
        acumulado += x
    return acumulado

print(f"Resultado de la suma de 1 a 100 es:{sumar()} ")