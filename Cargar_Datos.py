import sqlite3
import pandas as pd
import os
import kagglehub

print("Descargando el dataset desde Kaggle...")

# 1. Descargamos la última versión del dataset usando kagglehub
path = kagglehub.dataset_download("dillonmyrick/bike-store-sample-database")
print(f"Dataset descargado con éxito \n Ruta de los archivos: {path}\n")

# 2. Conectamos (o creamos) nuestra base de datos SQLite local
db_name = "bike_store.db"   
conn = sqlite3.connect(db_name)

# Lista de las tablas del dataset de Bike Store
tablas = [
    "customers", 
    "products", 
    "categories", 
    "brands", 
    "orders", 
    "order_items", 
    "staffs", 
    "stores", 
    "stocks"
]

print("Iniciando la carga de archivos CSV a la base de datos...\n")

# 3. Recorremos cada tabla, la leemos con Pandas y la guardamos en SQLite
for tabla in tablas:

    ruta_csv = os.path.join(path, f"{tabla}.csv")
    
    if os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv)
        df.to_sql(tabla, conn, if_exists="replace", index=False)
        print(f"Tabla '{tabla}' cargada exitosamente ({len(df)} registros).")
    else:
        print(f"No se encontró el archivo '{tabla}.csv' en la ruta de Kaggle.")

# Cerramos la conexión a la base de datos
conn.close()
print("\n Listo. Base de datos 'bike_store.db' creada y poblada con éxito.")