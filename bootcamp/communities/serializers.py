from pyx.color import color

from rest_framework.serializers import *
from .models import Community
import random

class RecursiveField(Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommunitySerializerTree(ModelSerializer):
    children = RecursiveField(many=True)
    label   = SerializerMethodField()
    amount = SerializerMethodField()
    #color  = SerializerMethodField()
    class Meta:
        model = Community
        fields = ['label','amount','description','children','pk']

    def get_amount(self , obj):

        return 500000

    def get_label(self,obj):
        return obj.name
