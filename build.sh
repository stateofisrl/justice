#!/usr/bin/env bash
# Render build script
set -o errexit

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate --noinput

# Create superuser automatically (if doesn't exist)
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@scamresolvedcsi.com', 'admin123');
    print('Superuser created: admin / admin123');
else:
    print('Superuser already exists');
"

# Seed blog posts automatically
python manage.py seed_blog
