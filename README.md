## Instal pipenv library (If not existing)
```python
pip install pipenv
```

## Generate Secret Key
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Migration
```bash
cd myproject
py manage.py makemigrations
py manage.py migrate
```

## Run Virtual Environment
```bash
pipenv shell
```

## Dependencies Updates (Generate Outside the Django Project)
```bash
pip freeze > requirements.txt
```

## Install Dependencies
```bash
pipenv install -r requirements.txt
```

## Run Development Server
```bash
cd myproject
py manage.py runserver
```