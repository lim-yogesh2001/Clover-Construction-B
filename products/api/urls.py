from django.urls import path
from . import views

urlpatterns = [
    path('products-list/<int:store_id>/<int:category_id>', views.products_api, name='products-api'),
    path('products-detail/<int:product_id>', views.product_detail_api, name = 'product-detail-api')
]
