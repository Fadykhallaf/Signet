from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Question, Answer, Tag


class AnswerSerializer(ModelSerializer):
    username = SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            'user',
            'username',
            'question',
            'description',
            'create_date',
            'update_date',
            'votes',
            'is_accepted'
        ]

    def get_username(self, obj):
        return str(obj.user.username)


class QuestionSerializer(ModelSerializer):
    username = SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'id',
            'user',
            'username',
            'title',
            'description',
            'create_date',
            'update_date',
            'favorites',
            'has_accepted_answer'
        ]

    def get_username(self, obj):
        return str(obj.user.username)