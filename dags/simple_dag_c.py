from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
        dag_id='simple_dag_class_c',
        default_args=default_args,   # SETED TO AD THE DEFAULT_ARGS ON PARAMETERS
        schedule_interval="@daily",
        start_date=days_ago(3),
        catchup=False,
) as dag:

    task_1 = DummyOperator(
        task_id='task_c1',
        # retry=5, #NO NEED THIS LINE BECOUSE OF THE DEFAULT_ARGS SET
        # retry_delay=timedelta(minutes=5), #NO NEED THIS LINE BECOUSE OF THE DEFAULT_ARGS SET
    )

    task_2 = DummyOperator(
        task_id='task_c2',

    )

    task_3 = DummyOperator(
        task_id='task_c3',
        # retry=5, # NO NEED THIS LINE BECOUSE OF THE DEFAULT_ARGS SET
        # retry_delay=timedelta(minutes=5),#NO NEED THIS LINE BECOUSE OF THE DEFAULT_ARGS SET
    )
