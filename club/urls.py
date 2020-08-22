from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from club.views import clubViews
from club.views import intClubViews


urlpatterns = [
    path('clubs/', clubViews.ClubsList.as_view()),
    path('clubs/<int:pk>',clubViews.ClubDetail.as_view()),
<<<<<<< HEAD
    path('int-clubs', intClubViews.InterestClub.as_view()),   
=======
    path('int-clubs', intClubViews.InterestClubList.as_view()),
>>>>>>> b5ec6d280798e50402d02d297a878ed4501df620
    path('int-clubs/<int:pk>', intClubViews.InterestClubDetail.as_view()),
    path('clubs/famous', clubViews.FamousClubList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
