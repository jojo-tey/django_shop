from django.db import models

# Create your models here.


class Oder(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='Product')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Date')
