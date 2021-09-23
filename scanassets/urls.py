from django.urls import path
from . import views

urlpatterns = [
    path('scanassets/', views.scanassets, name="scanasets"),
    path('scanasset/<str:pk>', views.scanasset, name="scanaset"),
]