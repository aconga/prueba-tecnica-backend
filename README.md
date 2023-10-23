# Backend Challenge

## Problema

A basic catalog system for managing products. A product must have basic information such as sku, name and price.

## Requisitos
In this system, we need to have at least two types of users:

- Administrators: create/update/delete products and to create/update/delete other administrators
- Anonymous user: who can only retrieve product information but cannot make changes
- Whenever an admin user makes a change in a product (for example, if a price is adjusted), we need to notify all other admins about the change, either via email or other mechanism.

## Solución
Este proyecto Django Rest Framework implementa un sistema de recomendación utilizando Redis como base de datos en memoria y Amazon Simple Email Service (SES) de AWS para enviar correos electrónicos a los clientes. A continuación, encontrarás información sobre cómo configurar, ejecutar y contribuir al proyecto.

## Configurar Variables de Entorno

Crea un archivo .env.dev en la raíz del proyecto con las siguientes variables de entorno, donde se define la variable del ambiente:
```sh
DJANGO_SETTINGS_MODULE=myshop.settings.local
```
En caso de utilizar el servicio SES de aws se debe agregar las sus credenciales:
```sh
AWS_ACCESS_KEY_ID = "aws_access_key"
AWS_SECRET_ACCESS_KEY = "aws_secret_access_key"
AWS_DEFAULT_REGION = "us-east-1"
```


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
