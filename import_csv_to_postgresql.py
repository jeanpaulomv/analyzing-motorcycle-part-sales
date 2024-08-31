import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener credenciales y detalles de conexión desde variables de entorno
db_url = os.getenv('DATABASE_URL')

# Conectar a PostgreSQL
engine = create_engine(db_url)

# Leer archivo CSV
df = pd.read_csv('sales.csv')

# Crear la tabla automáticamente e importar los datos
df.to_sql('sales', engine, index=False, if_exists='replace')

print("Table created and data imported successfully.")
