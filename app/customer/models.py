from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    tc = models.CharField(max_length=11, unique=True)  # length = 11 yap
    phone = models.CharField(max_length=12, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.tc

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
