from django.urls import path
from ..views.order_views import addOrderItems, getOrderById, updateOrderToPaid, getMyOrders

urlpatterns = [
    path('myorders/', getMyOrders, name='myorders'),
    path('add/', addOrderItems, name='orders-add'),
    path('<str:pk>/', getOrderById, name='orders-add'),
    path('<str:pk>/pay/', updateOrderToPaid, name='pay'),


]