from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from apps.core.models import CRMBaseModel


class Document(CRMBaseModel):
    class DocType(models.TextChoices):
        CONTRACT = "contract", "Contract"
        PROPOSAL = "proposal", "Proposal"
        CERTIFICATE = "certificate", "Certificate"
        CV = "cv", "CV"
        INVOICE = "invoice", "Invoice"
        REPORT = "report", "Report"
        OTHER = "other", "Other"

    title = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=20, choices=DocType.choices, default=DocType.OTHER)
    file = models.FileField(upload_to="documents/")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="uploaded_documents"
    )
    visible_to_client = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.UUIDField(null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Invoice(CRMBaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SENT = "sent", "Sent"
        VIEWED = "viewed", "Viewed"
        PAID = "paid", "Paid"
        OVERDUE = "overdue", "Overdue"
        CANCELLED = "cancelled", "Cancelled"

    invoice_number = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="invoices"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    issue_date = models.DateField()
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    vat_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    po_number = models.CharField(max_length=100, blank=True)
    booking = models.ForeignKey(
        "training.Booking", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="invoices"
    )
    placement = models.ForeignKey(
        "recruitment.Placement", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="invoices"
    )
    pdf = models.FileField(upload_to="invoices/", blank=True)

    class Meta:
        ordering = ["-issue_date"]

    def __str__(self):
        return f"{self.invoice_number} — {self.client.name}"


class InvoiceLineItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="line_items")
    description = models.CharField(max_length=500)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    line_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.description} (x{self.quantity})"
