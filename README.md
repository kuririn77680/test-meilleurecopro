1) Install dependencies
- Ensure you have Poetry installed (https://python-poetry.org/)
- From the project root, install deps:
  
  ```bash
  poetry install
  ```
  
2) Start local PostgreSQL database (Docker):
```bash
docker run -d \
  -e POSTGRES_HOST_AUTH_METHOD=trust \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=backend_db \
  -p 5432:5432 postgres:14.5
```

3) Apply database migrations
- Move into the meilleurecopro folder:
  
  ```bash
  cd meilleurecopro
  ```
- Run migrations:
  
  ```bash
  poetry run python meilleurecopro/manage.py migrate
  ```

4) Start the application
```bash
poetry run python meilleurecopro/manage.py runserver
```

Notes:

you may need to change this in settings.py 

- CORS_ALLOWED_ORIGINS = [
    "http://localhost:63342",
]


Go further:

-write test suites

-implement error handling

-implement data valiation 

-change index.html to "real" front