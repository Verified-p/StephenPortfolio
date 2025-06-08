import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-production-secret-key')  # Set via environment variable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'  # Set this environment variable for production

# Add allowed hosts for production deployment
ALLOWED_HOSTS = ['stephenportfolio-p.onrender.com', 'localhost', '127.0.0.1']

# CSRF trusted origins (important for production)
CSRF_TRUSTED_ORIGINS = ['https://stephenportfolio-p.onrender.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'application',  # Make sure your application is listed here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'folio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Ensure you have a templates folder
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

WSGI_APPLICATION = 'folio.wsgi.application'

# Database settings (using SQLite for development, use a more robust DB like PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL in production
        'NAME': BASE_DIR / 'db.sqlite3',         # SQLite database file for dev
    }
}

# Password validation (Optional, just in case you need it for authentication)
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL to serve static files from
STATICFILES_DIRS = [BASE_DIR / 'static']  # Custom static directory (in development)

# Directory where static files will be collected for production
STATIC_ROOT = BASE_DIR / 'staticfiles'  # This will be the directory where collectstatic puts all the files

# Use hashed static files in production to avoid cache issues
if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Logging Configuration - Added to capture detailed logs for debugging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Set to DEBUG for more detailed logging
            'propagate': True,
        },
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SECURITY SETTINGS (for production)
SECURE_SSL_REDIRECT = not DEBUG  # Redirect HTTP to HTTPS in production
CSRF_COOKIE_SECURE = not DEBUG   # Set to True in production
SESSION_COOKIE_SECURE = not DEBUG  # Set to True in production
X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being embedded in an iframe (good for security)
SECURE_HSTS_SECONDS = 3600  # Forces browsers to only communicate over HTTPS (1 hour)

# Email settings (Optional for production)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Change if using SMTP server
EMAIL_HOST = 'smtp.gmail.com'  # Example SMTP server
EMAIL_PORT = 587  # Port for Gmail
EMAIL_USE_TLS = True  # Use TLS for security
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # Set via environment variable
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Set via environment variable

