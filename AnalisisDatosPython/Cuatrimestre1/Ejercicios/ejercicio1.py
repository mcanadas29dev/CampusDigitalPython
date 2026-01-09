"""
Docstring for AnalisisDatosPython.Cuatrimestre1.Ejercicios.ejercicio1

"""
from pathlib import Path
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def carga_csv():
    """
    Carga un archivo CSV y devuelve un DataFrame de pandas.
    
    Parámetros:
    nombre_archivo (str): Ruta al archivo CSV.
    
    Retorna:
    pd.DataFrame: DataFrame con los datos del CSV.
    """
    try:
        data_file = Path(__file__).with_name("ventas.csv")
        data = pd.read_csv(data_file)
    except FileNotFoundError:
        print("El archivo 'ventas.csv' no se encontró. Asegúrate de que el archivo esté en el directorio correcto.")
        data = pd.DataFrame()  # Crear un DataFrame vacío como respaldo
    return data

def analisis_datos(data):
    """
    Realiza un análisis básico de los datos en el DataFrame.
    
    Parámetros:
    data (pd.DataFrame): DataFrame con los datos a analizar.
    """
    # Verificar valores nulos
    print("Verificación de valores nulos:")
    print(data.isnull().sum())
    
    # Estadísticas descriptivas
    print("\nEstadísticas descriptivas:")
    print(data.describe())
    
    # Información del DataFrame
    print("\nInformación del DataFrame:")
    print(data.info())
    
    # 1. Verificar NULLs en el dataframe completo
    print("Verificación de NULLs en el DataFrame:\n")
    print(data.isnull().sum())  # Cantidad de NULLs por columna
    print(data.isnull().any())  # ¿Hay al menos un NULL en cada columna?

    # 2. Visualizar filas con NULLs
    print("Filas con NULLs:\n")
    print(data[data.isnull().any(axis=1)])  # Todas las filas que tengan al menos un NULL

    # ============= ESTADÍSTICA BÁSICA =============
    print("\n" + "="*50)
    print("ESTADÍSTICA BÁSICA DEL DATAFRAME")
    print("="*50)

    # 1. Información general
    print("\nForma del DataFrame (filas, columnas):")
    print(data.shape)

    print("\nTipos de datos:")
    print(data.dtypes)

    print("\nInformación detallada:")
    print(data.info())
    
    print("\n Cambio de tipo de columna fecha a tipo datetime: ")
    if 'fecha' in data.columns:
        data['fecha'] = pd.to_datetime(data['fecha'], errors='coerce')
        print(data.dtypes)  
    data['importe_total'] = data['unidades_vendidas'] * data['precio_unitario']
    data['otra_columna'] = None
    print(data)
    data.drop(columns=['otra_columna'], inplace=True)
    print(data)
    data.rename(columns={'importe_total': 'total_venta'}, inplace=True)
    print(data)
    data_grupo = data.groupby('categoria')['total_venta'].sum().sort_values(ascending=False)
    for categoria, total in data_grupo.items():
        print(f"Categoría: {categoria}, Total de Ventas: {total:3}€")      
   # Muestro producto mas vendido
    producto_mas_vendido = data.groupby('producto')['unidades_vendidas'].sum().idxmax()
    total_vendido = data.groupby('producto')['unidades_vendidas'].sum()
    print(f"\nProducto más vendido: {producto_mas_vendido} con {total_vendido[producto_mas_vendido]} unidades vendidas.")
    print(f"\nProducto más vendido: {producto_mas_vendido} con {total_vendido} unidades vendidas.")
    
    
def estadistica(data):
    """
    Realiza un análisis estadístico básico de los datos en el DataFrame.
    
    Parámetros:
    data (pd.DataFrame): DataFrame con los datos a analizar.
    """
    # 2. Estadísticas descriptivas
    print("\nEstadísticas descriptivas (mean, std, min, max, etc):")
    print(data.describe())

    # 3. Estadísticas específicas
    print("\nMedia (mean) por columna:")
    print(data.mean())

    print("\nMediana (median) por columna:")
    print(data.median())

    print("\nDesviación estándar (std):")
    print(data.std())

    print("\nVarianza:")
    print(data.var())

    print("\nValor mínimo por columna:")
    print(data.min())

    print("\nValor máximo por columna:")
    print(data.max())

