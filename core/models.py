from django.db import models


class AbstractModel(models.Model):

    """Custom Abstract Mdoel"""

    created_at = models.DateTimeField(auto_now_add=True)
    updatea_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
