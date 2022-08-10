from airflow import DAG
from airflow.operators.dummy import DummyOperator   #it's a operator that do nothing. It helps to make sexperiments.
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

with DAG(
        dag_id='simple_dag_class_b',
        schedule_interval="@daily",
        # schedule_interval="* */10 * * *",
        # schedule_interval="@weekly"
        # schedule_interval=timedelta(days=1)
        # schedule_interval=None - the dag will never be automated trigger
        start_date=days_ago(3),
        # start_date=datetime(2022, 8, 8),
        catchup=True,
        # if True, will run all Non-Triggered or Already Triggered DAGs;
        # if False, will run only last Non-Triggered or Already Triggered DAGs.
        max_active_runs=2    # if catchup=True, it will run only the nº set to run
) as dag:

    task_1 = DummyOperator(
        task_id='task_b',
        # start_date=datetime(2022, 8, 9) start_date can be set up in operator level, but, it's never recomendesd

    )
