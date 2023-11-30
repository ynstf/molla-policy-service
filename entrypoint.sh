#!/bin/bash
APP_PORT=${PORT:-9999}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm auth.wsgi:application --bind "0.0.0.0:${APP_PORT}"