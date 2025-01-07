from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_script(script_path):
    """Helper function to run scripts in the workflow."""
    result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
    print(f"Script {script_path} finished:\n{result.stdout}")
    return result.stdout

# DAG
dag = DAG(
    'data_pipeline',
    description='Data Generation, Ingestion and Processing Pipeline',
    schedule_interval='@hourly', 
    start_date=datetime(2024, 12, 29), 
    catchup=False
)

# Order of execution of tasks
task1 = PythonOperator(
    task_id='run_data_generator',
    python_callable=run_script,
    op_args=['Data_Generator/data_generator.py'],
    dag=dag
)

task2 = PythonOperator(
    task_id='run_kafka_producer',
    python_callable=run_script,
    op_args=['Data_ingestion/kafka_producer.py'],
    dag=dag
)

task3 = PythonOperator(
    task_id='run_kafka_consumer',
    python_callable=run_script,
    op_args=['Data_ingestion/kafka_consumer.py'],
    dag=dag
)

task4 = PythonOperator(
    task_id='run_process_job',
    python_callable=run_script,
    op_args=['Process_stream_data/process_job.py'],
    dag=dag
)

# Task dependencies (this ensures they run in order)
task1 >> task2 >> task3 >> task4


