from dotenv import find_dotenv, load_dotenv
from os import environ

envpath = find_dotenv()
load_dotenv(dotenv_path=envpath)

DATABASE_URL = environ.get("DATABASE_URL")
