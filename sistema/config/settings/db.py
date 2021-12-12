from .base import BASE_DIR, os

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child(str(os.getenv('DB_LOCAL')))
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_PROD_NAME'),
        'USER': os.getenv('DB_PROD_USER'),
        #'PASSWORD': os.getenv('DB_PROD_PASS'),
        'HOST': 'db_postgres',
        'PORT': 5432
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prueba',
        'USER': 'uprueba',
        'PASSWORD': 'root2020',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}