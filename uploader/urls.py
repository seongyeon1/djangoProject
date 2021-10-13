from django.urls import path
from .views import *

app_name = 'uploader'

urlpatterns = [
    # path('', HomeView.as_view(), name='uploader'),
    # path('process_image/', process_image, name='process_image'),
    path('', uploadfile, name='uploader'),
]