from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
