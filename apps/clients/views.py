from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Client
from .serializers import ClientListSerializer, ClientDetailSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.select_related("account_manager").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "client_type", "account_manager", "portal_enabled"]
    search_fields = ["name", "trading_name", "industry", "city"]
    ordering_fields = ["name", "created_at", "lifetime_value", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return ClientListSerializer
        return ClientDetailSerializer
