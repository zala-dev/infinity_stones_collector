from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('infinity_stones/', views.infinity_stones_index,
         name="index")
]
