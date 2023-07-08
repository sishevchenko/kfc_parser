import os
from dotenv import load_dotenv

load_dotenv(".env")


API_URL = os.getenv("API_URL")
DATABASE_URL = os.getenv("DATABASE_URL")
