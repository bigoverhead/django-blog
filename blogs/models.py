from django.db import models
from core import models as core_models


class Blog(core_models.AbstractModel):

    """Post Model"""

    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title
