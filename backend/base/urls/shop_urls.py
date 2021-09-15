from django.urls import path

from ..views.shop_views import get_shops, get_shop, create_shop, update_shop

urlpatterns = [

    path('update/<str:pk>/', update_shop, name='product-update'),
    path('createshop', create_shop, name="create-shop"),
    path('', get_shops, name="shops"),
    path('<str:pk>/', get_shop, name="shop"),



]