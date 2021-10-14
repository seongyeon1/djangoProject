from django.urls import path, reverse
from . import views

app_name = 'mysite'

#url = reverse('page-detail', kwargs={'file_pk': 1, 'page_pk':1})

urlpatterns = [
    path('', views.FileListView.as_view(), name='file_list'),
    path('<str:pk>', views.FilePageListView.as_view(), name='page_list'),
    path('detail/<int:pk>', views.PageDetailView.as_view(), name='page_detail'),
]