FROM python:3.10.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/app

WORKDIR $APP_HOME

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev postgresql-client

RUN pip install --upgrade pip
COPY /api/requirements.txt .
RUN pip install -r requirements.txt

COPY ./api $APP_HOME
COPY ./app/app/models $APP_HOME/app

CMD python main.py