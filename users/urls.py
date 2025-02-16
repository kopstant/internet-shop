from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
]
