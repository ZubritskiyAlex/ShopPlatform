
from django.urls import path

from ..views.product_views import getProduct, getProducts, deleteProduct, createProduct, updateProduct, uploadImage, \
    createProductReview, getTopProducts, show_products_of_store

urlpatterns = [

    path('', getProducts, name="products"),

    path('create/', createProduct, name='product-create'),
    path('upload/', uploadImage, name='image-upload'),

    path('productsofstore/<int:store_id>/', show_products_of_store, name='productsofstore'),


    path('update/<str:pk>/', updateProduct, name='product-update'),
    path('delete/<str:pk>/', deleteProduct, name='product-delete'),

    path('top/', getTopProducts, name='top-products'),

    path('<str:pk>/', getProduct, name="product"),
    path('<str:pk>/reviews/', createProductReview, name="create-review"),
]
