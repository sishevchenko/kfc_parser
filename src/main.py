import sqlite3
import time

from src.restaurant.update_db import update_db


def main():
    with sqlite3.connect('kfc_restaurant.db') as conn:
        cursor = conn.cursor()
        if cursor.execute(
                """SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'restaurant';""").fetchone():
            update_db()
        else:
            cursor.execute("""CREATE TABLE restaurant (
            store_id TEXT NOT NULL PRIMARY KEY,
            city TEXT NOT NULL,
            street_address TEXT NULL,
            title TEXT NULL,
            latitude REAL NULL,
            longitude REAL NULL,
            start_time_local TIME NULL,
            end_time_local TIME NULL,
            features INTEGER NULL);""")
            update_db()


if __name__ == "__main__":
    print("start program")
    start = time.perf_counter()
    main()
    print("completed in {} sec".format(time.perf_counter() - start))
else:
    print("It's not a module")
