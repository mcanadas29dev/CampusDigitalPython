from pathlib import Path
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def carga_csv():

    try:
        data_file = Path(__file__).with_name("ventas.csv")
        data = pd.read_csv(data_file)
       # Incorporar columna de fecha como datetime
        data['fecha'] = pd.to_datetime(data['fecha'])     
       # Calcular columna de importe total
        data['importe_total'] = data['unidades_vendidas'] * data['precio_unitario']  
    except FileNotFoundError:
        print("El archivo 'ventas.csv' no se encontró. Asegúrate de que el archivo esté en el directorio correcto.")
        data = pd.DataFrame()  # Crear un DataFrame vacío como respaldo
    return data
#Barras (bar) comparar
def gra_barras(data, columna_x, columna_y, titulo):
    plt.figure(figsize=(10,6))
    plt.bar(data[columna_x].groupby(data[columna_x]).sum().index, data[columna_y].groupby(data[columna_x]).sum().values, color='skyblue')
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def gra_lineas(data, columna_x, columna_y, titulo):
    plt.figure(figsize=(10,6))
    plt.plot(data[columna_x], data[columna_y], marker='o', linestyle='-', color='orange')
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def gra_pastel(data, columna, titulo):
    plt.figure(figsize=(8,8))
    data[columna].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title(titulo)
    plt.ylabel('')
    plt.show()

def main(): 
    # Leer un archivo CSV y cargarlo en un DataFrame de pandas
    data = carga_csv()
    if data.empty:
        print("No se pudo realizar el análisis debido a que el DataFrame está vacío.")
        return
    else:  
        # Realizar análisis de datos
        print(data.head())
        # Crear gráficos    
        gra_barras(data, 'producto', 'unidades_vendidas', 'Unidades Vendidas por Producto')
        gra_pastel(data, 'producto', 'Distribución de Ventas por Categoría')
        gra_lineas(data, 'fecha', 'importe_total', 'Importe Total de Ventas a lo Largo del Tiempo')
        

if __name__ == "__main__":
    main()  