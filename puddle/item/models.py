from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    # Class Meta is a kinf of configuration of a class/model
    # Correct and show teble name as you want
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
    
    # Show elemetns inside a table with their names 
    def __str__(self):
        return self.name


# Second database model is item

class Item(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Show elemetns inside a table with their names 
    def __str__(self):
        return self.name
