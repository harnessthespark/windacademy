from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Campaign, CampaignRecipient, Newsletter
from .serializers import (
    CampaignListSerializer, CampaignDetailSerializer,
    CampaignRecipientListSerializer, CampaignRecipientDetailSerializer,
    NewsletterListSerializer, NewsletterDetailSerializer,
)


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.select_related("owner").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["campaign_type", "status", "owner"]
    search_fields = ["name"]
    ordering_fields = ["created_at", "start_date", "name"]

    def get_serializer_class(self):
        if self.action == "list":
            return CampaignListSerializer
        return CampaignDetailSerializer


class CampaignRecipientViewSet(viewsets.ModelViewSet):
    queryset = CampaignRecipient.objects.select_related("campaign", "delegate", "client_contact").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["campaign", "bounced", "unsubscribed"]
    search_fields = ["email"]
    ordering_fields = ["sent_at", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return CampaignRecipientListSerializer
        return CampaignRecipientDetailSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.select_related("campaign").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "campaign"]
    search_fields = ["title", "subject_line"]
    ordering_fields = ["created_at", "scheduled_send_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return NewsletterListSerializer
        return NewsletterDetailSerializer
