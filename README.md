# <p align="center">Electronics trade</p>
### Веб-приложение, с API интерфейсом реализующий модель сети по продаже электроники
___
___
БД
```shell
docker-composer --env-file .env.local -f ifra/docker-compose.yml up -d
```
___
Загрузка фикстур:
```shell
python3 electronics_trade/manage.py loaddata fixtures/*.json
```
___
