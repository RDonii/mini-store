import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    DB_STRING = 'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}'
    DB_USERNAME = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '8001')
    DB_NAME = os.getenv('DB_NAME', 'postgres')

    DB_STRING = DB_STRING.format(username=DB_USERNAME,
                                 password=DB_PASSWORD,
                                 host=DB_HOST,
                                 port=DB_PORT,
                                 db_name=DB_NAME)

    SECRET_KEY = os.getenv("SECRET_KEY")

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

config = Config()
