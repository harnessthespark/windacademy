from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .portal_views import (
    PortalProfileViewSet,
    PortalBookingViewSet,
    PortalCourseViewSet,
    PortalInvoiceViewSet,
    PortalDocumentViewSet,
    PortalJobViewSet,
)

router = DefaultRouter()
router.register("profile", PortalProfileViewSet, basename="portal-profile")
router.register("bookings", PortalBookingViewSet, basename="portal-booking")
router.register("courses", PortalCourseViewSet, basename="portal-course")
router.register("invoices", PortalInvoiceViewSet, basename="portal-invoice")
router.register("documents", PortalDocumentViewSet, basename="portal-document")
router.register("jobs", PortalJobViewSet, basename="portal-job")

urlpatterns = [
    path("", include(router.urls)),
]
