## 1. Create a Virtual Environment

```bash
python -m venv cybersecurity_env
```

## 2. Activate the virtual environment

```bash
.\cybersecurity_env\Scripts\activate
```

## 3. Install Poetry

```bash
pip install poetry
```

## 4. poetry lock

```bash
poetry lock
```

## 5. poetry install

```bash
poetry install
```

## 6. Create and Configure the Database, Make sure you have PostgreSQL running, then create a database named "project_cybersecurity"
- Between lines 83–90, make sure the database settings match your local PostgreSQL configuration (mysite/settings.py) :

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_cybersecurity',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## 7. Make Migrations

```bash
python manage.py makemigrations accounts
```

## 8. Apply Migrations

```bash
python manage.py migrate
```

## 9. Run the Development Server

```bash
python manage.py runserver
```

- Now you can test the APIs using graphQL in Postman, use this URL : http://127.0.0.1:8000/graphql/
