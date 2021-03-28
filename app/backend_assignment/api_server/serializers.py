from rest_framework import serializers
from .models import Video

# serializers.HyperlinkedModelSerializer
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('published_at', 'channel_id', 'title', 'description', 'channel_title', 'video_id', )
