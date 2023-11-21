from app1.views import *
from django.urls import path

app_name = "home"

urlpatterns = [
    path('team/',team,name='team'),
]