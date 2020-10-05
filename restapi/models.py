from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Songs(models.Model):
    song_name = models.TextField()
    song_artist = models.TextField()
    song_album = models.CharField(max_length=100)
    song_genre = models.CharField(max_length=100)
    song_rating = models.TextField(blank=True,null=True)
    song_url = models.TextField(blank=True,null=True,default="None")

class Playlists(models.Model):
    class Meta:
        unique_together = (('playlist_name', 'user'),)
    playlist_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

class PlaylistSongsMapping(models.Model):
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs,on_delete=models.CASCADE)

class SongRating(models.Model):
    song = models.ForeignKey(Songs,on_delete=models.CASCADE)
    five_stars = models.IntegerField(blank=True,null=True,default=0)
    four_stars = models.IntegerField(blank=True,null=True,default=0)
    three_stars = models.IntegerField(blank=True,null=True,default=0)
    two_stars = models.IntegerField(blank=True,null=True,default=0)
    one_star = models.IntegerField(blank=True,null=True,default=0)

class Recommendations(models.Model):
    song = models.ForeignKey(Songs,on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, blank=True,null=True,related_name='shared_by',on_delete=models.CASCADE)
    shared_to = models.ForeignKey(User, blank=True,null=True,related_name='shared_to', on_delete=models.CASCADE)
   