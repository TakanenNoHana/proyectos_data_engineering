import sqlite3
import pandas as pd

# 1. Conectarnos a nuestra base de datos bike_store.db
conexion = sqlite3.connect("bike_store.db")

# 2. Definir una consulta SQL
query = """
SELECT 
    s.store_name,
    p.product_name,
    p.product_id,
    st.quantity AS stock_disponible
FROM stocks st
INNER JOIN stores s ON st.store_id = s.store_id
INNER JOIN products p ON st.product_id = p.product_id
"""

# 3. Leer el resultado de la consulta y cargarlo en un DataFrame de pandas
df_reporte = pd.read_sql(query, conexion)

# 4. Cerrar la conexión a la base de datos 
conexion.close()

# 5. Exportar ese DataFrame a un archivo CSV nuevo
df_reporte.to_csv("reporte_inventario.csv", index=False)

print("¡Reporte generado y guardado con éxito como 'reporte_inventario.csv'!")