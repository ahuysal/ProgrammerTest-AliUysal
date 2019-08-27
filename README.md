# ProgrammerTest-AliUysal

> This repository is the solution to the assessment provided by Cherre. It includes a Dockerfile to create a virtual Alpine Linux machine on which to run the SQL script and a Python API to return the result set in JSON format.

## Installation (Windows 10 OS)

- Clone this repo to your local machine using `https://github.com/ahuysal/ProgrammerTest-AliUysal.git`
- Copy the archive file to an appropriate folder and extract it
- Click the extracted folder. SHIFT + Right Click and then start the command prompt
- Go to DockerContainer folder

```
cd .\DockerContainer\
```

- Issue below Docker commands to build the image using Dockerfile and then run the container using the built image

```
# Build image using Dockerfile
docker build -t aliuysal/cherre_sqlitedb .

# Run container using built image
docker run -it -p 5000:5000 aliuysal/cherre_sqlitedb
```


## Run

- SQL Script

```

```


```
python app.py
```

then go to http://localhost:5000/departments

you could drill down by deparments too!

try http://localhost:5000/dept/police
