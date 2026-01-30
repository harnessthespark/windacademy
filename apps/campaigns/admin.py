from django.contrib import admin
from .models import Campaign, CampaignRecipient, Newsletter


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "campaign_type", "status", "start_date", "total_sent", "total_opened")
    list_filter = ("campaign_type", "status")
    search_fields = ("name",)
    raw_id_fields = ("owner",)


@admin.register(CampaignRecipient)
class CampaignRecipientAdmin(admin.ModelAdmin):
    list_display = ("email", "campaign", "sent_at", "opened_at", "bounced", "unsubscribed")
    list_filter = ("bounced", "unsubscribed")
    search_fields = ("email",)
    raw_id_fields = ("campaign", "delegate", "client_contact")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "scheduled_send_at", "sent_at", "total_sent")
    list_filter = ("status",)
    search_fields = ("title", "subject_line")
    raw_id_fields = ("campaign",)
