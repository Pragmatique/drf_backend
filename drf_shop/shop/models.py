from django.db import models
from user.models import MyUser
from product.models import Product

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    owner = models.ForeignKey(MyUser, related_name='shops', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    objects = models.Manager()


class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, related_name='items', on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, related_name='shop_items', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.product

    objects = models.Manager()


class ShopClient(models.Model):
    shop = models.ForeignKey(Shop, related_name='clients', on_delete=models.CASCADE, null=False)
    client = models.ForeignKey(MyUser, related_name='shop_clients', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.shop + ' ' + self.client

    objects = models.Manager()
