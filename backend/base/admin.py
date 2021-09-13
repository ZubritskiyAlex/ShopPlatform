from django.contrib import admin

# Register your models here.
from .models import Product, Review, Order, OrderItem, ShippingAddress, Shop

admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
