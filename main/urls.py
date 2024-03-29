from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="Homepage"),
    path("search", views.search, name="Search"),
    path("track/<str:id>", views.track, name="Track"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile', views.home, name='Homepage'),
    path('logout/', LogoutView.as_view(), name='logout'),



]
