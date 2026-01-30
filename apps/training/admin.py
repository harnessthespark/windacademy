from django.contrib import admin
from .models import (
    Course, CourseInstance, Booking,
    Module, Lesson, Assessment, AssessmentResult, Feedback,
)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ("order", "title", "lesson_type", "delivery_method", "duration_minutes")
    ordering = ("order",)


class AssessmentInline(admin.TabularInline):
    model = Assessment
    extra = 0
    fields = ("title", "assessment_type", "pass_mark", "max_score", "is_mandatory")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "category", "delivery_method", "duration_days", "price_per_delegate")
    list_filter = ("category", "delivery_method")
    search_fields = ("title", "code", "description")
    inlines = [AssessmentInline]


@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ("course", "status", "start_date", "end_date", "venue", "trainer", "client")
    list_filter = ("status", "course")
    search_fields = ("course__title", "venue")
    raw_id_fields = ("course", "trainer", "client")
    date_hierarchy = "start_date"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("delegate", "course_instance", "status", "price", "certificate_issued", "created_at")
    list_filter = ("status", "certificate_issued")
    search_fields = ("delegate__first_name", "delegate__last_name", "po_number")
    raw_id_fields = ("course_instance", "delegate", "booked_by_client", "booked_by_contact")


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("course", "order", "title")
    list_filter = ("course",)
    search_fields = ("title", "description")
    raw_id_fields = ("course",)
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("module", "order", "title", "lesson_type", "delivery_method", "duration_minutes")
    list_filter = ("lesson_type", "delivery_method", "module__course")
    search_fields = ("title", "description")
    raw_id_fields = ("module",)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("course", "title", "assessment_type", "pass_mark", "max_score", "is_mandatory")
    list_filter = ("assessment_type", "is_mandatory", "course")
    search_fields = ("title", "description")
    raw_id_fields = ("course",)


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ("assessment", "booking", "score", "passed", "assessed_by", "assessed_at")
    list_filter = ("passed", "assessment__assessment_type")
    search_fields = ("comments",)
    raw_id_fields = ("assessment", "booking", "assessed_by")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("booking", "overall_rating", "trainer_rating", "content_rating", "venue_rating", "submitted_at")
    list_filter = ("overall_rating", "is_anonymous")
    search_fields = ("comments", "suggestions")
    raw_id_fields = ("booking",)
