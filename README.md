# BikeStore Data Engineering & Analytics Pipeline

## Descripción del Proyecto
Pipeline de ingeniería y análisis de datos desarrollado para simular el procesamiento de información transaccional de una cadena minorista de bicicletas (`BikeStore`). El proyecto implementa extracción, transformación y consultas analíticas avanzadas utilizando **Python**, **SQLite** y **SQL**, estructurado bajo buenas prácticas de arquitectura de software y control de versiones.

## Arquitectura del Repositorio
El proyecto está organizado de manera modular para separar el código fuente, la lógica de bases de datos y los insumos analíticos:
- `analisis_bike_store_sql/`: Contiene los scripts de consultas SQL para la exploración de inventario, clientes, marcas y productos.
- `src/`: Código fuente en Python para la ingesta de datos, validación de calidad y generación automatizada de reportes.
- `Data/`: Almacena la base de datos relacional (`bike_store.db`) y los datasets procesados en formato CSV.

## Stack Tecnológico
* **Lenguaje:** Python 3 (Pandas)
* **Base de Datos:** SQLite
* **Lenguaje de Consultas:** SQL Avanzado (Joins, CTEs, Funciones de Ventana / `ROW_NUMBER`)
* **Control de Versiones:** Git / GitHub

## Principales Reportes Generados
El sistema procesa y genera automáticamente reportes orientados a negocio, destacando:
1. **Control de Inventario y Logística (Top Products):** Consulta optimizada mediante CTEs para identificar el *Top 10 de productos más vendidos por tienda*, cruzado en tiempo real con el stock disponible (`quantity`) para la gestión de reabastecimiento.
2. **Análisis de Clientes y Ventas:** Exploración de comportamiento de compra y rendimiento comercial por sucursal.
