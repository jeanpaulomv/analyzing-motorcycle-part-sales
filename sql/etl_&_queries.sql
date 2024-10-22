-- FASE 3: Exploración de datos
SELECT * 
FROM sales
LIMIT 10;

-- Transformaciones básicas
ALTER TABLE sales
ALTER COLUMN unit_price TYPE NUMERIC(10, 2),
ALTER COLUMN total TYPE NUMERIC(10, 2),
ALTER COLUMN payment_fee TYPE NUMERIC(10, 2);

-- Verificar la calidad de los datos
-- Revisar la existencia de valores nulos o errores
SELECT *
FROM sales
WHERE warehouse IS NULL AND client_type IS NULL;

-- Identificar anomalías
SELECT * 
FROM sales
WHERE quantity < 0 OR unit_price < 0;

-- FASE 4: Consultas Detalladas
-- Ingresos netos al por mayor por línea de producto, mes y almacén.
SELECT 
	product_line,
	CASE 	WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
			WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
			WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
	END AS month,
	warehouse,
	SUM(total) - SUM(payment_fee) AS net_revenue
FROM sales
WHERE client_type = 'Wholesale'
GROUP BY product_line, EXTRACT(MONTH FROM date), warehouse
ORDER BY product_line, EXTRACT(MONTH FROM date), net_revenue DESC;

-- Estacionalidad y patrones de compra 
SELECT
	CASE 	WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
			WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
			WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
	END AS month,
	product_line,
	SUM(total) AS total_sales
FROM sales
GROUP BY EXTRACT(MONTH FROM date), product_line
ORDER BY EXTRACT(MONTH FROM date), total_sales DESC;

-- Análisis por Método de Pago
SELECT
	payment,
	SUM(total) AS total_revenue,
	SUM(payment_fee) AS total_fees
FROM sales
GROUP BY payment;

-- Análisis de Márgenes y Rendimiento
SELECT 
	warehouse,
	SUM(quantity) AS total_quantity,
	SUM(total) - SUM(payment_fee) AS net_revenue,
	ROUND((SUM(total) - SUM(payment_fee)) / SUM(quantity), 2) AS revenue_per_unit
FROM sales
GROUP BY warehouse
ORDER BY net_revenue DESC;
