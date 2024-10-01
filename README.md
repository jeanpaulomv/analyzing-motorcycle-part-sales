# Motorcycle Parts Sales Analysis 

## Project Description 

This project analyzes sales data from a company that sells motorcycle parts, focusing on wholesale transactions. The goal of the analysis is to provide useful insights into revenue sources by examining product lines, payment fees, and warehouse distribution. This project is part of a DataCamp course and demonstrates my ability to work with large datasets, perform complex SQL queries, and use PostgreSQL for data management.

## Key Steps in the Analysis 

1. **Data Transformation:**

   - Dates were converted to month names to simplify analysis.
   - Payment fees were subtracted from the total order value to calculate net revenue.

2. **Data Filtering and Grouping:**

   - Focused exclusively on wholesale orders.
   - Data was grouped by product line, month, and warehouse.
   - Results were sorted by product line, month, and net revenue.

3. **Database Management:**

   - PostgreSQL was used to store and manage sales data.
   - SQLAlchemy was employed in Python to facilitate data import and manipulation.
   - SQL queries were created to extract relevant information and generate reports.

## Technologies and Tools Used  

<p><img src="https://github.com/user-attachments/assets/f381507e-9c84-4136-80de-1c8986469ef5" alt="PostgreSQL" width="20" height="20"/> <b>PostgreSQL:</b> For database management.</p>
<p><img src="https://img.icons8.com/?size=512&id=123603&format=png" alt="SQLAlchemy" width="20" height="20"/> <b>SQLAlchemy:</b> To connect Python with PostgreSQL.</p>
<p><img src="https://img.icons8.com/color/48/000000/pandas.png" alt="Pandas" width="20" height="20"/> <b>Pandas:</b> For data manipulation in Python.</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="Jupyter" width="20" height="20"/> <b>Jupyter Notebook:</b> To document the analysis process.</p>
<p><img src="https://img.icons8.com/color/48/000000/python--v1.png" alt="Python" width="20" height="20"/> <b>Python:</b> For data import and transformation.
</p>

## File Structure 

- [`data`](data/sales.csv) - Sales data used in the project.
- [`image`](images/motorcycle.jpg) - Image used in the Notebook.
- [`notebook`](notebooks/project_instructions.ipynb) - Jupyter Notebook with project instructions.
- [`query solution`](sql/query_solution.sql) - SQL query used to extract and analyze data.
- [`script`](src/import_csv_to_postgresql.py) - Python script to import CSV data to PostgreSQL.
- [`.gitignore`](./.gitignore) - Specifies files and directories to be ignored by Git.
- [`README.md`](README.md) - This documentation file.
- [`README_spanish.md`](README_spanish.md) - Spanish version of the documentation.
- [`requirements.txt`](requirements.txt) - Install all dependencies.

## Documentation and Setup Instructions 

1. **Install Dependencies:**

   - Run `pip install -r requirements.txt` to install all necessary libraries.

2. **Set Up Environment Variables:**

   - Create a `.env` file in the root directory and add the following:
     ```plaintext
     DATABASE_URL=your_database_url_here
     ```
   - Replace `your_database_url_here` with your PostgreSQL database URL.

3. **Run the Python Script:**

   - Execute the [`import_csv_to_postgresql.py`](src/import_csv_to_postgresql.py) script to import CSV data into the PostgreSQL database.
   - The script reads from `sales.csv` and populates the `sales` table in your PostgreSQL database.

4. **Run SQL Query:**

   - Review and execute the query in [`query_solution.sql`](sql/query_solution.sql) to obtain the requested report.

## Conclusion 

This project provides valuable insights into wholesale revenue by product line, month, and warehouse, helping the company better understand its financial performance. The approach used in this analysis is efficient and can be adapted to similar business scenarios.

## Contact

If you have any questions or would like more information, feel free to contact me.

<a href="https://www.linkedin.com/in/jeanpaulomv/"><img src="https://img.shields.io/badge/jeanpaulomv-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" height="30"></a>
<a href="https://www.datascienceportfol.io/jeanpaulomv"><img src="https://img.shields.io/badge/Portfolio-255E63?style=for-the-badge&logo=About.me&logoColor=white" alt="Portfolio" height="30"></a>
