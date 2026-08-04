from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipeline.extract_pipeline import ExtractPipeline
from pipeline.transform_pipeline import TransformPipeline
from pipeline.gold_pipeline import GoldPipeline
from pipeline.load_pipeline import LoadPipeline


def run_extract():
    ExtractPipeline().run()


def run_transform():
    TransformPipeline().run()


def run_gold():
    GoldPipeline().run()


def run_load():
    LoadPipeline().run()


with DAG(
    dag_id="youtube_data_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    tags=["youtube", "etl"],
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=run_extract,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=run_transform,
    )

    gold = PythonOperator(
        task_id="gold",
        python_callable=run_gold,
    )

    load = PythonOperator(
        task_id="load",
        python_callable=run_load,
    )

    extract >> transform >> gold >> load