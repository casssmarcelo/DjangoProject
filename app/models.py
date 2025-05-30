from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name
