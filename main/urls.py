from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Homepage"),
    path("search", views.search, name="Search"),
    path("track/<str:id>", views.track, name="Track")
]