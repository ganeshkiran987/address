from django.db import models
import uuid

class Address(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    latitude = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, null=True, blank=True)
