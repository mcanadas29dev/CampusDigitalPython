"""
7. Detector de Vocales en una Frase: 
Implementa la función contar_vocales(texto). Debe recorrer el texto con un bucle for y usar el operador in para verificar 
si cada letra es una vocal (a, e, i, o, u), devolviendo el total de vocales encontradas
"""

def contar_vocales(texto):
    VOCALES = "aeiou"
    total_vocales = 0
    for caracter in texto:
        if caracter.lower() in VOCALES:
            total_vocales +=1
    return total_vocales

texto = input("Introduce un texto para comprobar el numero de vocales: ")
print(f"El numero de vocales del texto \"{texto}\"  es: {contar_vocales(texto)}")