#!-*-coding:utf-8-*-
from django.test import TestCase

from ..models import Video, Audio, Text
from ..factories import PageFactory, VideoFactory, AudioFactory, TextFactory


class ModelTestCase(TestCase):
    def test_page(self):
        page = PageFactory()
        video = VideoFactory()
        audio = AudioFactory()
        text = TextFactory()
        page.content.add(video)
        page.content.add(audio)
        page.content.add(text)
        for content in page.content.all():
            if isinstance(content, Video):
                assert content.counter == 0
            if isinstance(content, Audio):
                assert content.bitrate == audio.bitrate
            if isinstance(content, Text):
                assert content.txt == text.txt
