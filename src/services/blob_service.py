import os
import streamlit as st
from utils.config import Config
from azure.storage.blob import BlobServiceClient

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        blob_url = blob_client.url
        return blob_url
    except Exception as e:
        st.error(f"An error occurred while uploading to Azure Blob Storage: {e}")
        return None