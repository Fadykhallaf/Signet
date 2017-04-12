import hashlib
import os
import urllib

from rest_framework.serializers import ModelSerializer, SerializerMethodField, URLField, IntegerField
from django.conf import settings

from .models import Feed
from bootcamp.communities.models import User


class FeedSerializer(ModelSerializer):
    user = User()
    username = SerializerMethodField()
    picture = URLField(source='get_picture', read_only=True)

    class Meta:
        model = Feed
        fields = [
            'id',
            'user',
            'picture',
            'username',
            'date',
            'parent',
            'post',
            'likes',
            'comments',
        ]

    def get_username(self, obj):
        return str(obj.user.username)

    def __str__(self):
        return self.user.username


class FeedEditSerializer(ModelSerializer):
    username = SerializerMethodField()
    picture = URLField(source='get_picture', read_only=True)

    class Meta:
        model = Feed
        fields = [
            'id',
            'user',
            'picture',
            'username',
            'date',
            'parent',
            'post',
        ]

    def get_username(self, obj):
        return str(obj.user.username)

    def __str__(self):
        return self.user.username