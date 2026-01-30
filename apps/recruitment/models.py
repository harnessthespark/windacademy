from django.conf import settings
from django.db import models
from apps.core.models import CRMBaseModel


class Job(CRMBaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        OPEN = "open", "Open"
        INTERVIEWING = "interviewing", "Interviewing"
        OFFERED = "offered", "Offered"
        FILLED = "filled", "Filled"
        CLOSED = "closed", "Closed"

    class JobType(models.TextChoices):
        PERMANENT = "permanent", "Permanent"
        CONTRACT = "contract", "Contract"
        TEMP = "temp", "Temporary"
        TEMP_TO_PERM = "temp_to_perm", "Temp to Perm"

    title = models.CharField(max_length=255)
    reference = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(
        "clients.Client", on_delete=models.CASCADE, related_name="jobs"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.PERMANENT)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fee_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    consultant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="jobs"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.reference} — {self.title}"


class Candidate(CRMBaseModel):
    class Stage(models.TextChoices):
        SOURCED = "sourced", "Sourced"
        APPLIED = "applied", "Applied"
        SCREENING = "screening", "Screening"
        SHORTLISTED = "shortlisted", "Shortlisted"
        SUBMITTED = "submitted", "Submitted to Client"
        INTERVIEWS = "interviews", "Interviews"
        OFFER = "offer", "Offer"
        PLACED = "placed", "Placed"
        REJECTED = "rejected", "Rejected"
        WITHDRAWN = "withdrawn", "Withdrawn"

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="candidates")
    delegate = models.ForeignKey(
        "contacts.Delegate", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="candidacies"
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    stage = models.CharField(max_length=20, choices=Stage.choices, default=Stage.SOURCED)
    cv = models.FileField(upload_to="cvs/candidates/", blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.job.reference}"


class Interview(CRMBaseModel):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        CONFIRMED = "confirmed", "Confirmed"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"
        NO_SHOW = "no_show", "No Show"

    class InterviewType(models.TextChoices):
        PHONE = "phone", "Phone Screen"
        VIDEO = "video", "Video Call"
        IN_PERSON = "in_person", "In Person"
        ASSESSMENT = "assessment", "Assessment"
        PANEL = "panel", "Panel"

    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="interviews"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="interviews")
    interview_type = models.CharField(
        max_length=20, choices=InterviewType.choices, default=InterviewType.VIDEO
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    location = models.CharField(max_length=255, blank=True)
    interviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="interviews_conducted"
    )
    feedback = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-scheduled_at"]

    def __str__(self):
        return f"{self.candidate} — {self.interview_type} ({self.scheduled_at:%Y-%m-%d})"


class Placement(CRMBaseModel):
    class Status(models.TextChoices):
        PENDING_START = "pending_start", "Pending Start"
        STARTED = "started", "Started"
        PROBATION = "probation", "Probation"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="placements")
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name="placement")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING_START)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    agreed_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    day_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    client_fee_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        help_text="Client fee as a percentage"
    )
    resourcer_commission = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Resourcer commission amount"
    )
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    guarantee_period_days = models.PositiveIntegerField(default=90)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.candidate} — {self.job.reference}"
