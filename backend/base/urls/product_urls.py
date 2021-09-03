
from django.urls import path

from ..views.product_views import getProduct, getProducts, deleteProduct

urlpatterns = [

    path('', getProducts, name="products"),
    path('<str:pk>/', getProduct, name="product"),

    path('delete/<str:pk>/', deleteProduct, name='product-delete'),

]