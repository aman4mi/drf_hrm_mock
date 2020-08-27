from django.db import models


class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    class Meta:
        # app_label = 'music'
        db_table = 'music_songs'
    def __str__(self):
        return  '%s' % self.title 
    

      