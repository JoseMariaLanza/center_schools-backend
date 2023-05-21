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

commands
```
# Original
curl -X POST -d "grant_type=password&username=jose@admin.com&password=123456&client_id=jpPSQFtQXlMqE9L4ZHAmMbrFgwe4EeiQxbLNZYc3&client_secret=pbkdf2_sha256$600000$EtuAFWaCmsrFRQjQccSuzl$D5MrfBPlVtN3gQUAWFhcmQp/bPGX+cS0vCTKmf7Jbhk=&backend=google-oauth2&token=<google_token>" http://localhost:8000/auth/token

# Edited by password and username (Access to APP 3 Own custom API)
curl -X POST -d "client_id=o9oLXJ5YBLiKJ6XrfMWy0kyZH24p7cRUahW8S3PC&client_secret=sHPKnWCL4anAcB8r8tGbXeNFLFS1g9pQJpRRQGgkeQDqAnPk6DwsTpi9YJovr5WCsi5sqFxcYBm9N4thIjNVn5tG5xjVfHSINK5hcjdBWpMuukuKlzYk3gaKM8iuSu9t&grant_type=password&username=jose@admin.com&password=123456" http://localhost:8000/auth/token
```