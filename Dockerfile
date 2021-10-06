FROM python:3.9-alpine
WORKDIR /src
ENV QUART_APP=main:app
RUN apk add --no-cach postgresql-dev gcc python3-dev musl-dev linux-headers postgresql-client
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
