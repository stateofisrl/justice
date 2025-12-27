import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing admin if exists
User.objects.filter(username='admin').delete()

# Create new superuser
User.objects.create_superuser('admin', 'admin@scamresolvedcsi.com', 'admin123')
print("Admin account created successfully!")
print("Username: admin")
print("Password: admin123")
