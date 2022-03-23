from rest_framework import serializers
from videos_api.models import Video

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url']