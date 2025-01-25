from rest_framework import serializers
from .models import Product, Review, Tag, Category

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'date', 'reviewer_name', 'reviewer_email']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'price', 'discount_percentage', 
                  'rating', 'stock', 'brand', 'sku', 'weight', 'dimensions_width', 
                  'dimensions_height', 'dimensions_depth', 'warranty_information', 
                  'shipping_information', 'availability_status', 'return_policy', 
                  'minimum_order_quantity', 'barcode', 'qr_code', 'images', 'thumbnail', 
                  'tags', 'reviews']