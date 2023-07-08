from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

from conf import DATABASE_URL

BaseMeta: DeclarativeMeta = declarative_base()

engine = create_engine(DATABASE_URL)
