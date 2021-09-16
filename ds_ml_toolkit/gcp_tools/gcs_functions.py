from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def look_for_file(bucket_name,file_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    stats = storage.Blob(bucket=bucket, name=file_name).exists(storage_client)
    return stats

def parse_gcs_uri(uri_string):
    prefix = "gs://"
    if uri_string.find(prefix) != 0:
        raise Exception("The uri is not a gcs path")
    uri_string = uri_string.replace(prefix, "")
    split_path = uri_string.split("/")
    bucket = split_path[0]
    file_name = split_path[-1]
    uri_string = uri_string.replace(f"{bucket}/", "")
    directory = uri_string.replace(file_name, "")
    return {"bucket": bucket, "directory": directory, "file_name": file_name, "uri":uri_string}