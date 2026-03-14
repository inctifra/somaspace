from django.db import models
from bunifu_django_auth.models import BunifuUser as User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(verbose_name=_("First Name"), blank=True, null=True, max_length=255)
    lname = models.CharField(verbose_name=_("Last Name"), blank=True, null=True, max_length=255)
    role = models.CharField(max_length=100, choices=(
        ("student", "Student"),
        ("admin", "Admin")
    ), default="student")

    def __str__(self):
        return (
            f"{self.fname} {self.lname}" if self.get_full_name else f"{self.user.email}"
        )

    @property
    def get_full_name(self) -> str | None:
        return f"{self.fname} {self.lname}" if (self.fname and self.lname) else None
