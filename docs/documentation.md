# Proyecto de Análisis de Ingresos por Producto y Almacén

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Objetivos del Proyecto](#objetivos-del-proyecto)
3. [Entregables](#entregables)
4. [Configuración del Entorno](#configuración-del-entorno)
5. [Proceso ETL](#proceso-etl)
6. [Consultas SQL](#consultas-sql)
7. [Visualización de Resultados en Power BI](#visualización-de-resultados-en-power-bi)
8. [Herramientas Utilizadas](#herramientas-utilizadas)
9. [Requisitos](#requisitos)
10. [Conclusiones y Próximos Pasos](#conclusiones-y-próximos-pasos)

---

## Descripción General

Este proyecto se enfoca en el análisis de los ingresos generados por diferentes líneas de productos en diversos almacenes, específicamente durante los meses de junio, julio y agosto. El análisis aborda aspectos de estacionalidad, patrones de compra, impacto de los métodos de pago y rendimiento de cada almacén.

---

## Objetivos del Proyecto

- **Pregunta Principal**: ¿Cómo varían los ingresos netos por línea de productos y almacén durante los meses de junio, julio y agosto?
- **Subpreguntas**:
  - Identificar estacionalidad y patrones de compra.
  - Analizar el impacto de los métodos de pago en los ingresos netos.
  - Determinar el almacén con mayores ingresos y el de mejor rendimiento.
  - Identificar las líneas de productos más rentables y con mayor contribución al margen de beneficios.

---

## Entregables

1. **Reporte SQL**:

   - Consultas SQL que permitan extraer ingresos por línea de producto y almacén.
   - Identificación de patrones de ventas y estacionalidad.

2. **Dashboards en Power BI**:

   - Indicadores clave (ingresos por línea de producto, almacén y método de pago).
   - Visualización de tendencias y estacionalidad.

3. **Documentación Técnica**:

   - Descripción del flujo de trabajo y justificación de técnicas.
   - Procedimientos de ETL y transformaciones en SQL y Python.

4. **Código de Automatización en Python**:
   - Scripts para la carga y limpieza de datos.
   - Generación de reportes automatizados en PDF y Jupyter Notebook.

---

## Configuración del Entorno

1. **Base de datos PostgreSQL**:

   - Crear una base de datos PostgreSQL para almacenar y consultar los datos.
   - Optimizar la base de datos mediante indexación en columnas clave (e.g., `order_number`).

2. **Archivo de Variables de Entorno**:

   - Configurar un archivo `.env` para almacenar credenciales y rutas de archivos (`DATABASE_URL`, `CSV_PATH`, `WKHTMLTOPDF_PATH`).

3. **Entorno Virtual en Python**:
   - Crear un entorno virtual para gestionar las dependencias del proyecto, garantizando que las bibliotecas necesarias estén instaladas y aisladas.

---

## Proceso ETL

### 1. Extracción de Datos

- **Fuente**: Archivo CSV proporcionado por DataCamp, que simula ventas de retail.
- **Proceso**: Se utiliza `Pandas` para leer el CSV, aprovechando variables de entorno para facilitar la carga flexible de datos.

### 2. Transformación de Datos

- **Limpieza**:

  - Eliminar filas con valores nulos o inválidos.
  - Convertir la columna de fecha a tipo `datetime` y ajustar otros tipos de datos (`numeric` para valores monetarios).

- **Preparación para Carga**:
  - Indexar columnas críticas para optimizar las consultas.
  - Convertir columnas de datos a los tipos adecuados, utilizando `ALTER TABLE` en SQL para la estructura final.

### 3. Carga

- **Cargar Datos a PostgreSQL**:
  - Usar `SQLAlchemy` y `Pandas` para insertar los datos en la tabla `sales` de PostgreSQL.
  - Los datos pueden ser reemplazados (`replace`) o agregados (`append`) en función de la necesidad de actualización.

---

## Consultas SQL

### 1. Ingresos Netos por Línea de Producto, Mes y Almacén

Consulta para identificar los ingresos netos por cada línea de productos en cada almacén durante el período analizado, ayudando a determinar las líneas y almacenes con mejor desempeño.

### 2. Análisis de Estacionalidad y Patrones de Compra

Esta consulta identifica los patrones de ventas mensuales y estacionales, facilitando la identificación de tendencias de demanda.

### 3. Impacto del Método de Pago en Ingresos y Costos

Consulta para analizar cómo afecta cada método de pago el margen de ingresos, facilitando la optimización de métodos de pago para maximizar ingresos.

### 4. Análisis de Márgenes y Eficiencia por Almacén

Evalúa el rendimiento de cada almacén en términos de ingresos netos y rentabilidad, lo cual permite priorizar almacenes de mejor desempeño.

---

## Visualización de Resultados en Power BI

1. **Creación de Medidas Calculadas**:

   - Medidas para ingresos netos, totales, comisiones, margen, forecasting y rentabilidad por unidad.

2. **Dashboards Interactivos**:

   - **Ingresos Netos por Línea y Almacén**: Visualización de ingresos por producto y almacén, desglosados por mes.
   - **Análisis de Estacionalidad**: Gráfico de líneas para observar estacionalidad en ventas.
   - **Impacto de Métodos de Pago**: Gráfico circular para identificar la contribución de cada método al ingreso total.
   - **Rendimiento por Almacén**: Tarjetas de KPI para comparar almacenes y su margen de ingresos.

3. **Análisis Predictivo y Proyección de Tendencias**:
   - `Forecasting` para anticipar tendencias de ventas, facilitando la toma de decisiones sobre inventarios y promociones futuras.

---

## Herramientas Utilizadas

Este proyecto emplea diversas herramientas y tecnologías para cubrir el ciclo completo de análisis de datos, desde la ingesta hasta la visualización:

- **Python**: Usado para el procesamiento y limpieza de datos, así como la automatización de cargas y reportes.
  - **Pandas** y **NumPy**: Manipulación y limpieza de datos.
  - **SQLAlchemy**: Conexión y gestión de la base de datos PostgreSQL desde Python.
  - **dotenv**: Manejo de variables de entorno para una configuración segura y flexible del entorno.
- **PostgreSQL**: Base de datos relacional para el almacenamiento y procesamiento de grandes volúmenes de datos de ventas y transacciones.

- **Power BI**: Herramienta de visualización para crear dashboards interactivos con KPI y análisis de tendencias. Se usaron:

  - **Medidas Calculadas**: Para KPIs y análisis comparativo.
  - **Visualizaciones Interactivas**: Como gráficos de barras, líneas y pastel para análisis en profundidad de ingresos y patrones de estacionalidad.

- **Jupyter Notebook**: Para documentación adicional, análisis exploratorio y generación de reportes automatizados en formato PDF.

- **VS Code**: Editor de código para el desarrollo del proyecto, configuración de scripts y edición del archivo README.md.

---

## Requisitos

Para ejecutar este proyecto localmente, asegúrate de tener los siguientes elementos instalados y configurados:

1. **Python 3.8 o superior**: Requerido para los scripts de ETL y automatización.

   - Instalar dependencias del proyecto:
     ```bash
     pip install -r requirements.txt
     ```

2. **PostgreSQL**: Base de datos utilizada para el almacenamiento y consulta de datos.

   - Crea una base de datos PostgreSQL local y configura las credenciales de acceso en el archivo `.env`.

3. **Power BI Desktop**: Necesario para la creación y visualización de dashboards.

   - Las visualizaciones e informes están optimizados para Power BI Desktop, que permite la personalización y análisis interactivo de los datos.

4. **Archivo `.env`**: Configuración de variables de entorno para credenciales de base de datos y rutas de archivos.

   - Ejemplo de configuración en el archivo `.env`:
     ```makefile
     DATABASE_URL=postgres://usuario:contraseña@localhost:5432/nombre_db
     CSV_PATH=ruta/al/archivo.csv
     WKHTMLTOPDF_PATH=ruta/al/ejecutable_wkhtmltopdf
     ```

5. **wkhtmltopdf** (opcional): Para generar reportes automatizados en formato PDF desde Jupyter Notebook.

---

## Conclusiones y Próximos Pasos

Este análisis ofrece insights claros sobre el rendimiento de cada línea de producto y almacén, así como el impacto de los métodos de pago en los ingresos. Los próximos pasos incluyen:

- Evaluar estrategias de inventario y promociones en base a los patrones estacionales.
- Optimizar métodos de pago y priorizar aquellos con menores comisiones.
- Ampliar el análisis a otros períodos para validar tendencias de crecimiento y rentabilidad.

---

> **Nota**: Para detalles adicionales sobre los insights y gráficos, consulte el archivo de [notebook de resultados](/reports/sales_report.ipynb).
