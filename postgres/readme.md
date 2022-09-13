# Database Setup

## Old
```sh
docker search pgadmin4

docker pull dpage/pgadmin4:latest

docker images

docker ps

docker run dpage/pgadmin4 
```

## New
```sh
docker-compose up
```

In browser go to http://localhost:8080

---

Username `admin@admin.com`

Password `secret`

---

`Object` > `Create` > `Server`

---

Name: `<Whatever-you-want>`


Host: `postgres_container`

Pass: `secret`

Save: `true`

---

Create Virtual Docker Netowrk

```sh
docker network create <name-of-network>
docker network connect <name-of-network> <name-of-container>
docker netowrk inspect <name-of-network>
```

---

Docker stop / kill / reset all settings

```sh
docker stop <container-name>
docker rmi -f <image-name-or-id> 
docker image rm <image-id>

docker system prune --all --force --volumes
```