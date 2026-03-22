from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length = 200)
    bio = models.TextField(blank = True)
    genre = models.CharField(max_length = 100, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)


def __str__(self):
    return self.name

   
class Album(models.Model):
    artist =  models.ForeignKey(Artist,on_delete = models.CASCADE, related_name = 'albums')
    title = models.CharField(max_length = 200)
    cover_image = models.FileField(upload_to = 'albums/',blank = True, null = True)
    release_date = models.DateField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
       
def __str__(self):
    return self.title


class Song(models.Model):
    title = models.CharField(max_length = 200)
    artist = models.ForeignKey(Artist,on_delete = models.CASCADE, related_name = 'songs')
    album = models.ForeignKey(Album, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'songs')
    audio_file = models.FileField(upload_to = 'songs/')
    cover_image = models.FileField(upload_to = 'covers/',blank = True, null = True)
    genre = models.CharField(max_length = 10 ,blank = True)
    duration = models.CharField(max_length = 10, blank = True)
    plays = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return self.title    

    
class Playlist(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'playlists')
    songs = models.ManyToManyField(Song,blank = True, related_name = 'playlists' )
    created_at = models.DateTimeField(auto_now_add = True)
def __str__(self):
    return self.name
    

# Create your models here.
