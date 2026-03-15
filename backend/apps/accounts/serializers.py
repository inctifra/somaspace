from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as _TokenObtainPairSerializer,
)

from apps.accounts.models import Profile


class TokenObtainPairSerializer(_TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        try:
            profile = get_object_or_404(
                Profile,
                user=user,
            )
        except Profile.DoesNotExist:
            token["role"] = "user"
        token["role"] = profile.role
        return token
