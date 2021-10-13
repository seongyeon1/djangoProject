from django.urls import path, reverse
from .views import *

app_name = 'threshold'

urlpatterns = [
    #path('', setThreshold, name='threshold'),
    path('', ThresholdView.as_view(), name='threshold'),
]