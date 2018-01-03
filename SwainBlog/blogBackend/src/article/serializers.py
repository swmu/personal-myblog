# coding=utf-8

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'type','labels', 'date', 'time', 'chief', 'image_path', 'content')