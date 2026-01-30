from django.contrib import admin
from .models import Employee, DayRate, LeaveRequest, Timesheet


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "department", "role", "status", "start_date")
    list_filter = ("status", "department")
    search_fields = ("first_name", "last_name", "email")
    raw_id_fields = ("user",)


@admin.register(DayRate)
class DayRateAdmin(admin.ModelAdmin):
    list_display = ("employee", "role", "day_rate", "client_fee_percentage", "resourcer_commission", "effective_from", "effective_to")
    list_filter = ("effective_from",)
    search_fields = ("employee__first_name", "employee__last_name", "role")
    raw_id_fields = ("employee",)


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ("employee", "leave_type", "start_date", "end_date", "days", "status")
    list_filter = ("status", "leave_type")
    search_fields = ("employee__first_name", "employee__last_name")
    raw_id_fields = ("employee", "approved_by")


@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ("employee", "week_starting", "total_hours", "day_rate", "status")
    list_filter = ("status",)
    search_fields = ("employee__first_name", "employee__last_name")
    raw_id_fields = ("employee", "approved_by")
