# Documentación del Proyecto: Análisis de Ingresos Netos por Línea de Productos y Almacén

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Fase 1: Planificación del Proyecto](#fase-1-planificación-del-proyecto)
3. [Fase 2: Configuración del Entorno](#fase-2-configuración-del-entorno)
4. [Fase 3: Exploración y Limpieza de los Datos](#fase-3-exploración-y-limpieza-de-los-datos)
5. [Fase 4: Consultas SQL Detalladas](#fase-4-consultas-sql-detalladas)
6. [Fase 5: Visualización de los Resultados en Power BI](#fase-5-visualización-de-los-resultados-en-power-bi)
7. [Requisitos](#requisitos)
8. [Instalación](#instalación)
9. [Uso](#uso)
10. [Contribuciones](#contribuciones)
11. [Licencia](#licencia)

## Introducción

Este proyecto tiene como objetivo analizar la variación de los ingresos netos por línea de productos y almacén durante los meses de junio, julio y agosto. Se exploran patrones de compra y se evalúa el rendimiento de diferentes almacenes y líneas de productos.

## Fase 1: Planificación del Proyecto

- **Objetivo del Proyecto**: Análisis de ingresos netos por línea de productos y almacén.
- **Entregables**:
  - Reporte SQL con consultas optimizadas.
  - Visualizaciones interactivas en Power BI.
  - Documentación técnica del proceso de análisis.
  - Código en Python para la automatización del proceso.

## Fase 2: Configuración del Entorno

1. **Base de datos PostgreSQL**: Crear una base de datos y cargar datos usando `SQLAlchemy` y `Pandas`.
2. **Archivo de Variables de Entorno**: Crear un archivo `.env` para almacenar configuraciones como `DATABASE_URL` y `CSV_PATH`.
3. **Entorno Virtual en Python**: Crear un entorno virtual para manejar dependencias.
4. **Script de Importación en Python**: Cargar datos desde un CSV a PostgreSQL.

## Fase 3: Exploración y Limpieza de los Datos

- Realizar transformaciones básicas de datos.
- Verificar la calidad de los datos y limpiar registros nulos o erróneos.

## Fase 4: Consultas SQL Detalladas

- Consultas para analizar ingresos netos por línea de producto y almacén.
- Análisis de estacionalidad y patrones de compra.
- Comparación de rendimiento de almacenes y líneas de productos.

## Fase 5: Visualización de los Resultados en Power BI

- Creación de un dashboard con visualizaciones clave.
- Análisis predictivo simple para proyectar tendencias de ventas.

## Requisitos

- PostgreSQL
- Python 3.x
- Bibliotecas: `pandas`, `sqlalchemy`, `python-dotenv`, `powerbi`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <url_del_repositorio>
   ```
