from django.urls import path
from restapi import views


urlpatterns = [
    path('all/',views.MusicList.as_view()),


    path('music/<int:music_id>/',views.MusicView.as_view()),
    path('music/',views.MusicView.as_view()),



]
