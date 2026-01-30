from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Page, Section
from .serializers import PageListSerializer, PageDetailSerializer, SectionSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.prefetch_related("sections").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "is_homepage"]
    search_fields = ["title", "slug", "description"]
    ordering_fields = ["title", "updated_at", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return PageListSerializer
        return PageDetailSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.select_related("page").all()
    serializer_class = SectionSerializer
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["page", "section_type", "is_visible"]
    search_fields = ["title"]
    ordering_fields = ["order", "section_type"]
