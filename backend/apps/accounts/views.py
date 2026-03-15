from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenObtainPairSerializer


class LoginTokenView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
