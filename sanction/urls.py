from django.urls import path, re_path
from . import views

app_name = 'sanction'

urlpatterns = [
    path('', views.SanctionListView.as_view(), name='index'),
    # path('<str:title>/', views.NoticeDetail.as_view(), name='detail'),
]