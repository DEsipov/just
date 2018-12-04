#!-*-coding:utf-8-*-
import json

from django.test import TestCase, Client, override_settings
from django.urls import reverse

from main.factories import PageFactory, AudioFactory, VideoFactory, TextFactory
from main.models import Page


class ModelsTestCase(TestCase):
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


class PageViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.page1 = PageFactory()
        self.audio = AudioFactory(weight=100)
        self.video = VideoFactory(weight=90)
        text = TextFactory(weight=80)
        self.page1.content.add(self.video, self.audio, text)

        self.page2 = PageFactory()
        self.page2.content.add(self.video)

    def test_get_pages(self):
        url = reverse('api-page-list')
        resp = self.client.get(url)
        assert resp.status_code == 200

        data = json.loads(resp.content)
        assert data['count'] == Page.objects.count()
        expected = [x.title for x in Page.objects.all()[:Page.PAGE_SIZE]]
        results = [x['title'] for x in data['results']]
        assert set(results) == set(expected)

    @staticmethod
    def check_item(expected, content):
        content.refresh_from_db()
        assert expected['title'] == content.title
        assert expected['counter'] == content.counter

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_get_page_detail(self):
        url1 = reverse('api-page-detail', kwargs={'pk': self.page1.pk})
        url2 = reverse('api-page-detail', kwargs={'pk': self.page2.pk})

        resp = self.client.get(url1)
        assert resp.status_code == 200
        data = json.loads(resp.content)
        assert data['title'] == self.page1.title
        self.check_item(data['content'][0], self.audio)
        self.check_item(data['content'][1], self.video)

        resp = self.client.get(url2)
        data = json.loads(resp.content)
        assert resp.status_code == 200
        self.check_item(data['content'][0], self.video)
        assert self.video.counter == 2
