from django.db.models import models

class BaseModel(models.Model):
    """
    An abstract base model that provides common fields for all models.
    """

    id_active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]