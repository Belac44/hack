from django.db import models
from config.base_model import BaseModel

class Allergy(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
