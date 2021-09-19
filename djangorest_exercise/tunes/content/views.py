from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Track, Album
from .serializers import AlbumListSerializer, AlbumDetailSerializer, \
    TrackListSerializer, TrackDetailSerializer


# Create your views here.
class TrackListView(ListCreateAPIView):
    queryset = Track.objects.all().order_by('album', 'id')
    serializer_class = TrackListSerializer


class TrackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all().order_by('album', 'id')
    serializer_class = TrackDetailSerializer


class AlbumListView(ListCreateAPIView):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumListSerializer


class AlbumDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumDetailSerializer
