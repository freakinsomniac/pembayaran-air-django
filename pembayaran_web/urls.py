from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_pelanggan, name='input_pelanggan'),
]