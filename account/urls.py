from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # предыдущий url для авторизации
    # path('login/', views.user_login, name='login'),
    # url-адреса для входа и выхода из учётной записи
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]