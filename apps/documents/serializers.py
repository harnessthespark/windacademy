from rest_framework import serializers
from .models import Document, Invoice, InvoiceLineItem


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("id", "title", "doc_type", "file", "uploaded_by", "visible_to_client", "created_at")


class DocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class InvoiceLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLineItem
        fields = ("id", "description", "quantity", "unit_price", "line_total")


class InvoiceListSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.name", read_only=True)

    class Meta:
        model = Invoice
        fields = (
            "id", "invoice_number", "client", "client_name",
            "status", "issue_date", "due_date", "total",
        )


class InvoiceDetailSerializer(serializers.ModelSerializer):
    line_items = InvoiceLineItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
