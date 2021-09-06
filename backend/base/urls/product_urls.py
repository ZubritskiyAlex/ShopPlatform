
from django.urls import path

from ..views.product_views import getProduct, getProducts, deleteProduct, createProduct, updateProduct, uploadImage

urlpatterns = [

    path('', getProducts, name="products"),
    path('create/', createProduct, name='product-create'),
    path('upload/', uploadImage, name='image-upload'),
    path('update/<str:pk>/', updateProduct, name='product-update'),
    path('delete/<str:pk>/', deleteProduct, name='product-delete'),

    path('<str:pk>/', getProduct, name="product"),

]