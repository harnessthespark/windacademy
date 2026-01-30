from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import (
    Course, CourseInstance, Booking,
    Module, Lesson, Assessment, AssessmentResult, Feedback,
)
from .serializers import (
    CourseListSerializer, CourseDetailSerializer,
    CourseInstanceListSerializer, CourseInstanceDetailSerializer,
    BookingListSerializer, BookingDetailSerializer,
    ModuleListSerializer, ModuleDetailSerializer,
    LessonListSerializer, LessonDetailSerializer,
    AssessmentListSerializer, AssessmentDetailSerializer,
    AssessmentResultListSerializer, AssessmentResultDetailSerializer,
    FeedbackListSerializer, FeedbackDetailSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "delivery_method"]
    search_fields = ["title", "code", "description", "accreditation_body"]
    ordering_fields = ["title", "code", "duration_days", "price_per_delegate"]

    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer
        return CourseDetailSerializer


class CourseInstanceViewSet(viewsets.ModelViewSet):
    queryset = CourseInstance.objects.select_related("course", "trainer", "client").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["course", "status", "trainer", "client"]
    search_fields = ["course__title", "course__code", "venue"]
    ordering_fields = ["start_date", "end_date", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return CourseInstanceListSerializer
        return CourseInstanceDetailSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related(
        "course_instance", "course_instance__course", "delegate", "booked_by_client"
    ).all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["course_instance", "delegate", "booked_by_client", "status", "certificate_issued"]
    search_fields = ["delegate__first_name", "delegate__last_name", "po_number"]
    ordering_fields = ["created_at", "status", "price"]

    def get_serializer_class(self):
        if self.action == "list":
            return BookingListSerializer
        return BookingDetailSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.select_related("course").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["course"]
    search_fields = ["title", "description"]
    ordering_fields = ["order", "title"]

    def get_serializer_class(self):
        if self.action == "list":
            return ModuleListSerializer
        return ModuleDetailSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related("module", "module__course").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["module", "module__course", "lesson_type"]
    search_fields = ["title", "description"]
    ordering_fields = ["order", "title", "duration_minutes"]

    def get_serializer_class(self):
        if self.action == "list":
            return LessonListSerializer
        return LessonDetailSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.select_related("course").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["course", "assessment_type", "is_mandatory"]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "assessment_type"]

    def get_serializer_class(self):
        if self.action == "list":
            return AssessmentListSerializer
        return AssessmentDetailSerializer


class AssessmentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.select_related(
        "assessment", "booking", "assessed_by"
    ).all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["assessment", "booking", "passed"]
    search_fields = ["comments"]
    ordering_fields = ["assessed_at", "score"]

    def get_serializer_class(self):
        if self.action == "list":
            return AssessmentResultListSerializer
        return AssessmentResultDetailSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.select_related("booking").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["booking", "booking__course_instance"]
    search_fields = ["comments", "suggestions"]
    ordering_fields = ["submitted_at", "overall_rating"]

    def get_serializer_class(self):
        if self.action == "list":
            return FeedbackListSerializer
        return FeedbackDetailSerializer
