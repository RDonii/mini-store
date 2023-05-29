import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    DB_STRING = 'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}'
    DB_USERNAME = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
    DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '8001')
    DB_NAME = os.getenv('DB_NAME', 'postgres')

    DB_STRING = DB_STRING.format(username=DB_USERNAME,
                                 password=DB_PASSWORD,
                                 host=DB_HOST,
                                 port=DB_PORT,
                                 db_name=DB_NAME)

config = Config()
