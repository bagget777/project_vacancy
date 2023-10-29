from django.urls import path
from apps.index import views  
urlpatterns = [
    path("", views.index, name="index"),
    path('header', views.header,name = "header"),
    path('homepage', views.homepage,name = "homepage"),
]
