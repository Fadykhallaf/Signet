from .models import Article, ArticleComment, User
from rest_framework.serializers import ModelSerializer, URLField, RelatedField, SerializerMethodField


class ArticleSerializer(ModelSerializer):
    create_user = SerializerMethodField()
    comments = URLField(source='get_comments')

    class Meta:
        model = Article
        fields = [
            'title',
            'slug',
            'content',
            'status',
            'comments',
            'create_user',
            'create_date',
            'update_date',
            'update_user',
        ]

        def get_create_user(self, obj):
            return str(obj.user.username)

        def __str__(self):
            return self.user.username