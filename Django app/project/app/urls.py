from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('download-csv/', views.download_csv_data)
]