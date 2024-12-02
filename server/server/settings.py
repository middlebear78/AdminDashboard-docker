import os
import json
import firebase_admin
from firebase_admin import credentials
from pathlib import Path
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

# Load environment variables from .env file
load_dotenv()

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Firebase initialization
if os.getenv('FIREBASE_CREDENTIALS'):
    cred = credentials.Certificate(
        json.loads(os.getenv('FIREBASE_CREDENTIALS')))
else:
    cred = credentials.Certificate("./config/fbServiceAccountKey.json")
firebase_admin.initialize_app(cred)

# Security settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'urisham.pythonanywhere.com',  # Add your specific domain
    '.pythonanywhere.com',
    '.vercel.app',
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'users',
    'vacations',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Removed: whitenoise middleware (not needed for PythonAnywhere)
    "auth.middleware.FirebaseAuthMiddleware",
    "auth.middleware.AdminCheckMiddleware",
]

ROOT_URLCONF = "server.urls"
WSGI_APPLICATION = "server.wsgi.application"

# Database settings - Simplified for PythonAnywhere MySQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": os.getenv('DB_HOST'),
        "PORT": os.getenv('DB_PORT', '3306'),
    }
}

# Removed: STATICFILES_STORAGE (not needed for PythonAnywhere)

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static and media files - Updated for PythonAnywhere
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Changed from 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:80",
    "https://*.vercel.app",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'token',
]

# Templates configuration
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

# Custom user model
AUTH_USER_MODEL = 'users.User'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"