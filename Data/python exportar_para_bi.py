import sqlite3
import pandas as pd

# 1. Conectarnos a nuestra base de datos existente
conexion = sqlite3.connect("bike_store.db")

# 2. Definir las tablas clave que necesitamos para las 3 vistas del Dashboard
tablas_a_exportar = [
    "customers",      # Datos de clientes
    "orders",         # Órdenes y fechas (para Vista 1)
    "order_items",    # Detalles de precios y cantidades (para Vista 1)
    "staffs",         # Empleados (para Vista 2)
    "stores",         # Tiendas y ciudades (para Vista 2)
    "stocks",         # Inventario (para Vista 3)
    "products"        # Productos (para Vista 3)
]

# 3. Bucle limpio para leer cada tabla de SQL y guardarla como CSV
for tabla in tablas_a_exportar:
    query = f"SELECT * FROM {tabla};"
    df = pd.read_sql(query, conexion)
    
    # Nombre del archivo resultante (ej. customers.csv)
    nombre_archivo = f"{tabla}.csv"
    df.to_csv(nombre_archivo, index=False)
    print(f" Archivo exportado con éxito: {nombre_archivo}")

# 4. Cerrar la conexión
conexion.close()
print("\n ¡Listo! Todos tus insumos están preparados para Power BI.")