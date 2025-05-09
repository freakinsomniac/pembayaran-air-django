from django.urls import path
from . import views

urlpatterns = [
    path('', views.tambah_pelanggan, name='tambah_pelanggan'),
    path('daftar/', views.daftar_pelanggan, name='daftar_pelanggan'),
]