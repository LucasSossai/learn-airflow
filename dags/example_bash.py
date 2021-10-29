from datetime import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}

dag = DAG(
    dag_id="example_bash",
    start_date=datetime(2021, 10, 29, 18),
    schedule_interval="*/1 * * * *",
    default_args=default_args,
)

task_1 = BashOperator(
    task_id="task_example_id_1",
    bash_command='echo "This is a bash test 1"',
    dag=dag,
)

task_2 = BashOperator(
    task_id="task_example_id_2",
    bash_command='echo "This is a bash test 2"',
    dag=dag,
)

task_1 >> task_2
