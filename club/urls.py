<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from club.views import club_views

urlpatterns = [
    path('clubs/', club_views.ClubsList.as_view()),
    path('clubs/<int:pk>',club_views.ClubDetail.as_view()),
]
=======
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

]


>>>>>>> 6b91237f33761b5fa7c577c7f5f4bc58c0bb5b2e
