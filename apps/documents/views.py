from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Document, Invoice, InvoiceLineItem
from .serializers import (
    DocumentListSerializer, DocumentDetailSerializer,
    InvoiceListSerializer, InvoiceDetailSerializer,
    InvoiceLineItemSerializer,
)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.select_related("uploaded_by").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["doc_type", "visible_to_client", "uploaded_by"]
    search_fields = ["title"]
    ordering_fields = ["created_at", "title"]

    def get_serializer_class(self):
        if self.action == "list":
            return DocumentListSerializer
        return DocumentDetailSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related("client").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["client", "status"]
    search_fields = ["invoice_number", "client__name", "po_number"]
    ordering_fields = ["issue_date", "due_date", "total", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return InvoiceListSerializer
        return InvoiceDetailSerializer


class InvoiceLineItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLineItem.objects.select_related("invoice").all()
    permission_classes = [IsStaffUser]
    serializer_class = InvoiceLineItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["invoice"]
