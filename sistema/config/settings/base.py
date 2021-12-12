# Variables de entorno
import os
from dotenv import load_dotenv
from unipath.path import Path
# 
from django.urls import reverse_lazy
# 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
BASE_DIR = Path(__file__).ancestor(3)
load_dotenv(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = str(os.getenv('SECRET_KEY'))

# Application definition
    
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps.core',
    'apps.ecommerce',
    'apps.users',
    'apps.products',
    'apps.carts',
    # Pruebas
    'apps.home',
)

THRID_PARTY_APPS = (
    'widget_tweaks',
    'easy_thumbnails',
    'session_security',
    # Debug
    #'debug_toolbar',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THRID_PARTY_APPS

#INTERNAL_IPS = ('127.0.0.1', )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    # Configuración del Debug toolbar
    #'debug_toolbar.middleware.DebugToolbarMiddleware',    
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Users Config
AUTH_USER_MODEL = 'users.User'

# Login and Logout Settings
# LOGIN_URL = reverse_lazy("users:login")
LOGIN_URL = reverse_lazy("users:login") # Para validar las expiraciones de sesiones
LOGOUT_REDIRECT_URL = reverse_lazy("users:logout")
LOGIN_REDIRECT_URL = reverse_lazy("index")

# Tiempo de las sesiones
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SECURITY_EXPIRE_AFTER = 300 #Duracion total de la sesion
SESSION_SECURITY_WARN_AFTER = 60

# Mensaje en libreria session_security.views PingView
MESSAGE_EXPIRED_SESSION = "Ha superado el tiempo maximo de inactividad. Por favor, ingrese de nuevo."

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Valores para la reduccion de Imagenes
THUMBNAIL_ALIASES = {
    '': {
        'mark': {'size': (200, 60), 'crop': True},
        'p_medium': {'size': (250, 232), 'crop': 'smat'},
        'p_mini': {'size': (180, 180), 'crop': 'smart'},
        # 'fondo': {'size': (30, 20), 'crop': True},
    },
}
