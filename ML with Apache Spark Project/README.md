<div align="center">
  <h1>Build an ML Pipeline for Airfoil noise prediction</h1>  
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/Apache%20Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black" />
  <img src="https://img.shields.io/badge/jupyter-F37626.svg?style=for-the-badge&logo=jupyter&logoColor=white" />
</div>

## Project Scenario



## Tasks
### Task 1: Generate a Spark DataFrame from the CSV data
Read data from the provided CSV file, `employees.csv` and import it into a Spark DataFrame variable named `employees_df`.

:ballot_box_with_check: ***Solution:***  
```py
# Read data from the "emp" CSV file and import it into a DataFrame variable named "employees_df"  
employees_df = spark.read.csv('employees.csv', header=True, inferSchema=True)
```
<kbd><img width="800px" alt="image" src="images/Task1.png" /></kbd>
