from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from .models import *
from .serlializers import *

# Create your views here.

class Login(APIView):
    def post(self,request,format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)
            user = authenticate(username = data['username'], password = data['password'])
            print(user.id)
            if user:
                return Response("Authentication Successful",status=status.HTTP_200_OK)
            else:
                return Response("User does not exist",status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class Register(APIView):
    def post(self,request,format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)
            new_user = User(username = data["username"],first_name= data['firstname'],last_name=data['lastname'],email=data['email'])
            new_user.set_password(data['password'])
            new_user.save()
            return Response("User created Successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class ListSongs(APIView):
    def get(self, request, format=None):
        try:
            songs = Songs.objects.all()
            songs_list= SongsSerializers(songs,many=True)
            return Response(songs_list.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class PlayLists(APIView):
    def post(self, request, format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)
            new_playlist = Playlists(playlist_name=data["playlist_name"],user_id=data["user_id"])
            new_playlist.save()
            for every_song in data["song_IDs"]:
                playlist_songs = PlaylistSongsMapping(playlist_id=new_playlist.id,song_id=every_song)
                playlist_songs.save()
            return Response("Playlist created Successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)
            user_playlist_info = []
            list_playlist = Playlists.objects.filter(user_id = data["user_id"])
            if list_playlist.count() > 0:
                for every_playlist in list_playlist:
                    playlist_info = {}
                    playlist_info["playlist_name"] = every_playlist.playlist_name
                    playlist_info["songs"] = []
                    songs = PlaylistSongsMapping.objects.filter(playlist_id=every_playlist.id)
                    if songs.count() > 0:
                        for every_song in songs:
                            song_detail = Songs.objects.get(id=every_song.song_id)
                            serilaized_song = SongsSerializers(song_detail)
                            playlist_info["songs"].append(serilaized_song.data)
                    user_playlist_info.append(playlist_info)
            return Response(user_playlist_info,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)
            playlist_details = Playlists.objects.get(user_id=data["user_id"],playlist_name=data["playlist_name"])
            
            if data["action"] == "add":
                if PlaylistSongsMapping.objects.filter(playlist_id=playlist_details.id,song_id=data["song_id"]).exists():
                    return Response("Song already Exists in the playlist",status=status.HTTP_200_OK)
                else:
                    playlist_songs = PlaylistSongsMapping(playlist_id=playlist_details.id,song_id=data["song_id"])
                    playlist_songs.save()
                    return Response("Song Added Successfully",status=status.HTTP_200_OK)
            
            elif data["action"] == "remove":
                if PlaylistSongsMapping.objects.filter(playlist_id=playlist_details.id,song_id=data["song_id"]).exists():
                    PlaylistSongsMapping.objects.filter(playlist_id=playlist_details.id,song_id=data["song_id"]).delete()
                    return Response("Song Removed Successfully",status=status.HTTP_200_OK)
                else:
                    return Response("Given Song doesn't exist in the playlist",status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class UserRating(APIView):
    def post(self,request,format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)

            if data["star"] == 5:
                if SongRating.objects.filter(song_id=data["song_id"]).exists():
                    existing_ratings = SongRating.objects.get(song_id=data["song_id"])
                    existing_ratings.five_stars = int(existing_ratings.five_stars)+ 1
                    existing_ratings.save()
                else:
                    new_rating = SongRating(song_id=data["song_id"],five_stars=1)
                    new_rating.save()
            
            elif data["star"] == 4:
                if SongRating.objects.filter(song_id=data["song_id"]).exists():
                    existing_ratings = SongRating.objects.get(song_id=data["song_id"])
                    existing_ratings.four_stars = int(existing_ratings.four_stars)+ 1
                    existing_ratings.save()
                else:
                    new_rating = SongRating(song_id=data["song_id"],four_stars=1)
                    new_rating.save()

            elif data["star"] == 3:
                if SongRating.objects.filter(song_id=data["song_id"]).exists():
                    existing_ratings = SongRating.objects.get(song_id=data["song_id"])
                    existing_ratings.three_stars = int(existing_ratings.three_stars)+ 1
                    existing_ratings.save()
                else:
                    new_rating = SongRating(song_id=data["song_id"],three_stars=1)
                    new_rating.save()

            elif data["star"] == 2:
                if SongRating.objects.filter(song_id=data["song_id"]).exists():
                    existing_ratings = SongRating.objects.get(song_id=data["song_id"])
                    existing_ratings.two_stars = int(existing_ratings.two_stars)+ 1
                    existing_ratings.save()
                else:
                    new_rating = SongRating(song_id=data["song_id"],two_stars=1)
                    new_rating.save()

            elif data["star"] == 1:
                if SongRating.objects.filter(song_id=data["song_id"]).exists():
                    existing_ratings = SongRating.objects.get(song_id=data["song_id"])
                    existing_ratings.one_star = int(existing_ratings.one_star)+ 1
                    existing_ratings.save()
                else:
                    new_rating = SongRating(song_id=data["song_id"],one_star=1)
                    new_rating.save()

            updated_ratings = SongRating.objects.get(song_id=data["song_id"])
            numerator = (5*int(updated_ratings.five_stars))+(4*int(updated_ratings.four_stars))+(3*int(updated_ratings.three_stars))+(2*int(updated_ratings.two_stars))+(1*int(updated_ratings.one_star))
            denominator = (int(updated_ratings.five_stars)+int(updated_ratings.four_stars)+int(updated_ratings.three_stars)+int(updated_ratings.two_stars)+int(updated_ratings.one_star))
            song = Songs.objects.get(id=data["song_id"])
            song.song_rating = numerator / denominator
            song.save()

            return Response("Rating for the song added Successfully",status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class GroupSongs(APIView):
    def get(self,request,format=None):
        try:
            songs_groupedby = {}
            distinct_list = Songs.objects.values_list('song_genre', flat=True).distinct()
            for value in distinct_list:
                songs_groupedby[value] = []
                songs = Songs.objects.filter(song_genre=value)
                for every_song in songs:
                    serilaized_song = SongsSerializers(every_song)
                    songs_groupedby[value].append(serilaized_song.data)
            return Response(songs_groupedby,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class AutoSuggestSongs(APIView):
    def get(self,request,format=None):
        try:
            user_genre = {}
            all_genre = {}
            recommend_genre = {}
            user_id = self.request.query_params.get("user_id")

            distinct_list = Songs.objects.values_list('song_genre', flat=True).distinct()
            for value in distinct_list:
                user_genre[value] = []
                all_genre[value] = []
                songs = Songs.objects.filter(song_genre=value)
                for every_song in songs:
                    all_genre[value].append(every_song.id)

            user_playlists = Playlists.objects.filter(user_id=user_id)
            for every_list in user_playlists:
                songs = PlaylistSongsMapping.objects.filter(playlist_id=every_list.id)
                for every_song in songs:
                    song_info = Songs.objects.get(id=every_song.song_id)
                    user_genre[song_info.song_genre].append(song_info.id)

            for key,value in user_genre.items():
                if value:
                    recommend_genre[key] = []
                    unmatches = list(set(all_genre[key])-set(user_genre[key]))
                    for every_val in unmatches:
                        song_info = Songs.objects.get(id=every_val)
                        serilaized_song = SongsSerializers(song_info)
                        recommend_genre[key].append(serilaized_song.data)
            
            return Response(recommend_genre,status=status.HTTP_200_OK)
        except Exception as e:
                return Response(
                    data={ "message": "Something went wrong",
                            "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

class UserRecommendedSongs(APIView):
    def post(self,request,format=None):
        try:
            data = request.body.decode("UTF-8")
            data = json.loads(data)
            if Recommendations.objects.filter(song_id=data["song_id"],shared_by_id=data["shared_by"],shared_to_id=data["shared_to"]).exists():
                return Response("Your have already shared the recommendation to the user",status=status.HTTP_200_OK)
            else:
                recommend = Recommendations(song_id=data["song_id"],shared_by_id=data["shared_by"],shared_to_id=data["shared_to"])
                recommend.save()
                return Response("Your recommendation is added successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,format=None):
        try:
            song_recommendations = []
            user_id = self.request.query_params.get("user_id")
            my_recommendations = Recommendations.objects.filter(shared_to_id=user_id)
            for every_recommendation in my_recommendations:
                song_info = Songs.objects.get(id=every_recommendation.song_id)
                serilaized_song = SongsSerializers(song_info)
                final_data = serilaized_song.data 
                final_data['shared_by'] = every_recommendation.shared_by_id
                song_recommendations.append(final_data)
            return Response(song_recommendations,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data={ "message": "Something went wrong",
                        "error": str(e)},status=status.HTTP_400_BAD_REQUEST)


