from rest_framework import serializers
from .models import Job, Candidate, Interview, Placement


class JobListSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.name", read_only=True)

    class Meta:
        model = Job
        fields = (
            "id", "title", "reference", "client", "client_name",
            "status", "job_type", "location", "created_at",
        )


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class CandidateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            "id", "job", "first_name", "last_name", "email",
            "stage", "rating", "created_at",
        )


class CandidateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class InterviewListSerializer(serializers.ModelSerializer):
    candidate_name = serializers.SerializerMethodField()
    job_title = serializers.CharField(source="job.title", read_only=True)
    interviewer_name = serializers.CharField(
        source="interviewer.get_full_name", read_only=True, default=""
    )

    class Meta:
        model = Interview
        fields = (
            "id", "candidate", "candidate_name", "job", "job_title",
            "interview_type", "status", "scheduled_at", "duration_minutes",
            "interviewer", "interviewer_name", "rating", "created_at",
        )

    def get_candidate_name(self, obj):
        return f"{obj.candidate.first_name} {obj.candidate.last_name}"


class InterviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class PlacementListSerializer(serializers.ModelSerializer):
    candidate_name = serializers.SerializerMethodField()

    class Meta:
        model = Placement
        fields = (
            "id", "job", "candidate", "candidate_name",
            "status", "start_date", "day_rate", "client_fee_percentage",
            "resourcer_commission", "fee_amount", "created_at",
        )

    def get_candidate_name(self, obj):
        return str(obj.candidate)


class PlacementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
