from yanadok.settings.base import *

DEBUG = True
SECRET_KEY = '@p1)x*c581_(g8=bj76ylhtg1086e4h#jkx%nl7o_l)*+x092q'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yanadock',
        'USER': 'yanadock',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',

    }
}
