# Motorcycle Parts Sales Analysis 🏍️

## Project Description 📊

This project analyzes sales data for a motorcycle parts company, focusing on wholesale transactions. The analysis aims to provide actionable insights into revenue streams by examining product lines, payment fees, and warehouse distributions. This project is part of a DataCamp course and showcases my ability to work with large datasets, perform complex SQL queries, and utilize PostgreSQL for data management.

## Key Analysis Steps 🔍

1. **Data Transformation:**

   - Dates were converted to month names for simplified analysis.
   - Payment fees were subtracted from total order values to calculate net revenue.

2. **Data Filtering & Aggregation:**

   - Focused exclusively on wholesale orders.
   - Grouped data by product line, month, and warehouse.
   - Sorted the results by product line, month, and net revenue.

3. **Database Management:**
   - Utilized PostgreSQL to store and manage the sales data.
   - Employed SQLAlchemy in Python to facilitate data import and manipulation.

## Technologies & Tools 🛠️

- **PostgreSQL:** For database management.
- **SQLAlchemy:** To connect Python with PostgreSQL.
- **Pandas:** For data manipulation in Python.
- **Jupyter Notebook:** For documenting the analysis process.
- **Python:** For data import and transformation.

## How to Use This Project 🚀

1. **Clone the Repository:**

   - `git clone <repository_url>`

2. **Install Dependencies:**

   - Make sure you have all the required packages installed. Refer to the [`requirements.txt`](./requirements.txt) file.

3. **Run the Analysis:**
   - Follow the instructions provided in the [project instructions notebook](project_instructions.ipynb).

## File Structure 📁

- [`.gitignore`](./.gitignore) - Specifies files and directories to be ignored by Git.
- [`project_instructions/motorcycle.jpg`](project_instructions.ipynb) - Image used in the project.
- [`1_project_instructions/project_instructions.ipynb`](./1_project_instructions/project_instructions.ipynb) - Jupyter Notebook with project instructions.
- [`README.md`](./README.md) - This documentation file.
- [`README_spanish.md`](./README_spanish.md) - Spanish version of the documentation.
- [`import_csv_to_postgresql.py`](./import_csv_to_postgresql.py) - Python script to import CSV data into PostgreSQL.
- [`sales.csv`](./sales.csv) - Sales data used in the project.

## Documentation & Setup Instructions 📑

1. **Installing Dependencies:**

   - Run `pip install -r requirements.txt` to install all required libraries.

2. **Setting Up Environment Variables:**

   - Create a `.env` file in the root directory and add the following:
     ```plaintext
     DATABASE_URL=your_database_url_here
     ```
   - Replace `your_database_url_here` with your actual PostgreSQL database URL.

3. **Running the Python Script:**
   - Execute the script [`import_csv_to_postgresql.py`](./import_csv_to_postgresql.py) to import the CSV data into the PostgreSQL database.
   - The script reads from `sales.csv` and populates the `sales` table in your PostgreSQL database.

## Conclusion 🎯

This project provides valuable insights into the wholesale revenue by product line, month, and warehouse, helping the company to better understand their financial performance. The approach used in this analysis is efficient and can be adapted for similar business scenarios.
