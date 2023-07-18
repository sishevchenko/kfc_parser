from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

from src.conf import DB_URL

BaseMeta: DeclarativeMeta = declarative_base()

engine = create_engine(DB_URL)
