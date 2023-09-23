# detector/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detection/', views.detection, name='detection'),
    path('dataset/', views.dataset, name='dataset'),
    path('result/', views.result, name='result'),
]
