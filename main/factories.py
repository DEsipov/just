#!-*-coding:utf-8-*-
import factory.fuzzy

from . import models


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Page

    title = factory.Sequence(lambda x: f"Page_{x}")


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Video

    title = factory.Sequence(lambda x: f"Video_{x}")


class AudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Audio

    title = factory.Sequence(lambda x: f"Audio_{x}")
    bitrate = factory.fuzzy.FuzzyInteger(1, 512)


class TextFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Text

    title = factory.Sequence(lambda x: f"Text_{x}")
    txt = factory.fuzzy.FuzzyText()
