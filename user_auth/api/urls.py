from django.urls import path, include
from . import views
from knox.views import LogoutView

urlpatterns = [
    path('user-profile/<int:user_id>/', views.user_profile, name = 'user-profile-api'),
    path('user-login/', views.login_view, name = 'user-login-api'),
    path('user-register/', views.register_api_view, name = 'user-register-api'),
    path('user-logout/', LogoutView.as_view()),
    path('change-password/', views.ChangePasswordView.as_view()),
    path('password-reset/', include('django_rest_passwordreset.urls'), name='password-reset')
]
