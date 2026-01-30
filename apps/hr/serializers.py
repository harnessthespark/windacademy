from rest_framework import serializers
from .models import Employee, DayRate, LeaveRequest, Timesheet


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id", "first_name", "last_name", "email",
            "department", "role", "status", "start_date", "created_at",
        )


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class DayRateListSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    client_day_rate = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = DayRate
        fields = (
            "id", "employee", "employee_name", "role",
            "day_rate", "client_fee_percentage", "client_day_rate",
            "resourcer_commission", "effective_from", "effective_to",
        )

    def get_employee_name(self, obj):
        return str(obj.employee)


class DayRateDetailSerializer(serializers.ModelSerializer):
    client_day_rate = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = DayRate
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class LeaveRequestListSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = LeaveRequest
        fields = (
            "id", "employee", "employee_name", "leave_type",
            "start_date", "end_date", "days", "status", "created_at",
        )

    def get_employee_name(self, obj):
        return str(obj.employee)


class LeaveRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class TimesheetListSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    total_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Timesheet
        fields = (
            "id", "employee", "employee_name", "week_starting",
            "total_hours", "day_rate", "total_value", "status",
            "submitted_at", "created_at",
        )

    def get_employee_name(self, obj):
        return str(obj.employee)


class TimesheetDetailSerializer(serializers.ModelSerializer):
    total_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Timesheet
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
