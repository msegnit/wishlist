from django.db import models

# Create your models here.

class Item(models.Model):
    details= models.TextField(max_length=100)