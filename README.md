# NoSQL-scanner


## About NoSQL-scanner

Project for Predprof Olympiad 2024. 

Web-App to scan vulnerabilities in NoSQL databases.



## Installation

If you want to start NoSQL-scanner locally, you need to install docker and docker-compose.

After the installation run this command:

```bash
make up
# or
docker compose -f docker-compose-dev.yaml up -d
```

To shutdown the service, run this command:

```bash
make down
# or
docker compose -f docker-compose-dev.yaml down
```

For additional commands see make help

```bash
make help
```
