from django.urls import path
from .views import AlbumListView, AlbumDetailView, TrackListView, TrackDetailView

urlpatterns = [
    path('album-list/', AlbumListView.as_view(), name='album-list'),
    path('album-detail/<int:pk>/',
         AlbumDetailView.as_view(),
         name='album-detail'),
    path('track-list', TrackListView.as_view(), name='track-list'),
    path('track-detail/<int:pk>/', TrackDetailView.as_view(), name='track-detail')
]
