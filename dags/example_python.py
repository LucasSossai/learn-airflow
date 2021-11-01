from datetime import datetime, timedelta
from airflow import DAG

from python_scrpits.print_test import print_test
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "dag_example_python",
    default_args=default_args,
    description="Python example",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 11, 1),
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="print_test_python",
        python_callable=print_test,
    )

    t1
