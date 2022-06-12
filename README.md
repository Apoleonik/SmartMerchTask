- docker
- python 3.10.4
- postgres 13
- ports 5432,7654,7655

Этапы запуска (необходимо находиться в папке проекта):

---
**Запуск БД**
1. docker-compose --env-file ./prod.env up -d db

---
**Запуск приложения pyramid**
1. python -m venv venv
2. .\venv\Scripts\activate
3. cd app
4. pip install -r requirements.txt
5. pip install -e git+https://github.com/pylons/pyramid.git@master#egg=pyramid
6. alembic -c production.ini upgrade head

----
1. python3 -m venv venv
2. pip install -e .
