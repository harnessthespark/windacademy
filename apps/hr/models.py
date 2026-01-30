from django.conf import settings
from django.db import models
from apps.core.models import CRMBaseModel


class Employee(CRMBaseModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        ON_LEAVE = "on_leave", "On Leave"
        PROBATION = "probation", "Probation"
        NOTICE = "notice", "Notice Period"
        LEFT = "left", "Left"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="employee_profile"
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DayRate(CRMBaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="day_rates"
    )
    role = models.CharField(max_length=150, blank=True, help_text="Role this rate applies to")
    day_rate = models.DecimalField(max_digits=10, decimal_places=2, help_text="Employee day rate")
    client_fee_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        help_text="Client fee as a percentage"
    )
    resourcer_commission = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Resourcer commission amount"
    )
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-effective_from"]

    def __str__(self):
        return f"{self.employee} — £{self.day_rate}/day"

    @property
    def client_day_rate(self):
        """Day rate plus client fee percentage."""
        fee = self.day_rate * (self.client_fee_percentage / 100)
        return self.day_rate + fee


class LeaveRequest(CRMBaseModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    class LeaveType(models.TextChoices):
        ANNUAL = "annual", "Annual Leave"
        SICK = "sick", "Sick Leave"
        COMPASSIONATE = "compassionate", "Compassionate"
        UNPAID = "unpaid", "Unpaid"
        WFH = "wfh", "Working From Home"
        OTHER = "other", "Other"

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )
    leave_type = models.CharField(max_length=20, choices=LeaveType.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.DecimalField(max_digits=5, decimal_places=1)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    reason = models.TextField(blank=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="approved_leave"
    )

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.employee} — {self.leave_type} ({self.start_date} to {self.end_date})"


class Timesheet(CRMBaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "submitted", "Submitted"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="timesheets"
    )
    week_starting = models.DateField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    day_rate = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Day rate at time of submission"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    submitted_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="approved_timesheets"
    )

    class Meta:
        ordering = ["-week_starting"]
        unique_together = [("employee", "week_starting")]

    def __str__(self):
        return f"{self.employee} — w/c {self.week_starting}"

    @property
    def total_value(self):
        """Total value based on hours and day rate (assuming 8h day)."""
        if self.day_rate and self.total_hours:
            return (self.total_hours / 8) * self.day_rate
        return 0
