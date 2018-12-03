#!-*-coding:utf-8-*-
from rest_framework import serializers

from .models import Page, Text, Video, Audio


class PageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('url', 'title')

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(location=obj.get_absolute_url())


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class PageDetailSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('title', 'content')

    @staticmethod
    def get_content_data(content):
        """
        Возвращает данные, в зависимости от типа контента
        :param content: BaseContent
        :return: dict
        """
        if hasattr(content, 'video'):
            return VideoSerializer(content.video).data
        if hasattr(content, 'audio'):
            return AudioSerializer(content.audio).data
        if hasattr(content, 'text'):
            return TextSerializer(content.text).data

    def get_content(self, obj):
        return [self.get_content_data(content) for content in obj.content.all().order_by('-weight')]
