from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CandidateViewSet, PlacementViewSet

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
router.register("candidates", CandidateViewSet, basename="candidate")
router.register("placements", PlacementViewSet, basename="placement")

urlpatterns = [
    path("", include(router.urls)),
]
