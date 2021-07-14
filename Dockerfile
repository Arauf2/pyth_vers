FROM python:3.9.6-slim-buster

RUN apt-get update -y

COPY ./requirements.txt /app/requirements.txt


WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]