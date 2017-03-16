import hashlib
import os
import urllib

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from django.conf import settings

from .models import Feed, User


class FeedSerializer(ModelSerializer):
    username = SerializerMethodField()
    picture = SerializerMethodField()

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

    def get_picture(self, obj):
        no_picture = 'http://trybootcamp.vitorfs.com/static/img/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' + \
                       self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' + \
                          self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                gravatar_url = 'http://www.gravatar.com/avatar/{0}?{1}'.format(
                    hashlib.md5(self.user.email.lower()).hexdigest(),
                    urllib.urlencode({'d': no_picture, 's': '256'})
                )
                return gravatar_url

        except Exception:
            return no_picture