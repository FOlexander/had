from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2j@_^1^7777s+emur=9w&cg+j4'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1","83.229.87.94"]#потом юда прописіваем домен или ip адрес

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#STATIC_DIR = os.path.join(BASE_Dir,'static')
#STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')