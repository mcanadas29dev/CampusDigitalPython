"""
9. Analizador de Palíndromos: 
Crea una función que determine si una palabra o frase es un palíndromo 
(se lee igual de izquierda a derecha que de derecha a izquierda). 
Para ello, usa métodos como .replace(" ", "") para quitar espacios y .lower() 
para normalizar el texto antes de compararlo con su versión invertida usando texto[::-1]
"""

def palindromo(frase):
    palabra_palindroma = frase.replace(" ", "").lower()
    return(palabra_palindroma == palabra_palindroma[::-1], frase)
resultado = palindromo("Anita lava la tina")    
print(f"Es {resultado[0]} que \"{resultado[1]}\" es palíndroma " )