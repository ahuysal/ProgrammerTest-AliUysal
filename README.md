# ProgrammerTest-AliUysal

> This repository provides the solution to the assessment by Cherre. It includes a Dockerfile to create a virtual Alpine Linux machine on which to run the SQL script and a Python API to return the result set in JSON format.

## Installation (Windows 10 OS)

- Download this repo to your local machine using `https://github.com/ahuysal/ProgrammerTest-AliUysal.git`
- Copy the archive file to an appropriate folder and extract it
- Go to extracted repo folder. Hold SHIFT + Right Click and then start the command prompt
- Go to DockerContainer folder

```
cd .\DockerContainer\
```

- Issue below Docker commands to build the image using Dockerfile and then to run the container using the built image

```
# Build image using Dockerfile
docker build -t aliuysal/cherre_sqlitedb .

# Run container using built image
docker run -it -p 5000:5000 aliuysal/cherre_sqlitedb
```


## Run

### SQL Script

- Connect to the testdb.db

```
sqlite3 testdb.db
```

- Turn on display for table column names

```
.headers on
```

- Run the SQL script

```
.read Solution_AliUysal_082619.sql
```

### Python API

- After launching the Docker container, simply run below command

```
python app.py
```

- Open a browser and go to http://localhost:5000/Visits
