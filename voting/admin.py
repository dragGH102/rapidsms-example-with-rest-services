# voting/admin.py
from django.contrib import admin

from .models import Choice

# add Choice to admin interface (e.g. http://localhost:8000/admin/)
# NOTE: before we can use it ==> we must update DB by python(3) manage.py makemigrations (create file) > migrate (apply migrations) > [NO! use migrte intead] syncdb
admin.site.register(Choice)