def graficos(data):
    """
    Crea gráficos representativos del DataFrame.
    
    Parámetros:
    data (pd.DataFrame): DataFrame con los datos a visualizar.
    """
    # Obtener columnas numéricas
    columnas_numericas = data.select_dtypes(include=[np.number]).columns.tolist()
    columnas_texto = data.select_dtypes(include=['object']).columns.tolist()
    
    if len(columnas_numericas) == 0:
        print("No hay columnas numéricas para graficar.")
        return
    
    # Crear figura con múltiples subgráficos
    fig = plt.figure(figsize=(15, 12))
    
    # 1. Histograma (distribución de la primera columna numérica)
    if len(columnas_numericas) >= 1:
        ax1 = fig.add_subplot(2, 3, 1)
        data[columnas_numericas[0]].hist(bins=20, ax=ax1, color='skyblue', edgecolor='black')
        ax1.set_title(f'Histograma: {columnas_numericas[0]}')
        ax1.set_xlabel('Valor')
        ax1.set_ylabel('Frecuencia')
    
    # 2. Box Plot (para detectar outliers)
    if len(columnas_numericas) >= 2:
        ax2 = fig.add_subplot(2, 3, 2)
        data[[columnas_numericas[0], columnas_numericas[1]]].boxplot(ax=ax2)
        ax2.set_title('Box Plot: Primeras dos columnas')
        ax2.set_ylabel('Valor')
    
    # 3. Scatter Plot (relación entre dos variables)
    if len(columnas_numericas) >= 2:
        ax3 = fig.add_subplot(2, 3, 3)
        ax3.scatter(data[columnas_numericas[0]], data[columnas_numericas[1]], 
                   alpha=0.6, color='green', s=50)
        ax3.set_title(f'Scatter: {columnas_numericas[0]} vs {columnas_numericas[1]}')
        ax3.set_xlabel(columnas_numericas[0])
        ax3.set_ylabel(columnas_numericas[1])
    
    # 4. Gráfico de línea (series temporales o evolución)
    if len(columnas_numericas) >= 1:
        ax4 = fig.add_subplot(2, 3, 4)
        ax4.plot(data[columnas_numericas[0]], marker='o', linestyle='-', color='red', linewidth=2)
        ax4.set_title(f'Línea: {columnas_numericas[0]}')
        ax4.set_xlabel('Índice')
        ax4.set_ylabel('Valor')
        ax4.grid(True, alpha=0.3)
    
    # 5. Gráfico de barras (si hay columna categórica)
    if len(columnas_texto) >= 1:
        ax5 = fig.add_subplot(2, 3, 5)
        value_counts = data[columnas_texto[0]].value_counts().head(10)
        ax5.bar(range(len(value_counts)), value_counts.values, color='orange', edgecolor='black')
        ax5.set_xticks(range(len(value_counts)))
        ax5.set_xticklabels(value_counts.index, rotation=45, ha='right')
        ax5.set_title(f'Barras: {columnas_texto[0]}')
        ax5.set_ylabel('Frecuencia')
    
    # 6. Matriz de correlación (heatmap)
    if len(columnas_numericas) >= 2:
        ax6 = fig.add_subplot(2, 3, 6)
        correlacion = data[columnas_numericas].corr()
        im = ax6.imshow(correlacion, cmap='coolwarm', aspect='auto')
        ax6.set_xticks(range(len(correlacion.columns)))
        ax6.set_yticks(range(len(correlacion.columns)))
        ax6.set_xticklabels(correlacion.columns, rotation=45, ha='right')
        ax6.set_yticklabels(correlacion.columns)
        ax6.set_title('Matriz de Correlación')
        plt.colorbar(im, ax=ax6)
    
    plt.tight_layout()
    plt.show()

def ventas_por_categoria(data):
    """
    Calcula las ventas totales por categoría.
    
    Parámetros:
    data (pd.DataFrame): DataFrame con los datos.
    """
    # Detectar columnas de categoría y ventas
    columnas = data.columns.tolist()
    
    # Buscar columnas que contengan "categoria", "category", "tipo", "type"
    col_categoria = None
    for col in columnas:
        if 'categoria' in col.lower() or 'category' in col.lower() or 'tipo' in col.lower() or 'type' in col.lower():
            col_categoria = col
            break
    
    # Buscar columnas que contengan "venta", "ventas", "sales", "monto", "cantidad"
    col_ventas = None
    for col in columnas:
        if 'venta' in col.lower() or 'sales' in col.lower() or 'monto' in col.lower() or 'precio' in col.lower():
            col_ventas = col
            break
    
    if col_categoria is None or col_ventas is None:
        print("No se encontraron columnas de categoría o ventas.")
        print(f"Columnas disponibles: {columnas}")
        return
    
    print("\n" + "="*60)
    print(f"VENTAS TOTALES POR CATEGORÍA ({col_categoria})")
    print("="*60)
    
    # Método 1: groupby() simple - suma total por categoría
    print("\n1. Total de ventas por categoría:")
    ventas_por_cat = data.groupby(col_categoria)[col_ventas].sum().sort_values(ascending=False)
    print(ventas_por_cat)
    
    # Método 2: Múltiples agregaciones
    print(f"\n2. Estadísticas detalladas por categoría:")
    ventas_stats = data.groupby(col_categoria)[col_ventas].agg({
        'Total': 'sum',
        'Promedio': 'mean',
        'Cantidad': 'count',
        'Máximo': 'max',
        'Mínimo': 'min'
    }).round(2)
    print(ventas_stats)
    
    # Método 3: Como DataFrame para facilitar manipulación
    print(f"\n3. Como DataFrame:")
    ventas_df = data.groupby(col_categoria)[col_ventas].sum().reset_index()
    ventas_df.columns = [col_categoria, 'total_ventas']
    ventas_df = ventas_df.sort_values('total_ventas', ascending=False)
    print(ventas_df)
    
    # Método 4: Gráfico de barras por categoría
    print(f"\n4. Gráfico de ventas por categoría:")
    fig, ax = plt.subplots(figsize=(10, 6))
    ventas_por_cat.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
    ax.set_title(f'Ventas Totales por {col_categoria}', fontsize=14, fontweight='bold')
    ax.set_xlabel(col_categoria)
    ax.set_ylabel('Total de Ventas')
    ax.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    return ventas_df

def main(): 
    # Leer un archivo CSV y cargarlo en un DataFrame de pandas
    data = carga_csv()
    if data.empty:
        print("No se pudo realizar el análisis debido a que el DataFrame está vacío.")
        return
    else:  
        # Realizar análisis de datos
        analisis_datos(data)
        # Realizar análisis estadístico
            # estadistica(data)
        # Crear gráficos
            # graficos(data)
        # Calcular ventas por categoría
        # ventas_por_categoria(data)
        
if __name__ == "__main__":
    main()  

