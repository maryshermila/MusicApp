from restapi.models import *
from django.conf import settings
import os

song = Songs(song_name="Perfect",song_artist="Ed Sheeran",song_album="Deluxe",song_genre="Love",song_url=settings.BASE_DIR+'/static/perfect.mp3')
song.save()

song = Songs(song_name="Galway Girl",song_artist="Ed Sheeran",song_album="Deluxe",song_genre="Love")
song.save()

song = Songs(song_name="Shape of View",song_artist="Ed Sheeran",song_album="Deluxe",song_genre="Love/Comedy")
song.save()

song = Songs(song_name="Halo",song_artist="Beyonce",song_album="Beyonce",song_genre="Love")
song.save()

song = Songs(song_name="Dynamite",song_artist="BTS",song_album="BTS",song_genre="Korean Pop Music")
song.save()

song = Songs(song_name="Party in the USA",song_artist="Miley Cyrus",song_album="Miley Cyrus",song_genre="Party",song_url=settings.BASE_DIR+'/static/party.mp3')
song.save()

song = Songs(song_name="IDOL",song_artist="BTS",song_album="BTS",song_genre="Korean Pop Music")
song.save()

song = Songs(song_name="Go Go",song_artist="BTS",song_album="BTS",song_genre="Korean Pop Music")
song.save()