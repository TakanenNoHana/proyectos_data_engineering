-- ==========================================================
-- Análisis de Negocio: Rendimiento de Empleados por Ingresos
-- Descripción: Identifica qué vendedores generan más ingresos totales y en qué tienda operan.
-- ==========================================================

SELECT 
    st.first_name || ' ' || st.last_name AS nombre_empleado,
    s.store_name,
    COUNT(o.order_id) AS total_ordenes_atendidas,
    SUM(oi.quantity * oi.list_price) AS ingresos_totales_generados
FROM staffs st
INNER JOIN stores s ON st.store_id = s.store_id
INNER JOIN orders o ON st.staff_id = o.staff_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY st.staff_id, st.first_name, st.last_name, s.store_name
ORDER BY ingresos_totales_generados DESC;