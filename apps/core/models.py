import uuid
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CRMBaseModel(TimeStampedModel):
    tags = GenericRelation("core.TaggedItem", related_query_name="%(class)s")
    notes = GenericRelation("core.Note", related_query_name="%(class)s")
    activities = GenericRelation("core.ActivityLog", related_query_name="%(class)s")

    class Meta:
        abstract = True


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    colour = models.CharField(max_length=7, default="#6366f1")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaggedItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tagged_items")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        unique_together = ("tag", "content_type", "object_id")

    def __str__(self):
        return f"{self.tag} → {self.content_object}"


class Note(TimeStampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="notes"
    )
    body = models.TextField()
    is_pinned = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        ordering = ["-is_pinned", "-created_at"]

    def __str__(self):
        return f"Note by {self.author} on {self.content_object}"


class ActivityLog(TimeStampedModel):
    class Action(models.TextChoices):
        CREATED = "created", "Created"
        UPDATED = "updated", "Updated"
        STATUS_CHANGE = "status_change", "Status Change"
        EMAIL_SENT = "email_sent", "Email Sent"
        CALL_LOGGED = "call_logged", "Call Logged"
        NOTE_ADDED = "note_added", "Note Added"
        DOCUMENT_UPLOADED = "document_uploaded", "Document Uploaded"
        BOOKING_MADE = "booking_made", "Booking Made"
        INVOICE_SENT = "invoice_sent", "Invoice Sent"
        OTHER = "other", "Other"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="activity_logs"
    )
    action = models.CharField(max_length=30, choices=Action.choices)
    description = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.action} by {self.user} at {self.created_at}"
