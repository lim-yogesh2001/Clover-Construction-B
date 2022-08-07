from django.urls import path
from . import views

urlpatterns = [
    path('orders-list/<int:user_id>/', views.order_api, name='orders-api'),
    path('orders-detail/<int:order_id>/', views.order_detail_api, name = 'orders_detail_api'),
    path('order-transection/', views.order_transection_api, name = 'order-transection-api'),
    path('order-transection-details/<int:id>/', views.order_transection_details_api, name = "order-transection-details-api"),
    path('hire-woker/<int:user_id>/', views.hire_api, name = "hire-worker-api")
]
