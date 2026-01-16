from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('<int:user_id>/', views.test_view, name="test_view"),
    path('login/', views.LoginView, name='LoginView'),
    path('logout/', views.LogoutView, name='LogoutView'),
    path('register/', views.UserRegistration, name='UserRegistration'),

]
