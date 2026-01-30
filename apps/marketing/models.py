from django.conf import settings
from django.db import models
from apps.core.models import CRMBaseModel


class Campaign(CRMBaseModel):
    class CampaignType(models.TextChoices):
        EMAIL = "email", "Email"
        LINKEDIN = "linkedin", "LinkedIn"
        PHONE = "phone", "Phone"
        EVENT = "event", "Event"
        WEBINAR = "webinar", "Webinar"

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=20, choices=CampaignType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_sent = models.PositiveIntegerField(default=0)
    total_opened = models.PositiveIntegerField(default=0)
    total_clicked = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="campaigns"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class CampaignRecipient(CRMBaseModel):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="recipients")
    delegate = models.ForeignKey(
        "contacts.Delegate", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="campaign_recipients"
    )
    client_contact = models.ForeignKey(
        "contacts.ClientContact", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="campaign_recipients"
    )
    email = models.EmailField()
    sent_at = models.DateTimeField(null=True, blank=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    clicked_at = models.DateTimeField(null=True, blank=True)
    bounced = models.BooleanField(default=False)
    unsubscribed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.email} — {self.campaign.name}"


class Newsletter(CRMBaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SCHEDULED = "scheduled", "Scheduled"
        SENDING = "sending", "Sending"
        SENT = "sent", "Sent"
        CANCELLED = "cancelled", "Cancelled"

    title = models.CharField(max_length=255)
    subject_line = models.CharField(max_length=255)
    body_html = models.TextField(blank=True)
    body_text = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    campaign = models.ForeignKey(
        Campaign, on_delete=models.SET_NULL, null=True, blank=True, related_name="newsletters"
    )
    scheduled_send_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    total_sent = models.PositiveIntegerField(default=0)
    total_opened = models.PositiveIntegerField(default=0)
    total_clicked = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
