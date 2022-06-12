FROM python:3.10.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/app

WORKDIR $APP_HOME

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev postgresql-client

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . $APP_HOME
RUN pip install -e .

CMD alembic -c production.ini upgrade head && gunicorn --paste production.ini --bind=0.0.0.0:$WEB_APP_PORT
