FROM python:3.6.7

ENV PYTHONBUFFERED 1

RUN apk add --no-cache linux-headers bash gcc \
    muskl-dev libjpeg-turbo-dev libpng libpq \
    postgresql-dev uwsgi uwsgi-python3 git \
    zlib-dev libmagic

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install -U -r /code/requirements.txt

CMD python3 manage.py migrate && \
    python3 manage.py makemigrations && \
    uwsgi --ini=/site/uwsgi.ini

