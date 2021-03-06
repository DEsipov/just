from django.db import models
from django.db.models import F
from django.urls import reverse
from django.db import transaction


class BaseModel(models.Model):
    """
    Общий класс для всех моделей.
    """
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Заголовок",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.title


class BaseContent(BaseModel):
    """
    Общий класс контента. Создастся табличка в БД, будет хранить ссылки на потомком.
    Сделать абстрактной нельзя, ибо для M2M не подойдет.
    """
    counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        default=0
    )
    # Задает порядок выдачи в API объектов, привязанных к странице. Чем больше значение,
    # тем выше будет позиция.
    weight = models.PositiveIntegerField(
        verbose_name="Вес, для сортировки",
        default=0
    )


def video_directory_path(instance, filename):
    return f'video/{instance.id}/{filename}'


class Video(BaseContent):

    class Meta:
        verbose_name = "Видео контент"
        verbose_name_plural = "Видео контент"

    video_file = models.FileField(
        upload_to=video_directory_path,
        null=True,
        blank=True,
        max_length=1024,
        verbose_name="Видеофайл",
    )

    subtitle_file = models.FileField(
        upload_to=video_directory_path,
        null=True,
        blank=True,
        max_length=1024,
        verbose_name="Файл субтитров",
    )


class Audio(BaseContent):
    class Meta:
        verbose_name = "Аудио контент"
        verbose_name_plural = "Аудио контент"

    bitrate = models.PositiveSmallIntegerField(
        verbose_name="Битрейт в количестве бит в секунду"
    )


class Text(BaseContent):
    class Meta:
        verbose_name = "Текстовый контент"
        verbose_name_plural = "Текстовый контент"

    txt = models.TextField(
        verbose_name='Текст'
    )


class Page(BaseModel):
    PAGE_SIZE = 2

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    content = models.ManyToManyField(
        'main.basecontent',
        verbose_name="Контент",
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('api-page-detail', args=[str(self.id)])

    @transaction.atomic()
    def increment_counter(self):
        """
        Инкрементируем счетчик контента страницы.
        :return:
        """
        self.content.update(counter=F('counter') + 1)
