### Зависимости
- docker
- python 3.10.4
- postgres 13
- ports db: 5432, api: 7654, web: 7655

### Расположение сервисов
- api - http://localhost:7654
- web - http://localhost:7655 

### Этапы запуска (необходимо находиться в папке проекта)

---
**Запуск сервисов db, api, web(pyramid)**
```
1. docker-compose --env-file ./prod.env up -d --build
```

---
**Запуск скрипта на загрузку данных**
```
1. python -m venv venv
2. .\venv\Scripts\activate
3. cd upload_script
4. pip install -r requirements.txt
5. python main.py
    - python main.py -t 1 -u http://localhost:7654/upload/document/
    - аргумент -t кол-во потоков
    - аргумент -u ссылка для загрузки
```
