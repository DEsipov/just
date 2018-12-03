from django.contrib import admin

from main.models import Page, Video, Audio, Text


class BaseAdmin(admin.ModelAdmin):
    search_fields = ['title__startswith']


class ContentInline(admin.TabularInline):
    model = Page.content.through
    extra = 1


@admin.register(Page)
class PageAdmin(BaseAdmin):
    search_fields = ['title__startswith']
    inlines = [
        ContentInline,
    ]
    exclude = ('content',)
    model = Page


@admin.register(Video)
class PageAdmin(BaseAdmin):
    pass


@admin.register(Audio)
class PageAdmin(BaseAdmin):
    pass


@admin.register(Text)
class PageAdmin(BaseAdmin):
    pass
