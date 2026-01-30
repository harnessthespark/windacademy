from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, InvoiceViewSet, InvoiceLineItemViewSet

router = DefaultRouter()
router.register("documents", DocumentViewSet, basename="document")
router.register("invoices", InvoiceViewSet, basename="invoice")
router.register("line-items", InvoiceLineItemViewSet, basename="invoicelineitem")

urlpatterns = [
    path("", include(router.urls)),
]
