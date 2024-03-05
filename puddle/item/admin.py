from django.contrib import admin

from .models import Category, Item

# Add the Category model to admin interface
admin.site.register(Category)
admin.site.register(Item)