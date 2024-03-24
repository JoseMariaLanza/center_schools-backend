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

# Facebook config
Center Schools
1. User Token - 
EAAUWXkLR8XQBAJBjhZAgrZBYiBsNvaZC824cEghxtZBqsW1poEww9LIxwRfb6ujH30hRG3nFqlLGvz9xXUOLexsoZC8LzBvVNkWuj4FzDyyiCbJoZBmJkHHOulkUbkaQXCUJxXRPrvezqhZAIzTEyNDYHddWLtv829JY3RNy3vqf5ruZAnx42YK6
1. App Token -
1431968987345268|Luzp5p4_XROsOarTTjmY4DKDI_M

command
```
curl -X POST -d "grant_type=convert_token&client_id=1431968987345268&client_secret=a05659ad279b6d69aa264786f95904b1&backend=facebook&token=W8oxbotRiG3dzcsVbRtX3XsbWKxhyC" http://localhost:8000/auth/convert-token
```