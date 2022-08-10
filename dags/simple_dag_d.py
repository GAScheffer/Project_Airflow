from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

"""
BASE OPERATOR TASKS:
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html
"""
default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        dag_id='simple_dag_d',
        default_args=default_args,
        schedule_interval='@daily',
        start_date=days_ago(3),
        catchup=False
) as dag:

    task_1_d = DummyOperator(
        task_id='task_1_d'
         )

    task_2_d = DummyOperator(
        task_id='task_2_d',
        # retry=3
         )
