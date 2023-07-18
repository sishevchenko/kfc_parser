from datetime import time

from sqlalchemy import String, Integer, Float, TIME
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta


class Restaurant(BaseMeta):
    __tablename__ = "restaurant"

    store_id: Mapped[str] = mapped_column(String, primary_key=True)
    city: Mapped[str] = mapped_column(String, nullable=True)
    street_address: Mapped[str] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String, nullable=True)
    latitude: Mapped[float] = mapped_column(Float, nullable=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=True)
    start_time_local: Mapped[time] = mapped_column(TIME, nullable=True)
    end_time_local: Mapped[time] = mapped_column(TIME, nullable=True)
    features: Mapped[int] = mapped_column(Integer, nullable=True)
