from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=128)
    categoryImg = models.ImageField(upload_to='categoryImg')