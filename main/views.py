from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Page
from .serializers import PageSerializer, PageDetailSerializer


class PagePagination(PageNumberPagination):
    page_size = Page.PAGE_SIZE


class PageListView(generics.ListAPIView):
    serializer_class = PageSerializer
    pagination_class = PagePagination
    queryset = Page.objects.all().order_by('id')


class PageDetailView(generics.RetrieveAPIView):
    serializer_class = PageDetailSerializer
    queryset = Page.objects.all()
