from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Songs)
admin.site.register(Playlists)
admin.site.register(PlaylistSongsMapping)
admin.site.register(SongRating)
admin.site.register(Recommendations)