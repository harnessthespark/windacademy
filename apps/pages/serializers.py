from rest_framework import serializers
from .models import Page, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = (
            "id", "page", "order", "title", "section_type",
            "content", "is_visible", "css_class",
            "created_at", "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class PageListSerializer(serializers.ModelSerializer):
    section_count = serializers.IntegerField(source="sections.count", read_only=True)

    class Meta:
        model = Page
        fields = ("id", "title", "slug", "status", "is_homepage", "section_count", "updated_at")


class PageDetailSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = (
            "id", "title", "slug", "description", "status",
            "is_homepage", "sections", "created_at", "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
