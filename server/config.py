# -*- coding: utf-8 -*-
from datetime import timedelta
from os import environ
from psycopg2cffi import compat

# hack for pyscopg2 which does not work using lastest version
compat.register()


def getenv(env, default=None):
    envar = environ.get(env, default)
    if envar is None:
        raise ValueError('envvar %s is missing' % env)
    return envar


# serv

APP_HOSTNAME = getenv('SERVER_HOSTNAME')  # not use
APP_PORT = int(getenv('SERVER_PORT'))  # not use
APP_NAME = getenv('PROJECT_NAME')
APP_VERSION = getenv('PROJECT_VERSION')
APP_ENV = getenv('PROJECT_ENV')
APP_URL_PUBLIC = getenv('URL_PUBLIC')


# flask

DEBUG = getenv('FLASK_DEBUG', getenv('SERVER_DEBUG', False))
SECRET_KEY = '\xcc)R\xda\x87\xcb\xae\xfd\xdd\xdc\xc0g\x1b\xeeq\xc5'
MAX_CONTENT_LENGTH = 2 * 1024 * 1024
UPLOAD_FOLDER = 'app/static/upldwl'
ALLOWED_EXT = set(['jpg', 'png', 'jpeg'])


# Session

PERMANENT_SESSION_LIFETIME = timedelta(seconds=int(getenv('SERVER_TTL')))
SESSION_TYPE = 'redis'
SESSION_USE_SIGNER = True
SESSION_PROTECTION = 'strong'


# DB

SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s' % (
    getenv('DB_USER'),
    getenv('DB_PWD'),
    getenv('DB_HOST'),
    getenv('DB_DB')
)


# momentjs

MOMENT_CDN_FORCE_SSL = True


# cache

REDIS_CACHE_HOSTNAME = getenv('REDIS_CACHE_HOSTNAME')
REDIS_CACHE_PORT = int(getenv('REDIS_CACHE_PORT'))
# IMPORTANT: You should use
# app.config.update(CACHE_REDIS=StrictRedis(host=,port=))


# Sentry
# TODO


# i18n

LANGUAGES = ['es', 'en']
BABEL_DEFAULT_LOCALE = 'es'


# ReCaptcha From Flask-WFT

RECAPTCHA_PUBLIC_KEY = getenv('GOOGLE_CAPTCHA_KEY')
RECAPTCHA_PRIVATE_KEY = getenv('GOOGLE_CAPTCHA_SECRET')


# Content Security Policy

CSP = {
    'default-src': [
        '\'self\'',
    ],
}
