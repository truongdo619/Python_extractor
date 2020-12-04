"""gunicorn WSGI server configuration."""
from os import environ


def max_workers():
    return environ.get('WORKER_QUANTITY', 8)


bind = '0.0.0.0:' + environ.get('PORT', '5050')
max_requests = 5000
worker_class = 'gevent'
workers = max_workers()