from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name
    @property
    def all_sum(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        return total
    @property
    def all_items(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    #
    def __str(self):
        return self.order.customer.name
    @property
    def get_total(self):
        total = int(self.product.price) * int(self.quantity)
        return total