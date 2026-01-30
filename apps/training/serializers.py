from rest_framework import serializers
from .models import (
    Course, CourseInstance, Booking,
    Module, Lesson, Assessment, AssessmentResult, Feedback,
)


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "title", "code", "category", "delivery_method", "duration_days", "price_per_delegate")


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class CourseInstanceListSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source="course.title", read_only=True)
    course_code = serializers.CharField(source="course.code", read_only=True)

    class Meta:
        model = CourseInstance
        fields = (
            "id", "course", "course_title", "course_code", "status",
            "start_date", "end_date", "venue", "trainer", "client",
        )


class CourseInstanceDetailSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source="course.title", read_only=True)

    class Meta:
        model = CourseInstance
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class BookingListSerializer(serializers.ModelSerializer):
    delegate_name = serializers.SerializerMethodField()
    course_title = serializers.CharField(source="course_instance.course.title", read_only=True)

    class Meta:
        model = Booking
        fields = (
            "id", "course_instance", "delegate", "delegate_name",
            "course_title", "status", "price", "created_at",
        )

    def get_delegate_name(self, obj):
        return str(obj.delegate)


class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


# --- Module ---

class ModuleListSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source="course.code", read_only=True)

    class Meta:
        model = Module
        fields = ("id", "course", "course_code", "order", "title")


class ModuleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


# --- Lesson ---

class LessonListSerializer(serializers.ModelSerializer):
    module_title = serializers.CharField(source="module.title", read_only=True)

    class Meta:
        model = Lesson
        fields = ("id", "module", "module_title", "order", "title", "lesson_type", "duration_minutes")


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


# --- Assessment ---

class AssessmentListSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source="course.code", read_only=True)

    class Meta:
        model = Assessment
        fields = ("id", "course", "course_code", "title", "assessment_type", "pass_mark", "max_score", "is_mandatory")


class AssessmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


# --- AssessmentResult ---

class AssessmentResultListSerializer(serializers.ModelSerializer):
    assessment_title = serializers.CharField(source="assessment.title", read_only=True)

    class Meta:
        model = AssessmentResult
        fields = ("id", "assessment", "assessment_title", "booking", "score", "passed", "assessed_at")


class AssessmentResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


# --- Feedback ---

class FeedbackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("id", "booking", "overall_rating", "trainer_rating", "content_rating", "venue_rating", "submitted_at")


class FeedbackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at", "submitted_at")
