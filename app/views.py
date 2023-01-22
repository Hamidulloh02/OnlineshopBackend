from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    customer = Customer.objects.get(id=2)
    order,create = Order.objects.get_or_create(customer=customer,complete=False)
    items = order.orderitem_set.all()

    print("##############")

    print(order.all_sum,"$")
    print(order.all_items)

    print("###############")
    return HttpResponse('Django Loyiha')

