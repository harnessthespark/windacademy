from django.contrib import admin
from .models import Delegate, Trainer, ClientContact


@admin.register(Delegate)
class DelegateAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "employer", "is_candidate", "created_at")
    list_filter = ("is_candidate", "gdpr_consent", "marketing_opt_in")
    search_fields = ("first_name", "last_name", "email", "company_name")
    raw_id_fields = ("employer", "user")


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "trainer_type", "day_rate")
    list_filter = ("trainer_type",)
    search_fields = ("first_name", "last_name", "email", "specialisms")
    filter_horizontal = ("approved_courses",)
    raw_id_fields = ("user",)


@admin.register(ClientContact)
class ClientContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "client", "is_primary", "is_billing")
    list_filter = ("is_primary", "is_billing", "is_booking")
    search_fields = ("first_name", "last_name", "email")
    raw_id_fields = ("client", "user")
