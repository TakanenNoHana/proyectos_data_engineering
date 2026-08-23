import sqlite3
import pandas as pd

# 1. Conectarnos a la base de datos existente
conexion = sqlite3.connect("bike_store.db")

# 2. Leer una tabla completa usando pandas y un query SQL básico
query = "SELECT * FROM customers;"
df_clientes = pd.read_sql(query, conexion)

# 3. Cerrar la conexión 
conexion.close()

# 4. Analizar la calidad de los datos con pandas
nulos_por_columna = df_clientes.isnull().sum()

print("--- REPORTE DE CALIDAD DE DATOS ---")
print(nulos_por_columna)