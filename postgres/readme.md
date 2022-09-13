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