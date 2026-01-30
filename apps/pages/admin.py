from django.contrib import admin
from .models import Page, Section


class SectionInline(admin.StackedInline):
    model = Section
    extra = 0
    fields = ("order", "title", "section_type", "content", "is_visible", "css_class")
    ordering = ("order",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "is_homepage", "updated_at")
    list_filter = ("status", "is_homepage")
    search_fields = ("title", "slug", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("page", "order", "title", "section_type", "is_visible")
    list_filter = ("section_type", "is_visible", "page")
    search_fields = ("title",)
    raw_id_fields = ("page",)
