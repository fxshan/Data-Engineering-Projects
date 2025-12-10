# import the libraries
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# defining DAG arguments
default_args = {
    'owner': 'Yummy',
    'start_date': days_ago(0),
    'email': ['yummy@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define the tasks
# define the task 'unzip'
unzip_data = BashOperator(
    task_id='unzip',
    bash_command='cd /home/project/airflow/dags/finalassignment && tar -xzf tolldata.tgz',
    dag=dag,
)
# define the task 'extract_data_from_csv'
extract_data_from_csv = BashOperator(
    task_id='extract_csv',
    bash_command='cut -d"," -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > \
    /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)
# define the task 'extract_data_from_tsv'
extract_data_from_tsv = BashOperator(
    task_id='extract_tsv',
    bash_command="cut -f5,6,7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv | \
    tr '\t' ',' | tr -d '\r' > /home/project/airflow/dags/finalassignment/tsv_data.csv",
    dag=dag,
)
# define the task 'extract_data_from_fixed_width'
extract_data_from_fixed_width = BashOperator(
    task_id='extract_txt',
    bash_command="awk '{print $10,$11}' /home/project/airflow/dags/finalassignment/payment-data.txt | \
    tr ' ' ',' > /home/project/airflow/dags/finalassignment/fixed_width_data.csv",
    dag=dag,
)
# define the task 'consolidate_data'
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='cd /home/project/airflow/dags/finalassignment && \
    paste -d "," csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag=dag,
)
# define the task 'transform_data'
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='cd /home/project/airflow/dags/finalassignment && \
    paste -d "," <(cut -d "," -f1-3 extracted_data.csv) \
    <(cut -d "," -f4 extracted_data.csv | tr [a-z] [A-Z]) \
    <(cut -d "," -f5- extracted_data.csv) > ./staging/transformed_data.csv',
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
