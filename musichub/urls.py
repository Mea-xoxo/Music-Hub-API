from django.urls import path
from .views import(
    ArtistListView,ArtistDetailView,
    AlbumListView,AlbumDetailView,
    SongListView,SongDetailView,
    PlaylistListView,PlaylistDetailView,
    RegisterView,
)

urlpatterns = [
    #register url
    path('register/',RegisterView.as_view(),name = 'Register'),
    
    #Artist URLS
    path('artists/',ArtistListView.as_view(),name = 'artist-detail'),
    path('artists/<int:pk>/',ArtistDetailView.as_view(), name = 'artist-detail'),
    
    #Album urls
    path('albums/',AlbumListView.as_view(),name = 'Album-list'),
    path('albums/<int:pk>/',AlbumDetailView.as_view(),name = 'album-detail'),
    
    #Songs urls
    path('songs/',SongListView.as_view(),name = 'song-list'),
    path('songs/<int:pk>/',SongDetailView.as_view(),name = 'song-detail'),
    
    #Playlist urls
    path('Playlists/',PlaylistListView.as_view(),name = 'playlist-list'),
    path('Playlists/<int:pk>/',PlaylistDetailView.as_view(),name ='playlist-detail'),
    
]