from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'webserver',
    '127.0.0.1',
    'web-production-a9f18.up.railway.app'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'task_manager',  # добавляем сюда название проекта
    'task_manager.users',
    'django_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Сюда добавляем располжение директориии шаблонов
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

WSGI_APPLICATION = 'task_manager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Нужно для деплоя!
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600,
                                      conn_health_checks=True, )
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

    # {
    #  'NAME': 'django.contrib.auth.password_validation.'
    #           'UserAttributeSimilarityValidator',
    # },

    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 3,
        }
    },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.'
    #            'CommonPasswordValidator',
    # },
    # {
    #    'NAME': 'django.contrib.auth.password_validation.'
    #            'NumericPasswordValidator',
    # },
]

AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = BASE_DIR / "static"

CSRF_TRUSTED_ORIGINS = ['https://*.railway.app']

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "task_manager", "locale"),
)

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]
