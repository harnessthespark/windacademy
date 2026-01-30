from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, CourseInstanceViewSet, BookingViewSet,
    ModuleViewSet, LessonViewSet, AssessmentViewSet,
    AssessmentResultViewSet, FeedbackViewSet,
)

router = DefaultRouter()
router.register("courses", CourseViewSet, basename="course")
router.register("instances", CourseInstanceViewSet, basename="courseinstance")
router.register("bookings", BookingViewSet, basename="booking")
router.register("modules", ModuleViewSet, basename="module")
router.register("lessons", LessonViewSet, basename="lesson")
router.register("assessments", AssessmentViewSet, basename="assessment")
router.register("assessment-results", AssessmentResultViewSet, basename="assessmentresult")
router.register("feedback", FeedbackViewSet, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
]
