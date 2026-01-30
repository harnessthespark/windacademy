from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Employee, DayRate, LeaveRequest, Timesheet
from .serializers import (
    EmployeeListSerializer, EmployeeDetailSerializer,
    DayRateListSerializer, DayRateDetailSerializer,
    LeaveRequestListSerializer, LeaveRequestDetailSerializer,
    TimesheetListSerializer, TimesheetDetailSerializer,
)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related("user").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "department"]
    search_fields = ["first_name", "last_name", "email", "department", "role"]
    ordering_fields = ["last_name", "first_name", "start_date", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return EmployeeListSerializer
        return EmployeeDetailSerializer


class DayRateViewSet(viewsets.ModelViewSet):
    queryset = DayRate.objects.select_related("employee").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["employee"]
    search_fields = ["employee__first_name", "employee__last_name", "role"]
    ordering_fields = ["effective_from", "day_rate", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return DayRateListSerializer
        return DayRateDetailSerializer


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.select_related("employee", "approved_by").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["employee", "status", "leave_type"]
    search_fields = ["employee__first_name", "employee__last_name", "reason"]
    ordering_fields = ["start_date", "status", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return LeaveRequestListSerializer
        return LeaveRequestDetailSerializer


class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.select_related("employee", "approved_by").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["employee", "status"]
    search_fields = ["employee__first_name", "employee__last_name"]
    ordering_fields = ["week_starting", "status", "created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return TimesheetListSerializer
        return TimesheetDetailSerializer
