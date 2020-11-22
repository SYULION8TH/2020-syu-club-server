from django.contrib import admin

from django.urls import path, include, re_path
from django.views.generic import TemplateView
# media file 설정
from django.conf.urls.static import static
from django.conf import settings

from user import views
# drf_yasg를 위한 설정
from django.conf import settings
from rest_framework import routers, permissions
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="SYU_CLUBS API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sahmyook@likelion.org"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # 모든 주소를 우선 client 쪽으로 연결시킴
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('post/', TemplateView.as_view(template_name='index.html'), name='post'),
    path('post/<int:post_id>/', TemplateView.as_view(template_name='index.html'), name='post_detail'),
    path('club/', TemplateView.as_view(template_name='index.html'), name='club'),
    path('club/<int:club_id>/', TemplateView.as_view(template_name='index.html'), name='club_detail'),
    path('login/', TemplateView.as_view(template_name='index.html'), name = 'login'),
    path('profile/', TemplateView.as_view(template_name='index.html'), name = 'profile'),
    path('club/<int:club_id>/qna', TemplateView.as_view(template_name='index.html'), name = 'qna'),
    path('club/<int:club_id>/qna/<int:qna_id>', TemplateView.as_view(template_name='index.html'), name = 'qna_detail'),
    
    path('admin/', admin.site.urls),
    # 소셜 로그인 관련 url
    path("accounts/" , include('allauth.urls')),
    path("api/user/", views.InfoGenerics.as_view()),
    # qna 관련 url
    path('api/', include('qna.urls')),
    #club 관련 url
    path('api/', include('club.urls')),
    # post 관련 url
    path('api/', include('board.urls')),
    # url(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html')),
]
if (settings.DEBUG):
    # swagger url
    urlpatterns += [
       path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
       path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]



# urlpatterns +=[
#    url(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html')),

# ]
