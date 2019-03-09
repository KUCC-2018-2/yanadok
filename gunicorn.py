daemon = True
bind = 'unix:/run/gunicorn.sock yanadok.wsgi:application'
workers = 5
