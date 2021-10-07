from django.urls import path, re_path
from . import views

app_name = 'sanction'

urlpatterns = [
    path('', views.SanctionListView.as_view(), name='index'),
    path('<int:pk>/', views.SanctionDetailView.as_view(), name='detail'),
]