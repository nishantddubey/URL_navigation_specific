from app2.views import *
from django.urls import path

app_name = "teams"

urlpatterns = [
    path('india/',india,name='india'),
    path('australia/',australia,name='australia'),
    path('SA/',SA,name='SA')
]