from django.contrib import admin

from .models import Category

# Add the Category model to admin interface
admin.site.register(Category)