FROM alpine:3.4
RUN apk add --update sqlite
RUN mkdir /db
WORKDIR /db

COPY db/testdb.db /db/

ENTRYPOINT ["sqlite3"]
CMD ["testdb.db"]