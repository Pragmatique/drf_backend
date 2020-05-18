from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    objects = models.Manager()
