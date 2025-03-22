from rest_framework import serializers
from .models import Announcements

class AnnouncementSerializer(serializers.ModelSerializer):
    tags =serializers.JSONField()
    class Meta:
        model = Announcements
        fields = '__all__'