from rest_framework import serializers
from .models import Job, Candidate, Placement


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


class PlacementListSerializer(serializers.ModelSerializer):
    candidate_name = serializers.SerializerMethodField()

    class Meta:
        model = Placement
        fields = (
            "id", "job", "candidate", "candidate_name",
            "status", "start_date", "fee_amount", "created_at",
        )

    def get_candidate_name(self, obj):
        return str(obj.candidate)


class PlacementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
