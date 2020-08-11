"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic import TemplateView
# media file 설정
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 모든 주소를 우선 client 쪽으로 연결시킴
    url(r'^$', TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/', admin.site.urls),
    # 소셜 로그인 관련 url
    path("accounts/" , include('allauth.urls'))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

