from django.contrib import admin
from django.urls import path, re_path

from main.views import PageListView, PageDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^pages/$', PageListView.as_view(), name='api-page-list'),
    re_path(r'^pages/(?P<pk>\d+)/$', PageDetailView.as_view(), name='api-page-detail'),
]
