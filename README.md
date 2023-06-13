Тестовое задание
-------------------
1. Написать для криптобиржи Deribit асинхронный клиент на aiohhtp.
Клиент должен каждую минуту забирать с биржи текущую цену BTC и ETH, после чего сохранять в базу данных тикер валюты, текущую цену и время в UNIX.
2. Написать внешнее API для обработки сохраненных данных на FastAPI.

    Должны быть следующие методы:  

    * Получение всех сохраненных данных по указанной валюте
    * Получение последней цены валюты
    * Получение цены валюты с фильтром по дате   

    Все методы должны быть GET и у каждого метода должен быть обязательный query параметр "ticker".   
    Вместо pydantic-моделей желательно использовать dataclass-модели.
3. Написать тесты для клиента.
Написать простой тест на метод получения данных с биржи.   

Навигация по API
-----------------
Автодокументация доступна по адресу `0.0.0.0:8000/docs`   
* `/allCurrent` - Возвращает все данные из базы данных по выбранной валюте
* `/lastUpdate` - Возвращает новейшую цену данной валюты
* `/valueByDate` - Возвращает все данные по выбранной валюте за выбранную дату

Инструкция по запуску проекта
---------------------------------
На Linux или при наличии Makefile:
* Запуск проекта: `make up`
* Остановка проект: `make down`
* Вывод логи: `make logs`
* Миграция alembic: `make migrate-alembic`
* Запуск тесты: `make pytest`
* Открытие терминал внутри докер контейнера: `make open-bash`
* Полный перезапуск (в ноль): `make hard-restart`

На Windows или при отсутствии Makefile:
* Запуск проекта:   
    `docker compose up -d`
* Остановка проекта:    
    `docker compose down`
* Вывод логи:    
    `docker compose logs app -f`
* Миграция alembic:     
    `docker compose exec app alembic revision --autogenerate`   
    `docker compose exec app alembic upgrade head`
* Запуск терминала внутри докер контейнера:    
    `docker compose exec -it "app" bash`