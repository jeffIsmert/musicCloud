from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
#/music/
    url(r'^$', views.index, name='index'),
#/.../
    url(r'^create_account/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    
    url(r'^create-album/$', views.create_album, name='add-album'),
    url(r'^(?P<album_id>[0-9]+)/create-song/$', views.create_song, name='add-song'),

    url(r'^(?P<album_id>[0-9]+)/delete-album/$', views.delete_album, name='delete-album'),
    url(r'^(?P<album_id>[0-9]+)/delete-song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete-song'),

    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^(?P<album_id>[0-9]+)/favorite-album/$', views.favorite_album, name='favorite-album'),

    url(r'^(?P<song_id>[0-9]+)/play-audio/$', views.play, name='play-audio'),               
]