import factory
from bunifu_django_auth.models import BunifuUser
from factory.django import DjangoModelFactory
from faker import Faker

from apps.accounts.models import Profile

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = BunifuUser

    email = faker.email()


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
