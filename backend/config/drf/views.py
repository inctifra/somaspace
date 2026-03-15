from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView as SAPIView


@extend_schema(exclude=True)
class SpectacularAPIView(SAPIView):
    url_name = "api-schema"
