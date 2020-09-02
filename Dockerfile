FROM python:3.6

ENV PYTHONUNBUFFERED 0

RUN apt-get -y install \
    libpq-dev

WORKDIR /app

COPY . /app/

ADD ./requirements.txt /app/

VOLUME [ "./data" ]

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0:8000" ]
