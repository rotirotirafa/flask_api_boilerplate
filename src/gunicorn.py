import os

bind = f'{os.environ.get("HOST")}:{os.environ.get("PORT")}'

workers = 2 if os.environ.get("ENVIRONMENT") != "production" else 6
worker_class = "gevent"
worker_connections = 1000

max_requests = int(workers * worker_connections)

keepalive = 2
max_requests_jitter = 5
timeout = 60
threads = 2
reload = True