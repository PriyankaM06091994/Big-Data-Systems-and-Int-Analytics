from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
#from download import download_data
import boto3
import sqlalchemy as sql
import pandas as pd
from sqlalchemy.dialects import registry


def download_data():
    #s3 = boto3.resource('s3')
    s3 = boto3.resource('s3',
                      aws_access_key_id='AKIAQYGLQ5IZM4PSIV2S',
                      aws_secret_access_key='I2TmkMyB3RMpu3KacYCQAlP1CG0WadVpj7PP4VMP')
    # Replace with your bucket name and download directory
    bucket_name = s3.Bucket('airflow-ingest-data')
    #path = './data/'

    # download file into path
    for s3_object in bucket_name.objects.all():
        print('Downloading file {}..'.format(s3_object.key))
        filename = s3_object.key
        bucket_name.download_file(s3_object.key, filename)
    print('Download Complete!')


def ingest_to_snowflake():
    registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

# Setup an SQL Alchemy Engine object
# This will provide a connection pool for Pandas to use later

    engine = sql.create_engine(
        'snowflake://{u}:{p}@{a}/{d}/{s}?warehouse={w}&role={r}'.format(
            u="imposter",
            p="Welcome@1",
            a="uda10611.us-east-1",
            r="SYSADMIN",
            d="WEATHER",
            s="PUBLIC",
            w="COMPUTE_WH"
        )
    )

    try:

        data = pd.read_csv('lending_club_info.csv')
        table_name = 'lending_club_info'  # Removing the extension .csv
        data.to_sql(table_name, con=engine, index=False, if_exists='append', chunksize=16000)
        print("Data loaded in table {t}".format(t=table_name))

        data = pd.read_csv('lending_club_loan_two.csv')
        table_name = 'lending_club_loan_two'  # Removing the extension .csv
        data.to_sql(table_name, con=engine, index=False, if_exists='append', chunksize=16000)
        print("Data loaded in table {t}".format(t=table_name))

    finally:
        engine.dispose()

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'concurrency': 1,
    'retries': 0,
    'depends_on_past': False,
}

with DAG('Windows-Pipeline',
         catchup=False,
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:
    t0_download = PythonOperator(task_id='DownloadData',
                              python_callable=download_data)
    t1_ingest = PythonOperator(task_id='IngestData',
                                python_callable=ingest_to_snowflake)


t0_download >> t1_ingest