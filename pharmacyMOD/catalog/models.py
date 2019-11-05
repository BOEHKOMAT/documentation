from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=32)
    provisor_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.CharField(max_length=500)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.user.name
