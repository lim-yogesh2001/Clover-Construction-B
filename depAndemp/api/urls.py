from django.urls import path
from . import views

urlpatterns = [
    path('department-list/',views.department_list_api, name = "department-list-api"),
    path('worker-list/<int:dep_id>/', views.worker_list_api, name = "worker-list-api"),
    path('worker-details/<int:worker_id>/', views.woker_details_api, name = "worker-detail-api")
]
