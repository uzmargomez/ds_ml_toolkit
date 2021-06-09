from google.cloud import bigquery
from google.cloud import storage
import pandas as pd
import logging

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def bq_query_to_df(sql):
    bqclient = bigquery.Client()
    df = bqclient.query(sql).to_dataframe()
    return df

def bq_table_to_df(table_id):
    bqclient = bigquery.Client()
    bqstorageclient = bigquery_storage.BigQueryReadClient()
    rows = bqclient.list_rows(table_id)
    dataset = rows.to_dataframe(bqstorage_client=bqstorageclient)
    return dataset

def df_to_bq(dataframe, table_id, write_disposition="WRITE_TRUNCATE"):
    bqclient = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        write_disposition=write_disposition,
    )

    job = bqclient.load_table_from_dataframe(
        dataframe, table_id, job_config=job_config
    )
    job.result()

    table = bqclient.get_table(table_id)
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )