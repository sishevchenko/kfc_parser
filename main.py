import sqlite3
import sys
import time

from src.conf import BASE_DIR
from src.restaurant.update import update_db


def main():
    with sqlite3.connect('src/kfc_restaurant.db') as conn:
        # Проверяем наличие таблицы в БД
        if conn.execute(
                """SELECT name
                FROM sqlite_master
                WHERE type = 'table' AND name = 'restaurant';""").fetchone():
            update_db()
        # Проверяем был ли аргумент для сырого запроса на создание таблицы
        elif "-raw-sql" in sys.argv:
            conn.execute("""CREATE TABLE restaurant (
                        store_id TEXT NOT NULL PRIMARY KEY,
                        city TEXT NULL,
                        street_address TEXT NULL,
                        title TEXT NULL,
                        latitude REAL NULL,
                        longitude REAL NULL,
                        start_time_local TIME NULL,
                        end_time_local TIME NULL,
                        features INTEGER NULL);""")
            update_db()
        # Уведомляем пользователя о том, что он может использовать alembic для обновления БД
        else:
            print("table 'restaurant' not found in database\n",
                  "please create an alembic migration by running the following commands\n",
                  "cd {}\n".format(BASE_DIR),
                  "alembic revision --autogenerate -m \"migration_name\"\n",
                  "alembic upgrade head\n",
                  "you can learn more about Alebik migrations here:\n",
                  "https://alembic.sqlalchemy.org/en/latest/tutorial.html\n",
                  "or you can start script with '-raw-sql' argument to create table")


if __name__ == "__main__":
    print("start program")
    start = time.perf_counter()
    try:
        main()
        print("completed in {} sec".format(time.perf_counter() - start))
    except KeyboardInterrupt:
        print("stop program")
    except Exception as ex:
        print(ex)
else:
    print("It's not a module")
