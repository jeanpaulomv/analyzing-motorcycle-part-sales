import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import nbformat as nbf

# Cargar variables de entorno
load_dotenv()

# Obtener detalles de conexión desde las variables de entorno
db_url = os.getenv('DATABASE_URL')

# Conectarse a PostgreSQL
engine = create_engine(db_url)

# Definir las consultas SQL
queries = {
    'net_revenue': '''
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
        ORDER BY product_line, EXTRACT(MONTH FROM date), net_revenue DESC;
    ''',
    'seasonality': '''
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
    ''',
    'payment_methods': '''
        SELECT payment,
               SUM(total) AS total_revenue,
               SUM(payment_fee) AS total_fees
        FROM sales
        GROUP BY payment;
    ''',
    'warehouse_performance': '''
        SELECT
            warehouse,
            SUM(quantity) as products_quantity,
            ROUND(AVG(quantity), 2) AS avg_products,
            SUM(total) - SUM(payment_fee) AS net_revenue
        FROM sales
        GROUP BY warehouse
        ORDER BY net_revenue DESC;
    ''',
    'product_line_performance': '''
        SELECT
            product_line,
            SUM(quantity) as products_quantity,
            ROUND((SUM(total) - SUM(payment_fee)) / SUM(quantity), 2) AS revenue_per_unit,
            ROUND(AVG(total), 2) AS avg_total,
            SUM(total) - SUM(payment_fee) AS net_revenue
        FROM sales
        GROUP BY product_line
        ORDER BY net_revenue DESC;
    '''
}

# Ejecutar cada consulta y almacenar los resultados en un diccionario de DataFrames
dataframes = {}
for key, query in queries.items():
    dataframes[key] = pd.read_sql(query, engine)

# Crear un nuevo notebook
nb = nbf.v4.new_notebook()

# Agregar una celda de texto para el título
nb.cells.append(nbf.v4.new_markdown_cell("# Reporte de Ventas"))

# Agregar una celda de texto con la descripción
nb.cells.append(nbf.v4.new_markdown_cell("Este notebook contiene un análisis de las ventas."))

# Agregar celdas de código y resultados
for key, df in dataframes.items():
    # Agregar celda de texto con el nombre de la consulta
    nb.cells.append(nbf.v4.new_markdown_cell(f"## {key.replace('_', ' ').title()}"))
    
    # Agregar celda de código para mostrar el DataFrame
    code = f"import pandas as pd\n\ndf_{key} = pd.DataFrame({df.to_dict(orient='records')})\ndf_{key}"
    nb.cells.append(nbf.v4.new_code_cell(code))

# Guardar el notebook
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Crear la carpeta "output" si no existe

notebook_path = os.path.join(output_dir, 'sales_report.ipynb')

# Escribir el archivo .ipynb
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Reporte .ipynb generado exitosamente.")
