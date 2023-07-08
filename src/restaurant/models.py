from datetime import time

from sqlalchemy import String, Integer, Float, TIME
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class Restaurant(BaseMeta):
    __tablename__ = "restaurant"

    store_id: Mapped[str] = mapped_column(String, primary_key=True)
    city: Mapped[str] = mapped_column(String)
    street_address: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    start_time_local: Mapped[time] = mapped_column(TIME)
    end_time_local: Mapped[time] = mapped_column(TIME)
    features: Mapped[int] = mapped_column(Integer)
