from airflow import DAG

# The DAG class will be used in order to instantiate a DAG object,
# and so create a data pipeline in airflow
"""
NOT THE BEST WAY
with DAG(dag_id='simple_dag') as dag:
    # task_1 = Operator(dag=dag)
    None
"""

# Statement (with) / DAG_Object / Parabeters / as dag:
with DAG(dag_id='simple_dag_class_a') as dag:
    None
    # 1º - Instantiate the DAG object;
    # 2º - the DAG ID, the first and most important parameter,
        # must be unique across all of DAGs, or will most recent DAGs
