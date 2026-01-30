from django.contrib import admin
from .models import Job, Candidate, Interview, Placement


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("reference", "title", "client", "status", "job_type", "consultant", "created_at")
    list_filter = ("status", "job_type")
    search_fields = ("title", "reference", "description")
    raw_id_fields = ("client", "consultant")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "job", "stage", "rating", "created_at")
    list_filter = ("stage", "rating")
    search_fields = ("first_name", "last_name", "email")
    raw_id_fields = ("job", "delegate")


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("candidate", "job", "interview_type", "status", "scheduled_at", "interviewer", "rating")
    list_filter = ("status", "interview_type")
    search_fields = ("candidate__first_name", "candidate__last_name", "job__title", "feedback")
    raw_id_fields = ("candidate", "job", "interviewer")


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ("candidate", "job", "status", "start_date", "day_rate", "client_fee_percentage", "resourcer_commission", "fee_amount")
    list_filter = ("status",)
    raw_id_fields = ("job", "candidate")
