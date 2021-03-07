# Synchro server 
A simple service with a microservice architecture in the same source code. build faster, build smarter, Websocket is easy and accessible with Synchro server. For real time application.


<br>

Development requirements:
<li>TDD</li>
<li>GitFow</li>

<br>

## Run development environment

### With Docker compose

Set .ENV file
```bash
cp ./.env.example  ./.env
```
First create the docker-compose network, then launch the Server
```bash
docker-compose up
```
<br>

### With Bash
Set .ENV file
```bash
cp ./.env.example  ./.env

```
Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

Make migrations
```bash
python3 manage.py makemigrations
```

Run migrations
```bash
python3 manage.py migrate
```

Launch the Server

```bash
python3 manage.py runserver
```

<br>
<br>

## Run test environment
<br>
<br>

### With Docker compose
``` bash 
docker-compose  -f docker-compose-test.yml up
```

### With Bash
``` bash 
python3 manage.py runserver
```
