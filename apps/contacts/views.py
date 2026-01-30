from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Delegate, Trainer, ClientContact
from .serializers import (
    DelegateListSerializer, DelegateDetailSerializer,
    TrainerListSerializer, TrainerDetailSerializer,
    ClientContactListSerializer, ClientContactDetailSerializer,
)


class DelegateViewSet(viewsets.ModelViewSet):
    queryset = Delegate.objects.select_related("employer").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["employer", "is_candidate", "source", "gdpr_consent", "marketing_opt_in"]
    search_fields = ["first_name", "last_name", "email", "company_name"]
    ordering_fields = ["last_name", "created_at", "email"]

    def get_serializer_class(self):
        if self.action == "list":
            return DelegateListSerializer
        return DelegateDetailSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["trainer_type"]
    search_fields = ["first_name", "last_name", "email", "specialisms"]
    ordering_fields = ["last_name", "day_rate", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return TrainerListSerializer
        return TrainerDetailSerializer


class ClientContactViewSet(viewsets.ModelViewSet):
    queryset = ClientContact.objects.select_related("client").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["client", "is_primary", "is_billing", "is_booking"]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["last_name", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ClientContactListSerializer
        return ClientContactDetailSerializer
