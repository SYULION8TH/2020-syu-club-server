FROM python:3.6

ENV PYTHONUNBUFFERED 0

RUN apt update

RUN apt-get -y install vim

RUN apt-get -y install \
    libpq-dev

WORKDIR /app

COPY . /app/

ADD ./requirements.txt /app/

# VOLUME [ "/data" ]

ENV DJANGO_SETTINGS_MODULE api.settings.prod

RUN pip install -r requirements.txt
RUN pip install -r prod.txt

# CMD [ "gunicorn", "api.wsgi:application", "--bind=0.0.0.0:8000"]
