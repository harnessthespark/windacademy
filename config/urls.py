from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/accounts/", include("apps.accounts.urls")),
    path("api/v1/contacts/", include("apps.contacts.urls")),
    path("api/v1/clients/", include("apps.clients.urls")),
    path("api/v1/training/", include("apps.training.urls")),
    path("api/v1/recruitment/", include("apps.recruitment.urls")),
    path("api/v1/campaigns/", include("apps.campaigns.urls")),
    path("api/v1/documents/", include("apps.documents.urls")),
    path("api/v1/dashboard/", include("apps.dashboard.urls")),
    path("api/v1/portal/", include("apps.clients.portal_urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
