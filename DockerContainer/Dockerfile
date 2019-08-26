FROM alpine:3.4
RUN apk add --update sqlite
RUN mkdir /db
WORKDIR /db

COPY db/testdb.db /db/
COPY Solution_AliUysal_082619.sql /db/

ENTRYPOINT ["sqlite3"]
CMD ["testdb.db"]