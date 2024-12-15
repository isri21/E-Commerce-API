from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
	category = serializers.CharField(source="category.name")
	class Meta:
		model = Product
		fields = "__all__"