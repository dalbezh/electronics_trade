# <p align="center">Electronics trade</p>
### Веб-приложение, с API интерфейсом реализующий модель сети по продаже электроники
___
[![Python](https://img.shields.io/badge/python-v3.9-orange)](https://www.python.org/downloads/release/python-394/)
[![Django](https://img.shields.io/badge/django-v3.2.20-green)](https://docs.djangoproject.com/en/4.2/releases/4.0.1/)
[![Postgres](https://img.shields.io/badge/postgres-v12.15-blue)](https://www.postgresql.org/docs/12/release-12-4.html)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
___
### Запуск приложения локально

1. Установка зависимостей. В качестве пакетного менеджера используется poetry
```shell
python3 -m pip install poetry &&
poetry install
```
2. В файле [.env.example](.env.example) находятся переменые окружения необходимые для запуска БД и самого проекта.
3. Запуск БД через docker-compose
```shell
docker-compose --env-file .env.example -f infra/docker-compose.yml up -d
```
4. Применить миграции
```shell
python3 electronics_trade/manage.py migrate
```
5. Для удобства были подготовлены csv-таблицы которые находятся в директории [datasets](./datasets). 
В них при необходимости можно добавить, убавить или изменить имеющиеся данные. 
Также создан [скрипт](./csv_to_json.py) для формирования [фикстур](./fixtures) из данных таблиц при помощи которого нужно сформировать фикстуры:
```shell
python3 csv_to_json.py
```
И непосредственно загрузить сформированные json файлы в БД:
```shell
python3 electronics_trade/manage.py loaddata fixtures/*.json
```
6. Запуск приложения:
```shell
python3 electronics_trade/manage.py runserver
```
___
### Структура приложения
Доступ к самому API реализуется **только** через Basic Auth.
Для этого нужно зарегистрировать суперпользователя, а затем через панель администрирование сделать "сотрудников".

Список URLs приложения:

| url                                      | Описание                                                                      |
|------------------------------------------|-------------------------------------------------------------------------------|
| http://localhost:8000/admin/             | Панель администрирования                                                      |
| http://localhost:8000/orgs/organization/ | Представления для всех организация                                            |
| http://localhost:8000/orgs/product/      | Представления для продуктов                                                   |
| http://localhost:8000/orgs/provider/     | Представления для всех организация являющиеся поставщиками                    |
| http://localhost:8000/docs/              | Swagger. В нем можно подробнее ознакомится доступными с роутами и их методами |
| http://localhost:8000/docs/schema/       | Схема Swagger`а в формате YAML                                                |

Схема базы данных приложения [orgs](./electronics_trade/orgs/models.py) выглядит следующим образом:
![db_schema](./img/db_schema.jpeg)
Имеется также отдельно пользовательское приложение [users](./electronics_trade/orgs/models.py), его модель наследуется от AbstractUser