from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.FileListView.as_view(), name='file_list'),
    path('<int:pk>/', views.FilePageListView.as_view(), name='page_list'),
    #path('<int:pk>/<int:pk>', views.file_detail_view, name='page_detail'),
]