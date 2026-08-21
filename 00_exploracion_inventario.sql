-- ==========================================================
-- Exploración: Catálogo completo de productos
-- Descripción: Muestra los productos con sus marcas y categorías asociadas.
-- ==========================================================

SELECT 
    p.product_id,
    p.product_name,
    b.brand_name,
    c.category_name,
    p.list_price
FROM products p
INNER JOIN brands b ON p.brand_id = b.brand_id
INNER JOIN categories c ON p.category_id = c.category_id
ORDER BY p.list_price DESC;