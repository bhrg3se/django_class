from rest_framework import serializers
from restapi import models



class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Music
        fields=["title","artist","genre","pk","track_no"]

