from django.contrib import admin
from django.urls import path, re_path

from main.views import PageListView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^pages/$', PageListView.as_view(), name='api-page-list'),
]
