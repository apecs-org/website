from gunicorn.workers.base import Worker
from gevent import monkey

def post_fork_patch(server, worker: Worker):
    monkey.patch_all()


wsgi_app = "apecs.wsgi"
capture_output = True  # Capture log output from Django
errorlog = "-"  # log to stderr
loglevel = "info"
bind = "0.0.0.0:8000"
worker_class = "gevent"
# Because we are using 'gevent' worker, a lower number of actual workers
# is required, because every request spawns a new greenlet
workers = 2
post_fork = post_fork_patch
max_requests = 2000
max_requests_jitter = 20