from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.FileListView.as_view(), name='file_list'),
    path('<int:pk>/', views.file_detail_view, name='file_detail'),
]