from django.db import migrations

from main.factories import PageFactory, VideoFactory, AudioFactory, TextFactory
from main.models import Page, Video, Audio, Text


def forwards(apps, schema_editor):
    page = PageFactory()
    video = VideoFactory()
    audio = AudioFactory()
    text = TextFactory()
    page.content.add(video, audio, text)
    page.save()


def backwards(apps, schema_editor):
    Page.objects.all().delete()
    Video.objects.all().delete()
    Audio.objects.all().delete()
    Text.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
