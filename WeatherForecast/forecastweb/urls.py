from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('forecast/', views.forecast, name='forecast'),
]