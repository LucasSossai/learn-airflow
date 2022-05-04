from datetime import datetime, timedelta
from airflow import DAG

from python_scripts.print_test import print_test
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'dag_example_hibrido',
    default_args=default_args,
    description='Hybrid example',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2022, 5, 1),
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='print_test_python',
        python_callable=print_test,
    )

    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t3 = PythonOperator(
        task_id='print_test_python2',
        python_callable=print_test,
    )

    t4 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t5 = PythonOperator(
        task_id='print_test_python3',
        python_callable=print_test,
    )

    t1 >> [t2, t3] >> t4 >> t5
