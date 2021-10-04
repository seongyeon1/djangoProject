from django.urls import path
from .views import *

app_name = 'uploader'

urlpatterns = [
    path('', uploadfile, name='uploader'),
]