from restapi.models import *
from rest_framework import serializers

class SongsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id','song_name','song_artist','song_album','song_genre','song_rating','song_url')
