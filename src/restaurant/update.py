from datetime import datetime

import requests
from sqlalchemy.dialects.sqlite import Insert
from sqlalchemy.engine.base import Engine

from src.conf import API_URL
from src.db import engine as db_engine
from src.restaurant.models import Restaurant


def update_db(api_url: str = API_URL, engine: Engine = db_engine):
    data = requests.get(api_url).json()
    with engine.connect() as session:
        for restaurant in data.get("searchResults"):
            store_id = restaurant["storePublic"]["storeId"]
            city = restaurant["storePublic"]["contacts"]["city"]["ru"]
            street_address = restaurant["storePublic"]["contacts"]["streetAddress"].get("ru")
            title = restaurant["storePublic"]["title"]["ru"]
            latitude = restaurant["storePublic"]["contacts"]["coordinates"]["geometry"]["coordinates"][0]
            longitude = restaurant["storePublic"]["contacts"]["coordinates"]["geometry"]["coordinates"][1]
            start_time_local = restaurant["storePublic"]["openingHours"]["regular"]["startTimeLocal"]
            end_time_local = restaurant["storePublic"]["openingHours"]["regular"]["endTimeLocal"]
            features = 1 if "breakfast" in restaurant["storePublic"]["features"] else 0
            try:
                start, end = datetime.strptime(start_time_local, "%H:%M:%S").time(), \
                             datetime.strptime(end_time_local, "%H:%M:%S").time()
            except TypeError:
                start = end = None
            stmt = Insert(Restaurant).values(store_id=store_id,
                                             city=city,
                                             street_address=street_address,
                                             title=title,
                                             latitude=latitude,
                                             longitude=longitude,
                                             start_time_local=start,
                                             end_time_local=end,
                                             features=features)
            on_conflict_do_update_stmt = stmt.on_conflict_do_update(
                index_elements=["store_id"],
                set_=dict(city=city,
                          street_address=street_address,
                          title=title,
                          latitude=latitude,
                          longitude=longitude,
                          start_time_local=start,
                          end_time_local=end,
                          features=features))
            session.execute(on_conflict_do_update_stmt)
            session.commit()
