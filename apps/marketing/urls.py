from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, CampaignRecipientViewSet, NewsletterViewSet

router = DefaultRouter()
router.register("campaigns", CampaignViewSet, basename="campaign")
router.register("recipients", CampaignRecipientViewSet, basename="campaignrecipient")
router.register("newsletters", NewsletterViewSet, basename="newsletter")

urlpatterns = [
    path("", include(router.urls)),
]
