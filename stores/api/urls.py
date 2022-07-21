from django.urls import path
from . import views

urlpatterns = [
    path('store-list/', views.store_list_api, name='store-list-api'),
    path('store-detail/<int:store_id>/', views.store_detail_api, name='store-detail-api'),
    path('store-recent/', views.recent_store_api, name='store-recent-api'),
    path('store-categories/<int:store_id>/', views.store_categories_api, name='store-categories-api')
]
