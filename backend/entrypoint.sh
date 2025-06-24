#!/bin/bash

# Exit if any command fails
set -e

# Apply migrations
echo "Applying database migrations..."
poetry run python manage.py migrate

# Collect static files (optional)
# poetry run python manage.py collectstatic --noinput

# Start the server
echo "Starting Django server..."
exec poetry run python manage.py runserver 0.0.0.0:8000
