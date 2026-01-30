from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DelegateViewSet, TrainerViewSet, ClientContactViewSet

router = DefaultRouter()
router.register("delegates", DelegateViewSet, basename="delegate")
router.register("trainers", TrainerViewSet, basename="trainer")
router.register("client-contacts", ClientContactViewSet, basename="clientcontact")

urlpatterns = [
    path("", include(router.urls)),
]
