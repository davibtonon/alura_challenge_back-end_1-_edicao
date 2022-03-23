import imp
from django.shortcuts import render
from videos_api.models import Video
from videos_api.serializers import VideoSerializers
from rest_framework import viewsets
# Create your views here.

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers