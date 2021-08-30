"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from djangoProject.views import Home, Introduce


urlpatterns = [
    path('admin/', admin.site.urls),

    # 홈
    path('', Home.as_view(), name='home'),

    # 공지사항
    # path('notice/', ),

    # 기술소개
    path('intro/', Introduce.as_view(), name='introduce'),
    path('article/', include('article.urls')),

    # 기술사용
    # path('uploader/', include('uploader.urls')),

    # 로그인, 회원가입
    path('account/', include('account.urls')),

]
