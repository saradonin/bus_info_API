from django.db import models


class TerritorialUnits(models.Model):
    name = models.CharField(max_length=64)
    type_name = models.CharField(max_length=64)
    region = models.CharField(max_length=8)
    county = models.CharField(max_length=8, blank=True, null=True)
    community = models.CharField(max_length=8, blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    date = models.DateField()
