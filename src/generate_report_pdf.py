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
engine = create_engine(db_url)

# Consulta SQL para obtener los datos
query = '''
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
'''

# Ejecutar la consulta y cargar los datos en un DataFrame de pandas
df = pd.read_sql(query, engine)

# Convertir el DataFrame a HTML
df_html = df.to_html(index=False)  # Convertir a HTML sin índice

# Definir la ruta del template HTML para el reporte
template_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio actual
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('report_template.html')

# Renderizar el HTML con el contenido del DataFrame como HTML
html_content = template.render(data_table=df_html)

# Definir la ruta para el archivo PDF de salida
pdf_path = os.path.join(template_dir, 'sales_report.pdf')

# Ruta al ejecutable de wkhtmltopdf (asegúrate de que es correcta para tu sistema)
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Verifica si el archivo existe
if not os.path.exists(path_to_wkhtmltopdf):
    raise FileNotFoundError(f"El ejecutable wkhtmltopdf no se encuentra en: {path_to_wkhtmltopdf}")

# Configura pdfkit con la ruta correcta
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Generar el archivo PDF a partir del contenido HTML
pdfkit.from_string(html_content, pdf_path, configuration=config)

print("Reporte PDF generado exitosamente.")
