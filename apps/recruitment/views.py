from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsStaffUser
from .models import Job, Candidate, Placement
from .serializers import (
    JobListSerializer, JobDetailSerializer,
    CandidateListSerializer, CandidateDetailSerializer,
    PlacementListSerializer, PlacementDetailSerializer,
)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related("client", "consultant").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["client", "status", "job_type", "consultant"]
    search_fields = ["title", "reference", "description", "location"]
    ordering_fields = ["created_at", "title", "status"]

    def get_serializer_class(self):
        if self.action == "list":
            return JobListSerializer
        return JobDetailSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.select_related("job", "delegate").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["job", "stage", "rating"]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["created_at", "stage", "rating"]

    def get_serializer_class(self):
        if self.action == "list":
            return CandidateListSerializer
        return CandidateDetailSerializer


class PlacementViewSet(viewsets.ModelViewSet):
    queryset = Placement.objects.select_related("job", "candidate").all()
    permission_classes = [IsStaffUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["job", "status"]
    search_fields = ["candidate__first_name", "candidate__last_name"]
    ordering_fields = ["created_at", "start_date", "fee_amount"]

    def get_serializer_class(self):
        if self.action == "list":
            return PlacementListSerializer
        return PlacementDetailSerializer
