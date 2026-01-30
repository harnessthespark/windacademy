from django.conf import settings
from django.db import models
from apps.core.models import CRMBaseModel


class Client(CRMBaseModel):
    class Status(models.TextChoices):
        PROSPECT = "prospect", "Prospect"
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        FORMER = "former", "Former"

    class ClientType(models.TextChoices):
        TRAINING = "training", "Training"
        RECRUITMENT = "recruitment", "Recruitment"
        BOTH = "both", "Both"

    name = models.CharField(max_length=255)
    trading_name = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROSPECT)
    client_type = models.CharField(max_length=20, choices=ClientType.choices, default=ClientType.TRAINING)
    company_number = models.CharField(max_length=30, blank=True)
    vat_number = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=150, blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, default="United Kingdom")
    billing_email = models.EmailField(blank=True)
    payment_terms_days = models.PositiveIntegerField(default=30)
    account_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="managed_clients"
    )
    lifetime_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    portal_enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
