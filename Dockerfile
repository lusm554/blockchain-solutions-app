FROM python:3.9-alpine
WORKDIR /src
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
RUN apk add --no-cach postgresql-dev gcc python3-dev musl-dev linux-headers postgresql-client
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
