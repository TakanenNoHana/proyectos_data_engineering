-- ==========================================================
-- Análisis de Negocio: Productos más vendidos y control de stock
-- Descripción: Identifica los productos con mayores ventas totales para evaluar si el inventario actual es suficiente.
-- ==========================================================

SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_unidades_vendidas,
    SUM(oi.quantity * oi.list_price) AS ingresos_generados,
    SUM(st.quantity) AS stock_total_disponible
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
INNER JOIN stocks st ON p.product_id = st.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_unidades_vendidas DESC;