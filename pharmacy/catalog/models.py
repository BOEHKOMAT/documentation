from django.db import models


class Medicine(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=32)
    quantity = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=32)
    provisor_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_id = models.CharField(max_length=10)
    list = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.id
