from django.db import migrations

from main.factories import PageFactory, VideoFactory, AudioFactory, TextFactory
from main.models import Page, Video, Audio, Text


def forwards(apps, schema_editor):
    page1 = PageFactory()
    audio = AudioFactory(weight=100)
    video = VideoFactory(weight=90)
    text = TextFactory(weight=80)
    page1.content.add(video, audio, text)

    page2 = PageFactory()
    page2.content.add(video)

    # Создаем массово страницы, для проверки работы паджинатора.
    for _ in range(10):
        PageFactory()


def backwards(apps, schema_editor):
    Video.objects.all().delete()
    Audio.objects.all().delete()
    Text.objects.all().delete()
    Page.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
