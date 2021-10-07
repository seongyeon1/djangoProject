from django.urls import path, re_path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.NoticeList.as_view(), name='index'),
    path('<int:pk>/', views.NoticeDetail.as_view(), name='detail'),
]