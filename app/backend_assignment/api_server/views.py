# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, filters

from .serializers import VideoSerializer
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoAPIView(generics.ListCreateAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer