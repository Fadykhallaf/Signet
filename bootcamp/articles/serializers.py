from .models import Article, ArticleComment
from rest_framework.serializers import ModelSerializer, URLField, RelatedField, SerializerMethodField


class ArticleSerializer(ModelSerializer):
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