## Generate Secret Key
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Migration
```bash
cd mypoject
py manage.py makemigrations
py manage.py migrate
```

## Dependencies Updates (Generate Outside the Django Project)
pip freeze > requirements.txt

## Install Dependencies
pip install -r requirements.txt

## Run Development Server
```bash
cd mypoject
py manage.py runserver
```