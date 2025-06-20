from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name='categories')

    def __str__(self):
        return self.name

class Publisher (models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name='publisher')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name='author')

    def __str__(self):
        return self.name