from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DayRateViewSet, LeaveRequestViewSet, TimesheetViewSet

router = DefaultRouter()
router.register("employees", EmployeeViewSet, basename="employee")
router.register("day-rates", DayRateViewSet, basename="day-rate")
router.register("leave", LeaveRequestViewSet, basename="leave-request")
router.register("timesheets", TimesheetViewSet, basename="timesheet")

urlpatterns = [
    path("", include(router.urls)),
]
