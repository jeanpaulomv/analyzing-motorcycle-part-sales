-- PHASE 3: Data exploration
SELECT * 
FROM sales
LIMIT 10;

-- Data transformation
ALTER TABLE sales
ALTER COLUMN unit_price TYPE NUMERIC(10, 2),
ALTER COLUMN total TYPE NUMERIC(10, 2),
ALTER COLUMN payment_fee TYPE NUMERIC(10, 2);

-- Checking data quality
-- Check for null values or errors
SELECT *
FROM sales
WHERE warehouse IS NULL AND client_type IS NULL;

-- Identify anomalies
SELECT * 
FROM sales
WHERE quantity < 0 OR unit_price < 0;

-- PHASE 4: Detailed Consultations
-- Net revenue by product line, month and warehouse.
SELECT 
	product_line,
	CASE 	WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
			WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
			WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
	END AS month,
	warehouse,
	SUM(total) - SUM(payment_fee) AS net_revenue
FROM sales
GROUP BY product_line, EXTRACT(MONTH FROM date), warehouse
ORDER BY product_line, EXTRACT(MONTH FROM date), net_revenue DESC
LIMIT 10;

-- Seasonality and purchasing patterns 
SELECT
	CASE 	WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
			WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
			WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
	END AS month,
	product_line,
	SUM(total) AS total_sales
FROM sales
GROUP BY EXTRACT(MONTH FROM date), product_line
ORDER BY EXTRACT(MONTH FROM date), total_sales DESC
LIMIT 10;

-- Revenue by Payment Methods
SELECT 
	payment,
	SUM(payment_fee) AS total_fees,
	SUM(total) AS total_revenue
FROM sales
GROUP BY payment
ORDER BY total_revenue DESC;

-- Margin and Performance Analysis by Warehouse and Product Line
-- Warehouse with the most net revenue and units sold
SELECT
	warehouse,
	SUM(quantity) as products_quantity,
	ROUND(AVG(quantity), 2) AS avg_products,
	SUM(total) - SUM(payment_fee) AS net_revenue
FROM sales
GROUP BY warehouse
ORDER BY net_revenue DESC;

-- Best-selling product line in units and dollars
SELECT
	product_line,
	SUM(quantity) as products_quantity,
	ROUND((SUM(total) - SUM(payment_fee)) / SUM(quantity), 2) AS revenue_per_unit,
	ROUND(AVG(total), 2) AS avg_total,
	SUM(total) - SUM(payment_fee) AS net_revenue
FROM sales
GROUP BY product_line
ORDER BY net_revenue DESC;