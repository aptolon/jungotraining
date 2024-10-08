from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quanity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    