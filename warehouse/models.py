from django.db import models

class Product(models.Model):
    name = models.CharField("Тауар атауы", max_length=150)
    quantity = models.PositiveIntegerField("Ағымдағы саны")
    min_stock = models.PositiveIntegerField("Ең аз қор мөлшері")

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_stock

    def __str__(self):
        return self.name
