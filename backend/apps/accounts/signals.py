from django.dispatch import receiver
from django.db.models.signals import post_save
from bunifu_django_auth.models import BunifuUser as User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile_on_user_creation(sender, instance, created, **kwargs):
    if created:
        role = "student"
        if instance.is_staff:
            role = "admin"
        Profile.objects.create(user=instance, role=role)
