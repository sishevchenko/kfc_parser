-- SQL команда для создания таблицы
CREATE TABLE restaurant (
    store_id TEXT NOT NULL PRIMARY KEY,
    city TEXT NOT NULL,
    street_address TEXT NULL,
    title TEXT NULL, -- Название точки
    latitude REAL NULL, -- Долгота
	longitude REAL NULL, -- Широта
	start_time_local TIME NULL, -- Начало рабочего дня по локальному времени
	end_time_local TIME NULL, -- Конец рабочего дня по локальному времени
	features INTEGER NULL); -- Столбец соответствует аналогичному api kfc, но содержит тольког инфо о завтраке

-- Код для сброса таблицы
DROP TABLE restaurant;

-- Код запроса сокращенный
SELECT *
FROM restaurant
WHERE city = 'Новосибирск' and start_time_local < '08:45' and features = 1;

-- Полный код запроса
SELECT store_id, city, street_address, title, latitude, longitude, start_time_local, end_time_local, features
FROM restaurant
WHERE city = 'Новосибирск' and start_time_local < '08:45' and features = 1;
