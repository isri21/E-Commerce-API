from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name



class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.FloatField()
	stock = models.FloatField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
	owner = models.ForeignKey(user, on_delete=models.CASCADE, related_name="products_owned")

	def __str__(self):
		return self.name