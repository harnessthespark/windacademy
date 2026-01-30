from rest_framework import serializers
from .models import Campaign, CampaignRecipient, Newsletter


class CampaignListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = (
            "id", "name", "campaign_type", "status",
            "start_date", "end_date", "total_sent", "total_opened", "total_clicked",
        )


class CampaignDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class CampaignRecipientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignRecipient
        fields = ("id", "campaign", "email", "sent_at", "opened_at", "clicked_at", "bounced", "unsubscribed")


class CampaignRecipientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignRecipient
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class NewsletterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ("id", "title", "subject_line", "status", "scheduled_send_at", "sent_at", "total_sent")


class NewsletterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
