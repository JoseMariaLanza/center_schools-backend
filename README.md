# CENTER SCHOOLS

1. Create a superuser
```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

2. Create new server in Postgres
2.1 Log as admin
2.2 Create new Server
    - General:
    - - Name: Center Schools
    - Connection:
    - - Host name/address: pg_container
    - - username: postgress
    - - password: supersecretpassword

### Run migrations
```
docker-compose run --rm app sh -c "python manage.py migrate"
```