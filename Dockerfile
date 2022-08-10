FROM python:3.9-slim-buster
LABEL MAINTAINER="Ali Loloee Jahromi"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# RUN python manage.py collectstatic --noinput

# RUN adduser -D user
# USER user