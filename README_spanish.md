# Análisis de Ventas de Partes de Motocicletas 🏍️

## Descripción del Proyecto 📊

Este proyecto analiza datos de ventas de una empresa que comercializa partes de motocicletas, con un enfoque en las transacciones al por mayor. El objetivo del análisis es proporcionar insights útiles sobre las fuentes de ingresos, examinando líneas de productos, tarifas de pago y la distribución por almacenes. Este proyecto forma parte de un curso de DataCamp y demuestra mi capacidad para trabajar con grandes conjuntos de datos, realizar consultas SQL complejas y utilizar PostgreSQL para la gestión de datos.

## Pasos Clave en el Análisis 🔍

1. **Transformación de Datos:**

   - Las fechas se convirtieron en nombres de meses para simplificar el análisis.
   - Se restaron las tarifas de pago del valor total de los pedidos para calcular el ingreso neto.

2. **Filtrado y Agrupación de Datos:**

   - Se enfocó exclusivamente en pedidos al por mayor.
   - Se agruparon los datos por línea de producto, mes y almacén.
   - Se ordenaron los resultados por línea de producto, mes e ingreso neto.

3. **Gestión de la Base de Datos:**
   - Se utilizó PostgreSQL para almacenar y gestionar los datos de ventas.
   - Se empleó SQLAlchemy en Python para facilitar la importación y manipulación de datos.

## Tecnologías y Herramientas Utilizadas 🛠️

- **PostgreSQL:** Para la gestión de la base de datos.
- **SQLAlchemy:** Para conectar Python con PostgreSQL.
- **Pandas:** Para la manipulación de datos en Python.
- **Jupyter Notebook:** Para documentar el proceso de análisis.
- **Python:** Para la importación y transformación de datos.

## Cómo Usar Este Proyecto 🚀

1. **Clonar el Repositorio:**

   - `git clone <repository_url>`

2. **Instalar Dependencias:**

   - Asegúrate de tener todos los paquetes requeridos instalados. Consulta el archivo [`requirements.txt`](./requirements.txt).

3. **Ejecutar el Análisis:**
   - Sigue las instrucciones provistas en el [notebook de instrucciones del proyecto](./1_project_instructions/project_instructions.ipynb).

## Estructura de Archivos 📁

- [`.gitignore`](./.gitignore) - Especifica archivos y directorios que serán ignorados por Git.
- [`1_project_instructions/motorcycle.jpg`](./1_project_instructions/motorcycle.jpg) - Imagen utilizada en el proyecto.
- [`1_project_instructions/project_instructions.ipynb`](./1_project_instructions/project_instructions.ipynb) - Jupyter Notebook con las instrucciones del proyecto.
- [`README.md`](./README.md) - Este archivo de documentación.
- [`README_spanish.md`](./README_spanish.md) - Versión en español de la documentación.
- [`import_csv_to_postgresql.py`](./import_csv_to_postgresql.py) - Script en Python para importar datos del CSV a PostgreSQL.
- [`sales.csv`](./sales.csv) - Datos de ventas utilizados en el proyecto.

## Documentación e Instrucciones de Configuración 📑

1. **Instalación de Dependencias:**

   - Ejecuta `pip install -r requirements.txt` para instalar todas las bibliotecas necesarias.

2. **Configuración de Variables de Entorno:**

   - Crea un archivo `.env` en el directorio raíz y agrega lo siguiente:
     ```plaintext
     DATABASE_URL=tu_url_de_base_de_datos_aqui
     ```
   - Reemplaza `tu_url_de_base_de_datos_aqui` con la URL de tu base de datos PostgreSQL.

3. **Ejecución del Script en Python:**
   - Ejecuta el script [`import_csv_to_postgresql.py`](./import_csv_to_postgresql.py) para importar los datos del CSV a la base de datos PostgreSQL.
   - El script lee desde `sales.csv` y llena la tabla `sales` en tu base de datos PostgreSQL.

## Conclusión 🎯

Este proyecto proporciona información valiosa sobre los ingresos al por mayor por línea de producto, mes y almacén, ayudando a la empresa a comprender mejor su rendimiento financiero. El enfoque utilizado en este análisis es eficiente y se puede adaptar a escenarios comerciales similares.
