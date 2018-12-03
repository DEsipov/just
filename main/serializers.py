#!-*-coding:utf-8-*-
from rest_framework import serializers

from .models import Page


class PageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('url', 'title', )

    def get_url(self, obj):
        return obj.get_absolute_url()


class PageDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('title', )
