from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageViewSet, SectionViewSet

router = DefaultRouter()
router.register("pages", PageViewSet, basename="page")
router.register("sections", SectionViewSet, basename="section")

urlpatterns = [
    path("", include(router.urls)),
]
