import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Загружаем переменные окружения из .env
load_dotenv()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ проекта
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')

# Режим отладки
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Разрешённые хосты (читаем из переменных окружения, разделяем по запятой)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Сторонние приложения
    'crispy_forms',
    'crispy_bootstrap5',
    'taggit',

    # Наши приложения
    'accounts',
    'notes',
    'tasks',
    'categories',
    'tags',
]

# Настройки для crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personal_notes_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Общая папка шаблонов
        ],
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

WSGI_APPLICATION = 'personal_notes_project.wsgi.application'
ASGI_APPLICATION = 'personal_notes_project.asgi.application'


# Настройки базы данных
# По умолчанию SQLite, для локальной разработки.
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3'),
}
# DATABASE_URL = os.getenv('DATABASE_URL')
# if DATABASE_URL:
#     # Можно использовать dj_database_url для упрощения
#     # pip install dj-database-url (опционально)
#     # Пример:
#     # import dj_database_url
#     # DATABASES = {
#     #    'default': dj_database_url.parse(DATABASE_URL)
#     # }
#     pass
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

# Локаль и часовой пояс
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Для продакшн окружений

# Медиа файлы (загружаемые пользователями)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Настройки аутентификации
# Можно использовать встроенную модель User или создать кастомную
AUTH_USER_MODEL = 'auth.User'  # при необходимости можно определить свою модель пользователей

# URL для перенаправления после входа
LOGIN_REDIRECT_URL = 'notes:note_list'
LOGOUT_REDIRECT_URL = 'notes:note_list'
LOGIN_URL = 'accounts:login'

# Безопасность (на продакшне включить):
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# Логи
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
