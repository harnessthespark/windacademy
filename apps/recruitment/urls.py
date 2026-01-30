from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CandidateViewSet, InterviewViewSet, PlacementViewSet

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
router.register("candidates", CandidateViewSet, basename="candidate")
router.register("interviews", InterviewViewSet, basename="interview")
router.register("placements", PlacementViewSet, basename="placement")

urlpatterns = [
    path("", include(router.urls)),
]
