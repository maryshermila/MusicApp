from django.contrib import admin
from django.urls import path,include
from restapi.views import *

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register',Register.as_view(), name='register'),
    path('listsongs',ListSongs.as_view(), name = 'listsongs'),
    path('playlist',PlayLists.as_view(), name = 'playlist'),
    path('rating',UserRating.as_view(), name = 'rating'),
    path('groupsongs',GroupSongs.as_view(), name = 'groupsongs'),
    path('suggest',AutoSuggestSongs.as_view(), name = 'suggest'),
    path('usersongrecommendations',UserRecommendedSongs.as_view(), name ='usersongrecommendations')
]