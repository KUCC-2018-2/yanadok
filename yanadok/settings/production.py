from yanadok.settings.base import *
import os

DEBUG = False

ALLOWED_HOSTS = [os.environ['WEB_SERVER_URL']]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_URL'],
        'PORT': os.environ['DATABASE_PORT']
    }
}

SECRET_KEY = '@p1)x*c581_(g8=bj76ylhtg1asde4h#jkx%nl7o_l)*+x092q'

EMAIL_AUTH_HOST = 'yanadok.kucc.co.kr'

