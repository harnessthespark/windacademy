from django.contrib import admin
from .models import Tag, TaggedItem, Note, ActivityLog


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "colour")
    search_fields = ("name",)


@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ("tag", "content_type", "object_id")
    list_filter = ("content_type",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("author", "is_pinned", "content_type", "created_at")
    list_filter = ("is_pinned", "content_type")
    search_fields = ("body",)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "content_type", "created_at")
    list_filter = ("action", "content_type")
    search_fields = ("description",)
    readonly_fields = ("created_at",)
