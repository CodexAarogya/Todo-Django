from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.test_view, name="test_view"),
    path('login/', views.LoginView, name='LoginView'),
    path('register/', views.UserRegistration, name='UserRegistration'),

]
