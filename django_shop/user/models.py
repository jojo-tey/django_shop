from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=64, verbose_name='Password')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'shop_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
