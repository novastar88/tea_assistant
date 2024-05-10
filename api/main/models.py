from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.JSONField()
    category = models.CharField(max_length=50, null=True, blank=True)
