"""
3. Contador de Números Pares: 
Implementa una función es_par(numero) que devuelva True si un número es par y False si es impar 
usando el operador módulo %. Luego, usa un bucle para recorrer los números del 1 al 20 y, 
apoyándote en la función, cuenta cuántos de ellos son pares
"""
def es_par(numero):
    return numero % 2 == 0

total_pares = 0
for num in range (1, 21):
    if es_par(num):
        total_pares +=1
print (f"El ltotal de pares del 1 al 20 es :{total_pares} " )