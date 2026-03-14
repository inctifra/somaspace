from .serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginTokenView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
