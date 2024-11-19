from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('computers', 'Kompyuterlar'),
        ('laptops', 'Noutbuklar'),
        ('phones', 'Telefonlar'),
        ('tablets', 'Planshetlar'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='computers'
    )

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username