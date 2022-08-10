from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
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


def _download_data_e(my_param, ds):
    print(my_param)


with DAG(
        dag_id='simple_dag_e',
        default_args=default_args,
        schedule_interval='@daily',
        start_date=days_ago(3),
        catchup=False
) as dag:

    downloading_data_e = PythonOperator(
        task_id='downloading_data_e',
        python_callable=_download_data_e,
        op_kwargs={'my_param': 42}
    )
