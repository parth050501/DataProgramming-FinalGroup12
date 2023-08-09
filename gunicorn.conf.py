# gunicorn.conf.py

# Bind the application to this host and port
bind = "0.0.0.0:8081"

# Number of worker processes
workers = 2

# Worker class for handling requests
worker_class = "sync"

# Number of threads per worker process
threads = 4

# Timeout for worker processes
timeout = 120

# Location of the application module
# Change 'main:app' to the actual import path of your Flask app object
# For example: if your Flask app is defined in main.py as 'app', use 'main:app'
app = "main:app"

# Access log file
accesslog = "/path/to/access.log"

# Error log file
errorlog = "/path/to/error.log"

# Log level (debug, info, warning, error, critical)
loglevel = "info"

# Set to True to daemonize the Gunicorn process
daemon = False
