import pandas as pd
from sqlalchemy import create_engine
from jinja2 import Environment, FileSystemLoader
import pdfkit
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener detalles de conexión desde las variables de entorno
db_url = os.getenv('DATABASE_URL')

# Conectarse a PostgreSQL
try:
    engine = create_engine(db_url)
except Exception as e:
    raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")

# Definir las consultas SQL
queries = {
    'net_revenue': '''
        SELECT 
            product_line,
            CASE 
                WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
                WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
                WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
            END AS month,
            warehouse,
            SUM(total) - SUM(payment_fee) AS net_revenue
        FROM sales
        GROUP BY product_line, EXTRACT(MONTH FROM date), warehouse
        ORDER BY product_line, EXTRACT(MONTH FROM date), net_revenue DESC
        LIMIT 10;
    ''',
    'seasonality': '''
        SELECT
            CASE 
                WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
                WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
                WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
            END AS month,
            product_line,
            SUM(total) AS total_sales
        FROM sales
        GROUP BY EXTRACT(MONTH FROM date), product_line
        ORDER BY EXTRACT(MONTH FROM date), total_sales DESC
        LIMIT 10;
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
            SUM(quantity) AS products_quantity,
            ROUND(AVG(quantity), 2) AS avg_products,
            SUM(total) - SUM(payment_fee) AS net_revenue
        FROM sales
        GROUP BY warehouse
        ORDER BY net_revenue DESC;
    ''',
    'product_line_performance': '''
        SELECT
            product_line,
            SUM(quantity) AS products_quantity,
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

# Verificar si los DataFrames están vacíos
for key, df in dataframes.items():
    if df.empty:
        print(f"Advertencia: La consulta '{key}' no devolvió resultados.")

# Convertir los DataFrames a HTML
df_htmls = {key: df.to_html(index=False) for key, df in dataframes.items()}

# Definir la ruta del template HTML para el reporte (dentro de la carpeta "templates")
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('report_template.html')

# Definir rutas absolutas para las imágenes
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images')
net_sales_image_path = os.path.abspath(os.path.join(image_dir, 'net_sales_by_product_line_&_month.png'))
seasonality_image_path = os.path.abspath(os.path.join(image_dir, 'seasonality_&_purchasing_patterns.png'))
payment_methods_image_path = os.path.abspath(os.path.join(image_dir, 'revenue_by_payment_method.png'))
warehouse_performance_image_path = os.path.abspath(os.path.join(image_dir, 'margin_&_performance.png'))
product_line_image_path = os.path.abspath(os.path.join(image_dir, 'product_lines.png'))

# Renderizar el HTML con el contenido de los DataFrames como HTML y las rutas de las imágenes
html_content = template.render(
    net_revenue=df_htmls['net_revenue'],
    seasonality=df_htmls['seasonality'],
    payment_methods=df_htmls['payment_methods'],
    warehouse_performance=df_htmls['warehouse_performance'],
    product_line_performance=df_htmls['product_line_performance'],
    net_sales_image_path=net_sales_image_path,
    seasonality_image_path=seasonality_image_path,
    payment_methods_image_path=payment_methods_image_path,
    warehouse_performance_image_path=warehouse_performance_image_path,
    product_line_image_path=product_line_image_path
)

# Definir la ruta para el archivo PDF de salida en la carpeta "output"
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Crear la carpeta "output" si no existe

pdf_path = os.path.join(output_dir, 'sales_report.pdf')

# Ruta al ejecutable de wkhtmltopdf (asegúrate de que es correcta para tu sistema)
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Verifica si el archivo existe
if not os.path.exists(path_to_wkhtmltopdf):
    raise FileNotFoundError(f"El ejecutable wkhtmltopdf no se encuentra en: {path_to_wkhtmltopdf}")

# Configura pdfkit con la ruta correcta
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Generar el archivo PDF a partir del contenido HTML
options = {
    'enable-local-file-access': None,
    'disable-smart-shrinking': None
}
pdfkit.from_string(html_content, pdf_path, configuration=config, options=options)

print("Reporte PDF generado exitosamente.")
