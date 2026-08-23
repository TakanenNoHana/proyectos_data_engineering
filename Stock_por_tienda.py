import sqlite3
import pandas as pd

# 1. Conectarnos a la base de datos
conexion = sqlite3.connect("bike_store.db")

# 2. Consulta SQL optimizada para obtener el Top 10 de productos más vendidos por tienda + su stock actual
query_top10_con_stock = """
WITH VentasPorTienda AS (
    SELECT 
        s.store_id,
        s.store_name,
        p.product_id,
        p.product_name,
        SUM(oi.quantity) AS total_unidades_vendidas,
        ROW_NUMBER() OVER (PARTITION BY s.store_id ORDER BY SUM(oi.quantity) DESC) as ranking
    FROM order_items oi
    INNER JOIN orders o ON oi.order_id = o.order_id
    INNER JOIN stores s ON o.store_id = s.store_id
    INNER JOIN products p ON oi.product_id = p.product_id
    GROUP BY s.store_id, s.store_name, p.product_id, p.product_name
)
SELECT 
    v.store_name,
    v.product_name,
    v.total_unidades_vendidas,
    COALESCE(st.quantity, 0) AS stock_actual_en_tienda
FROM VentasPorTienda v
LEFT JOIN stocks st ON v.store_id = st.store_id AND v.product_id = st.product_id
WHERE v.ranking <= 10
ORDER BY v.store_name, v.total_unidades_vendidas DESC;
"""

# 3. Leer y exportar a CSV
df_top10 = pd.read_sql(query_top10_con_stock, conexion)
df_top10.to_csv("top10_vendidos_con_stock_por_tienda.csv", index=False)

# 4. Cerrar conexión
conexion.close()
print("Reporte del Top 10 de más vendidos y su stock generado con éxito: 'top10_vendidos_con_stock_por_tienda.csv'")