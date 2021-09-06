from django.urls import path
from ..views.order_views import addOrderItems, getOrderById, updateOrderToPaid, getMyOrders, getOrders, \
    updateOrderToDelivered

urlpatterns = [

    path('', getOrders, name='orders'),
    path('myorders/', getMyOrders, name='myorders'),
    path('add/', addOrderItems, name='orders-add'),
    path('<str:pk>/deliver/', updateOrderToDelivered),
    path('<str:pk>/pay/', updateOrderToPaid, name='pay'),
    path('<str:pk>/', getOrderById, name='orders-add'),
]