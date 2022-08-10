from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
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


def _download_data_f(**kwargs):
    with open('/tmp/my_file_f.txt', 'w') as f:
        f.write('my_data_f')


with DAG(
        dag_id='simple_dag_f',
        default_args=default_args,
        schedule_interval='@daily',
        start_date=days_ago(3),
        catchup=False
) as dag:

    downloading_data_f = PythonOperator(
        task_id='downloading_data_f',
        python_callable=_download_data_f,
    )

    waiting_for_data_f = FileSensor(
        task_id='waiting_for_data_f',
        fs_conn_id='fs_default_f',
        filepath='my_file_f.txt'
    )
