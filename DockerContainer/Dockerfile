FROM alpine:3.4
RUN apk add --update sqlite
RUN apk add --update py-pip
RUN apk add --update py-flask
RUN pip install --upgrade pip
RUN pip install Flask-RESTful
RUN pip install sqlalchemy
RUN mkdir /db
WORKDIR /db

COPY db/testdb.db /db/
COPY Solution_AliUysal_082619.sql /db/
COPY rest-app/app.py /db/

EXPOSE 5000