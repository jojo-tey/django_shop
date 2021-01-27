from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField(verbose_name='Quantity')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = 'shop_order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
