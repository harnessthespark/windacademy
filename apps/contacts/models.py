from django.conf import settings
from django.db import models
from apps.core.models import CRMBaseModel


class Person(CRMBaseModel):
    class Title(models.TextChoices):
        MR = "Mr", "Mr"
        MRS = "Mrs", "Mrs"
        MS = "Ms", "Ms"
        MISS = "Miss", "Miss"
        DR = "Dr", "Dr"
        PROF = "Prof", "Prof"

    title = models.CharField(max_length=10, choices=Title.choices, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=150, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, default="United Kingdom")
    linkedin_url = models.URLField(blank=True)
    gdpr_consent = models.BooleanField(default=False)
    gdpr_consent_date = models.DateTimeField(null=True, blank=True)
    marketing_opt_in = models.BooleanField(default=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        abstract = True
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Delegate(Person):
    source = models.CharField(max_length=100, blank=True)
    employer = models.ForeignKey(
        "clients.Client", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="delegates"
    )
    dietary_requirements = models.TextField(blank=True)
    accessibility_needs = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=255, blank=True)
    emergency_contact_phone = models.CharField(max_length=30, blank=True)
    is_candidate = models.BooleanField(default=False)
    cv = models.FileField(upload_to="cvs/delegates/", blank=True)

    class Meta(Person.Meta):
        verbose_name = "Delegate"
        verbose_name_plural = "Delegates"


class Trainer(Person):
    class TrainerType(models.TextChoices):
        INTERNAL = "internal", "Internal"
        EXTERNAL = "external", "External"
        ASSOCIATE = "associate", "Associate"

    trainer_type = models.CharField(max_length=20, choices=TrainerType.choices)
    day_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    specialisms = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/trainers/", blank=True)
    approved_courses = models.ManyToManyField(
        "training.Course", blank=True, related_name="approved_trainers"
    )
    dbs_expiry_date = models.DateField(null=True, blank=True)
    insurance_expiry_date = models.DateField(null=True, blank=True)

    class Meta(Person.Meta):
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"


class ClientContact(Person):
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="contacts"
    )
    is_primary = models.BooleanField(default=False)
    is_billing = models.BooleanField(default=False)
    is_booking = models.BooleanField(default=False)
    department = models.CharField(max_length=150, blank=True)

    class Meta(Person.Meta):
        verbose_name = "Client Contact"
        verbose_name_plural = "Client Contacts"
