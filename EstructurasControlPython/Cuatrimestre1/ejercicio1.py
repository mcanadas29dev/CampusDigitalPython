"""
1. Saludo Múltiple con Funciones: Crea una función llamada saludar_persona(nombre) que reciba un nombre 
y muestre el mensaje "¡Hola, [nombre]!". 
Después, utiliza un bucle for para llamar a esta función y saludar a una lista de tres nombres diferentes
Docstring for EstructurasControlPython.Cuatrimestre1.ejercicio1
"""
def saludar_persona(nombre):
    """Función que saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}!")  

name = input("Ingresa tu nombre: ")
saludar_persona(name)

# Llama a la función para cada nombre en la lista
nombres = ["Ana", "Luis", "María"]  
for nombre in nombres:
    saludar_persona(nombre) 

