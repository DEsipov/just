from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Page
from .serializers import PageSerializer


class PagePagination(PageNumberPagination):
    page_size = Page.PAGE_SIZE


class PageListView(generics.ListAPIView):
    serializer_class = PageSerializer
    pagination_class = PagePagination
    queryset = Page.objects.all().order_by('id')


class PageDetailView(generics.RetrieveAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
