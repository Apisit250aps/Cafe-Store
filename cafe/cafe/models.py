from django.db import models

# Create your models here.


class Menu(models.Model):
    menu = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='menu/')
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    s_price = models.FloatField(null=True)
    m_price = models.FloatField(null=True)
    l_price = models.FloatField(null=True)
    sold = models.PositiveIntegerField(null=True)
    rating = models.IntegerField(null=True)


class Categories(models.Model):
    category = models.CharField(max_length=64)


class Orders(models.Model):
    menu_id = models.IntegerField()
    unit = models.PositiveIntegerField()
    size = models.CharField(max_length=8)
    price = models.IntegerField()
    order_by = models.CharField(max_length=64)
    order_date = models.DateField(auto_now_add=True)


class Carts(models.Model):
    menu_id = models.IntegerField()
    unit = models.PositiveIntegerField()
    price = models.IntegerField()
    size = models.CharField(max_length=8)

