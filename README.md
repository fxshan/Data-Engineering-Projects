<a id="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/fxshan/Data-Engineering-Projects.git">
    <img src="images/multilogos.png" alt="Projects" width="1000px">
  </a>
  <h1>Data Engineering Projects</h1>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" /><br>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white" /><br>
  <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white" /><br>  
  <img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black" />
  <img src="https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black" />
  <img src="" />

  
</div>

This repository is a collection of data engineering projects covering a variety of topics, including Python, SQL, Shell scripting, ETL, Airflow, EDW, DBA tasks, NoSQL, BI solutions, and Big Data with Hadoop and Spark.  

## Project Recap
### Python Project 
- Extracted and transformed global banking market-cap data into multiple currencies (USD/GBP/EUR/INR) using Python and Pandas.
- Built automated ETL pipelines with logging, stored outputs in CSV and SQL tables, and implemented database queries to serve localized market-cap values for regional teams.  

### RDBMS Project
- Designed a centralized relational database for a nationwide coffee shop expansion by integrating data from POS systems, supplier databases, spreadsheets, and CRM exports.
- Built normalized schemas, ERDs, and SQL database objects across PostgreSQL and MySQL.
- Delivered reusable views and materialized views to support executive analytics and operational reporting.

### Linux Shell Scripting Project 
- Developed an automated Linux backup script (backup.sh) to detect and archive encrypted password files updated within the last 24 hours.
- Implemented timestamp-based file scanning, compression logic, and safe path handling using Bash.
- Scheduled the script via cron for daily execution, improving reliability and eliminating manual backup errors.

### Database Administration Project 
- Designed, configured, and administered multi-platform database environments using PostgreSQL, MySQL, and Datasette.
- Performed user/role management, privilege grants, backup & recovery operations, and optimized query performance through indexing and storage-engine analysis.
- Built views, restored datasets, and benchmarked query improvements to ensure reliable, efficient data access across systems.

### Apache Airflow ETL Pipeline Project
- Designed and deployed an Apache Airflow DAG to extract multi-format toll-traffic data (CSV, TSV, fixed-width) from diverse highway operators.
- Implemented data consolidation and transformation workflows using BashOperator tasks.
- Orchestrated a full ETL pipeline with DAG submission, triggering, task dependency management, and monitoring.

### PostgreSQL Data Warehouse Project
- Designed and implemented a star-schema data warehouse for a national solid-waste management company, modeling date, waste type, and zone dimensions with a large fact table of truck trips.
- Loaded dimensional and fact data into PostgreSQL and optimized analytical queries using GROUPING SETS, ROLLUP, CUBE, and materialized views.
- Enabled multi-city reporting on annual, monthly, quarterly, and per-truck waste-collection metrics.
