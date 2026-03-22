from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Artist,Album,Song,Playlist


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ArtistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__" 
        
        
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Playlist
        fields ='__all__'