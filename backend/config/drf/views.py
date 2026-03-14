from drf_spectacular.views import SpectacularAPIView as SAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(exclude=True)
class SpectacularAPIView(SAPIView):
    url_name = "api-schema"
