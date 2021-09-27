from django.urls import path
from . import views

urlpatterns = [
    path('', views.scanassets, name="scanasets"),
    path('scanasset/<str:pk>', views.scanasset, name="scanasset"),
]