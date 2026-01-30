from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.accounts.permissions import IsClientPortalUser
from apps.contacts.models import ClientContact
from apps.training.models import Booking, CourseInstance
from apps.training.serializers import BookingListSerializer, BookingDetailSerializer, CourseInstanceListSerializer
from apps.documents.models import Document, Invoice
from apps.documents.serializers import DocumentListSerializer, InvoiceListSerializer, InvoiceDetailSerializer
from apps.recruitment.models import Job
from apps.recruitment.serializers import JobListSerializer
from .models import Client
from .serializers import ClientDetailSerializer


class PortalMixin:
    """Mixin that filters querysets to the authenticated client's data."""

    def get_client(self):
        contact = ClientContact.objects.filter(user=self.request.user).select_related("client").first()
        if contact:
            return contact.client
        return None


class PortalProfileViewSet(PortalMixin, viewsets.GenericViewSet):
    permission_classes = [IsClientPortalUser]
    serializer_class = ClientDetailSerializer

    def list(self, request):
        client = self.get_client()
        if not client:
            return Response({"detail": "No client profile found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(client)
        return Response(serializer.data)

    @action(detail=False, methods=["patch"])
    def billing(self, request):
        client = self.get_client()
        if not client:
            return Response({"detail": "No client profile found."}, status=status.HTTP_404_NOT_FOUND)
        allowed = ["billing_email", "address_line_1", "address_line_2", "city", "county", "postcode"]
        for field in allowed:
            if field in request.data:
                setattr(client, field, request.data[field])
        client.save()
        serializer = self.get_serializer(client)
        return Response(serializer.data)


class PortalBookingViewSet(PortalMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsClientPortalUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["delegate__first_name", "delegate__last_name"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        client = self.get_client()
        if not client:
            return Booking.objects.none()
        return Booking.objects.filter(booked_by_client=client).select_related(
            "delegate", "course_instance", "course_instance__course"
        )

    def get_serializer_class(self):
        if self.action == "list":
            return BookingListSerializer
        return BookingDetailSerializer


class PortalCourseViewSet(PortalMixin, viewsets.ReadOnlyModelViewSet):
    """Available courses for booking."""
    permission_classes = [IsClientPortalUser]
    serializer_class = CourseInstanceListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["status"]
    search_fields = ["course__title", "course__code"]

    def get_queryset(self):
        return CourseInstance.objects.filter(
            status__in=["scheduled", "confirmed"]
        ).select_related("course", "trainer")


class PortalInvoiceViewSet(PortalMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsClientPortalUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["status"]
    ordering_fields = ["issue_date", "due_date", "total"]

    def get_queryset(self):
        client = self.get_client()
        if not client:
            return Invoice.objects.none()
        return Invoice.objects.filter(client=client)

    def get_serializer_class(self):
        if self.action == "list":
            return InvoiceListSerializer
        return InvoiceDetailSerializer


class PortalDocumentViewSet(PortalMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsClientPortalUser]
    serializer_class = DocumentListSerializer

    def get_queryset(self):
        client = self.get_client()
        if not client:
            return Document.objects.none()
        from django.contrib.contenttypes.models import ContentType
        ct = ContentType.objects.get_for_model(Client)
        return Document.objects.filter(
            visible_to_client=True, content_type=ct, object_id=client.pk
        )


class PortalJobViewSet(PortalMixin, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsClientPortalUser]
    serializer_class = JobListSerializer

    def get_queryset(self):
        client = self.get_client()
        if not client:
            return Job.objects.none()
        return Job.objects.filter(client=client).exclude(status="draft")
