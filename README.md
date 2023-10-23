# Backend Challenge

## Problema

A basic catalog system for managing products. A product must have basic information such as sku, name and price.

## Requisitos
In this system, we need to have at least two types of users:

- Administrators: create/update/delete products and to create/update/delete other administrators
- Anonymous user: who can only retrieve product information but cannot make changes


## Development

Tener instalado docker y docker-compose
```sh
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
# SWAGGER
http://localhost:8000/docs/swagger/
```

## API

Login
```sh
Request:
/account/login/
body = {
	"username": "aconga",
	"password": "A142857.?"
}

Response:
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3OTYyNzUzLCJqdGkiOiI1M2MyY2ZlZDUwZTI0YjUzYWQxYzA5YjA4YjUyYTkxYyIsInVzZXJfaWQiOjV9.nk6YB6ttZ4DIKBkZ617jLZYhAikkc6VaW3al_m5QKxQ",
    "user": {
        "id": 5,
        "username": "aconga",
        "administrator": true,
        "email": "acongadev4@gmail.com"
    }
}
```

Registro de Usuario
```sh
Request:
/api/users/
body = {
    "username": "test",
	"email": "test@gmail.com",
	"password": "A152879u.Z?",
    "administrator": true
}

Response:
{
    "username": "test",
    "email": "test@gmail.com",
    "creator": null,
    "administrator": true
}
```
