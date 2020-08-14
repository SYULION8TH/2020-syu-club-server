from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from club.views import clubViews
from club.views import intClubViews

urlpatterns = [
    path('clubs/', clubViews.ClubsList.as_view()),
    path('clubs/<int:pk>',clubViews.ClubDetail.as_view()),
    path('int-clubs', intClubViews.interestClubList.as_view()),
    path('int-clubs/<int:pk>', intClubViews.interestClubDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
