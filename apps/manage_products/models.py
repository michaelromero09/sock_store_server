from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Designs(models.Model):
  design = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Products(models.Model):
  name = models.CharField(max_length = 255)
  dept = models.CharField(max_length = 255)
  style = models.CharField(max_length = 255)
  design = models.ForeignKey(Designs, related_name = 'products')
  material = models.CharField(max_length = 255)
  price = models.IntegerField()
  cost = models.IntegerField()
  image = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Sizes(models.Model):
  size = models.CharField(max_length = 50)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Product_Sizes(models.Model):
  size = models.ForeignKey(Sizes, related_name = 'product_sizes')
  product = models.ForeignKey(Products, related_name = 'product_sizes')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)