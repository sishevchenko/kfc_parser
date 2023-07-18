import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


API_URL = os.getenv("API_URL")
DB_ENGINE = os.getenv("DB_ENGINE")
DB_NAME = os.getenv("DB_NAME")

DB_URL = DB_ENGINE + str(BASE_DIR / DB_NAME)
