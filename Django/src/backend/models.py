from django.db import models

# Tag Model (for easy filtering)
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField()
    rating = models.FloatField()
    stock = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    weight = models.FloatField()
    dimensions_width = models.FloatField()
    dimensions_height = models.FloatField()
    dimensions_depth = models.FloatField()
    warranty_information = models.CharField(max_length=255)
    shipping_information = models.CharField(max_length=255)
    availability_status = models.CharField(max_length=100)
    return_policy = models.CharField(max_length=255)
    minimum_order_quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=100)
    qr_code = models.URLField()
    images = models.JSONField()  # Store image URLs
    thumbnail = models.URLField()

    tags = models.ManyToManyField(Tag, related_name="products")

    def __str__(self):
        return self.title

# Review Model
class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()

    def __str__(self):
        return f"Review for {self.product.title} by {self.reviewer_name}"
