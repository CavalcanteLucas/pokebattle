from .base import *  # noqa

import json
import os
import sys


with open(os.path.join(sys.path[0], 'backend/pokebattle/settings/credentials.json'), 'r') as json_data:
    credentials = json.load(json_data)

SECRET_KEY = credentials['password']

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": base_dir_join("db.sqlite3"),}
}

STATIC_ROOT = base_dir_join("staticfiles")
STATIC_URL = "/static/"

MEDIA_ROOT = base_dir_join("mediafiles")
MEDIA_URL = "/media/"

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Speed up password hashing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
