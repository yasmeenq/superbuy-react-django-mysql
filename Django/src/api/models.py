from django.db import models
from rest_framework.serializers import ModelSerializer


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField()
    rating = models.FloatField()
    stock = models.IntegerField()
    tags = models.JSONField()  # List of tags
    brand = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    weight = models.FloatField()
    dimensions = models.JSONField()  # Stores width, height, depth as a JSON object
    warranty_information = models.TextField()
    shipping_information = models.TextField()
    availability_status = models.CharField(max_length=100)
    return_policy = models.TextField()
    minimum_order_quantity = models.IntegerField()
    reviews = models.JSONField()  # List of reviews
    meta = models.JSONField()  # Stores createdAt, updatedAt, barcode, qrCode
    images = models.JSONField()  # Stores image URLs
    thumbnail = models.URLField()

    class Meta:
        db_table = "products" 


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"