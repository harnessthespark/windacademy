from django.contrib import admin
from .models import Document, Invoice, InvoiceLineItem


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "doc_type", "uploaded_by", "visible_to_client", "created_at")
    list_filter = ("doc_type", "visible_to_client")
    search_fields = ("title",)
    raw_id_fields = ("uploaded_by",)


class InvoiceLineItemInline(admin.TabularInline):
    model = InvoiceLineItem
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "client", "status", "issue_date", "due_date", "total")
    list_filter = ("status",)
    search_fields = ("invoice_number", "client__name", "po_number")
    raw_id_fields = ("client", "booking", "placement")
    date_hierarchy = "issue_date"
    inlines = [InvoiceLineItemInline]
