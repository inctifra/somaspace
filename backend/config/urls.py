from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from drf_spectacular.views import SpectacularSwaggerView

from apps.accounts.views import LoginTokenView
from .drf.views import SpectacularAPIView
from apps.core._admin import somaspace_admin_site


urlpatterns = [
    # Django Admin
    path("admin/", somaspace_admin_site.urls),
    # superadmin for viewing the other information
    path("superadmin/", admin.site.urls),
    # -----------------------------
    # Core Backend API
    # -----------------------------
    path(
        f"api/{settings.DJANGO_APP_VERSION}/",
        include("config.api_router", namespace="api"),
    ),
    path(f"api/{settings.DJANGO_APP_VERSION}/auth/login/", LoginTokenView.as_view()),
    path(
        f"api/{settings.DJANGO_APP_VERSION}/auth/", include("bunifu_django_auth.urls")
    ),
    path("accounts/", include("allauth.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

# -----------------------------
# Static & Media (Development)
# -----------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
