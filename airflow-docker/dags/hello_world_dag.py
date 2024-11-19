from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

def _training_model ():
    return randint(1, 10)

def _choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
    ])

    best_accuracy = max(accuracies)

    if (best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'

with DAG('hello_world_dag', start_date=datetime(2024,1,1), schedule="@daily", catchup=False) as dag:

    # -- Tarefa 1  --
    training_model_A = PythonOperator(
        task_id='training_model_A',
        python_callable=_training_model
    )

    # -- Tarefa 2  --
    training_model_B = PythonOperator(
        task_id='training_model_B',
        python_callable=_training_model
    )

    # -- Tarefa 3  --
    training_model_C = PythonOperator(
        task_id='training_model_C',
        python_callable=_training_model
    )

    # -- Tarefa 4  --
    choose_best_model = BranchPythonOperator(
        task_id='choose_best_model',
        python_callable=_choose_best_model
    )

    # -- Tarefa 5 --
    accurate = BashOperator(
        task_id='accurate',
        bash_command="echo 'accurate'"
    )

    # -- Tarefa 6 --
    inaccurate = BashOperator(
        task_id='inaccurate',
        bash_command="echo 'inaccurate'"
    )

    [training_model_A, training_model_B, training_model_C] >> choose_best_model >> [accurate, inaccurate]