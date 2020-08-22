from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from club.views import clubViews, intClubViews


urlpatterns = [
    path('clubs/', clubViews.ClubsList.as_view()),
    path('clubs/<int:pk>',clubViews.ClubDetail.as_view()),
<<<<<<< HEAD
    path('int-clubs', intClubViews.InterestClub.as_view()),
  
=======
    path('int-clubs', intClubViews.InterestClub.as_view()),   
>>>>>>> 88050042fb83a64a97087b7426de0e29263564de
    path('int-clubs/<int:pk>', intClubViews.InterestClubDetail.as_view()),
    path('clubs/famous', clubViews.FamousClubList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
