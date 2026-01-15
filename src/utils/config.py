import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    ENDPOINT_KEY = os.getenv("ENDPOINT_KEY")
    STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")
    STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
    STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")