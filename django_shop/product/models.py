from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    stock = models.IntegerField(verbose_name='Stock')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
