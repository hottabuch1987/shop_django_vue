from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, verbose_name='заказчик')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=150, verbose_name='адрес')
    zipcode = models.CharField(max_length=100, verbose_name='почтовый индекс')
    place = models.CharField(max_length=120, verbose_name='место')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы продуктов'
        ordering = ['-created_at', ]

    def __str__(self):
        return f'имя:{self.first_name}: {self.phone}, дата:{self.created_at}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
