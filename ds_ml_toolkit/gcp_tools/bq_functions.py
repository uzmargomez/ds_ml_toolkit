from google.cloud import bigquery,bigquery_storage

import pandas as pd
import logging

def execute_query(sql=None,project=None):
    bqclient = bigquery.Client(project=project)
    query_job = bqclient.query(sql)
    results = query_job.result()  # Waits for job to complete.
    return results

def bq_query_to_df(sql=None,project=None):
    bqclient = bigquery.Client(project=project)
    df = bqclient.query(sql).to_dataframe()
    return df

def bq_table_to_df(table_id,project=None):
    bqclient = bigquery.Client(project=project)
    bqstorageclient = bigquery_storage.BigQueryReadClient()
    rows = bqclient.list_rows(table_id)
    dataset = rows.to_dataframe(bqstorage_client=bqstorageclient)
    return dataset

def df_to_bq(dataframe, table_id, write_disposition="WRITE_TRUNCATE",project=None):
    bqclient = bigquery.Client(project=project)
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