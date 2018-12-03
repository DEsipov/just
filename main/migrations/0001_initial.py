from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Счетчик просмотров')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('basecontent_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                      parent_link=True, primary_key=True, serialize=False, to='main.BaseContent')),
                ('bitrate', models.PositiveSmallIntegerField(verbose_name='Битрейт в количестве бит в секунду')),
            ],
            options={
                'verbose_name': 'Аудио контент',
                'verbose_name_plural': 'Аудио контент',
            },
            bases=('main.basecontent',),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('basecontent_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                      parent_link=True, primary_key=True, serialize=False, to='main.BaseContent')),
                ('txt', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текстовый контент',
                'verbose_name_plural': 'Текстовый контент',
            },
            bases=('main.basecontent',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('basecontent_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                      parent_link=True, primary_key=True, serialize=False, to='main.BaseContent')),
                ('video_file', models.FileField(blank=True, max_length=1024, null=True,
                                                upload_to=main.models.video_directory_path,
                                                verbose_name='Видеофайл')),
                ('subtitle_file', models.FileField(blank=True, max_length=1024, null=True,
                                                   upload_to=main.models.video_directory_path,
                                                   verbose_name='Файл субтитров')),
            ],
            options={
                'verbose_name': 'Видео контент',
                'verbose_name_plural': 'Видео контент',
            },
            bases=('main.basecontent',),
        ),
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.ManyToManyField(to='main.BaseContent', verbose_name='Контент'),
        )
    ]
