FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

EXPOSE 9000

COPY . .

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements/prod.txt

RUN python3 manage.py collectstatic --noinput
