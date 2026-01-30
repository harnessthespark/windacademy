from django.conf import settings
from django.db import models
from apps.core.models import CRMBaseModel


class Course(CRMBaseModel):
    class DeliveryMethod(models.TextChoices):
        CLASSROOM = "classroom", "Classroom"
        VIRTUAL = "virtual", "Virtual"
        BLENDED = "blended", "Blended"
        ELEARNING = "elearning", "E-Learning"

    title = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    objectives = models.TextField(blank=True)
    duration_days = models.DecimalField(max_digits=4, decimal_places=1, default=1)
    max_delegates = models.PositiveIntegerField(default=12)
    min_delegates = models.PositiveIntegerField(default=1)
    delivery_method = models.CharField(
        max_length=20, choices=DeliveryMethod.choices, default=DeliveryMethod.CLASSROOM
    )
    price_per_delegate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_bespoke = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    accreditation_body = models.CharField(max_length=255, blank=True)
    accreditation_number = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.code} — {self.title}"


class CourseInstance(CRMBaseModel):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        CONFIRMED = "confirmed", "Confirmed"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="instances")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=255, blank=True)
    virtual_link = models.URLField(blank=True)
    trainer = models.ForeignKey(
        "contacts.Trainer", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="course_instances"
    )
    client = models.ForeignKey(
        "clients.Client", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="bespoke_instances",
        help_text="Set if this is a bespoke course for a specific client"
    )
    price_override = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.course.code} — {self.start_date}"


class Booking(CRMBaseModel):
    class Status(models.TextChoices):
        PROVISIONAL = "provisional", "Provisional"
        CONFIRMED = "confirmed", "Confirmed"
        ATTENDED = "attended", "Attended"
        NO_SHOW = "no_show", "No Show"
        CANCELLED = "cancelled", "Cancelled"

    course_instance = models.ForeignKey(
        CourseInstance, on_delete=models.CASCADE, related_name="bookings"
    )
    delegate = models.ForeignKey(
        "contacts.Delegate", on_delete=models.CASCADE, related_name="bookings"
    )
    booked_by_client = models.ForeignKey(
        "clients.Client", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="bookings"
    )
    booked_by_contact = models.ForeignKey(
        "contacts.ClientContact", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="bookings_made"
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROVISIONAL)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    po_number = models.CharField(max_length=100, blank=True)
    certificate_issued = models.BooleanField(default=False)
    certificate_number = models.CharField(max_length=100, blank=True)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.delegate} — {self.course_instance}"


class Module(CRMBaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["course", "order"]
        unique_together = ("course", "order")

    def __str__(self):
        return f"{self.course.code} — Module {self.order}: {self.title}"


class Lesson(CRMBaseModel):
    class LessonType(models.TextChoices):
        THEORY = "theory", "Theory"
        PRACTICAL = "practical", "Practical"
        DISCUSSION = "discussion", "Discussion"
        ACTIVITY = "activity", "Activity"

    class DeliveryMethod(models.TextChoices):
        FACE_TO_FACE = "face_to_face", "Face to Face"
        VIDEO = "video", "Video"
        VR = "vr", "VR"
        ELEARNING = "elearning", "E-Learning"
        WEBINAR = "webinar", "Webinar"
        BLENDED = "blended", "Blended"

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=30)
    lesson_type = models.CharField(
        max_length=20, choices=LessonType.choices, default=LessonType.THEORY
    )
    delivery_method = models.CharField(
        max_length=20, choices=DeliveryMethod.choices, default=DeliveryMethod.FACE_TO_FACE
    )
    materials = models.FileField(upload_to="training/lesson_materials/", blank=True)

    class Meta:
        ordering = ["module", "order"]
        unique_together = ("module", "order")

    def __str__(self):
        return f"{self.module.title} — Lesson {self.order}: {self.title}"


class Assessment(CRMBaseModel):
    class AssessmentType(models.TextChoices):
        QUIZ = "quiz", "Quiz"
        PRACTICAL = "practical", "Practical"
        WRITTEN = "written", "Written"
        OBSERVATION = "observation", "Observation"

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assessments")
    title = models.CharField(max_length=255)
    assessment_type = models.CharField(
        max_length=20, choices=AssessmentType.choices, default=AssessmentType.QUIZ
    )
    description = models.TextField(blank=True)
    pass_mark = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_score = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    is_mandatory = models.BooleanField(default=True)

    class Meta:
        ordering = ["course", "title"]

    def __str__(self):
        return f"{self.course.code} — {self.title}"


class AssessmentResult(CRMBaseModel):
    assessment = models.ForeignKey(
        Assessment, on_delete=models.CASCADE, related_name="results"
    )
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="assessment_results"
    )
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    passed = models.BooleanField(default=False)
    assessed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="assessments_given"
    )
    assessed_at = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ["-assessed_at"]
        unique_together = ("assessment", "booking")

    def __str__(self):
        return f"{self.booking.delegate} — {self.assessment.title}: {'Pass' if self.passed else 'Fail'}"


class Feedback(CRMBaseModel):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="feedback")
    overall_rating = models.PositiveSmallIntegerField()
    trainer_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    content_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    venue_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    comments = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name_plural = "feedback"

    def __str__(self):
        return f"Feedback for {self.booking} — {self.overall_rating}/5"
