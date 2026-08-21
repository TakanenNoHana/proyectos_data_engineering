-- ==========================================================
-- Análisis de Negocio: Ingresos totales por Ciudad de los Clientes
-- Descripción: Identifica qué ciudades generan más ingresos para la empresa.
-- ==========================================================

SELECT 
    c.city,
    COUNT(DISTINCT o.order_id) AS total_ordenes,
    SUM(oi.quantity * oi.list_price) AS ingresos_totales
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.city
ORDER BY ingresos_totales DESC;