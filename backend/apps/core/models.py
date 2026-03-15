import uuid

from django.db import models


class TimeStampModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        max_length=2000,
        primary_key=True,
        db_index=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
