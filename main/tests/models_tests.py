#!-*-coding:utf-8-*-
from django.test import TestCase

from ..factories import PageFactory, VideoFactory, AudioFactory, TextFactory


class ModelTestCase(TestCase):
    def setUp(self):
        self.page = PageFactory()
        self.audio = AudioFactory()
        video = VideoFactory()
        text = TextFactory()
        self.page.content.add(video, self.audio, text)

    def test_smoke(self):
        for content in self.page.content.all():
            assert content.counter == 0
            if hasattr(content, 'audio'):
                assert content.audio.bitrate == self.audio.bitrate

    def test_increment_counter(self):
        self.page.increment_counter()
        assert self.page.content.filter(counter=1).count() == 3
