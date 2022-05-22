from dataclasses import fields
from email.policy import default
from rest_framework import serializers

from vopros.models import Quetion, Tag, Answer


class QuetionSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Quetion
        fields = ("tittle", "content", "photo", "isSolved", "tag_name", "author")



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("slug", "tag_name")        

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("quetionId","author","content", "time_create")
