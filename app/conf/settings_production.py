from conf.settings import *
import os

DEBUG = False
# DEBUG = eval(os.environ.get("DEBUG", default=True))

# TEMPLATE_DEBUG = eval(os.environ.get("TEMPLATE_DEBUG", default=True))

# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

ALLOWED_HOSTS = ['127.0.0.1', 'trees-everywhere.herokuapp.com']

# DATABASES = {
#     'default': {
#         "ENGINE": os.environ.get("SQL_ENGINE"),
#         "NAME": os.environ.get("SQL_DATABASE"),
#         "USER": os.environ.get("SQL_USER"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD"),
#         "HOST": os.environ.get("SQL_HOST"),
#         "PORT": os.environ.get("SQL_PORT"),
#     }
# }

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "d4h107hr2o57td",
        "USER": "peuktxarjnzwkc",
        "PASSWORD": "ac8f25978e02d37fe54416120956bce1d086c2b8a482464ddd3a03528c77601b",
        "HOST": "ec2-3-224-8-189.compute-1.amazonaws.com",
        "PORT": "5432",
    }
}

