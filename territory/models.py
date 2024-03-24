from django.db import models


class TerritorialUnit(models.Model):
    """
    Represents administrative division unit of the country
    """
    name = models.CharField(max_length=64)
    type_name = models.CharField(max_length=64)
    region = models.CharField(max_length=2)
    county = models.CharField(max_length=2, blank=True, null=True)
    community = models.CharField(max_length=2, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    date = models.DateField()


class Location(models.Model):
    """
    Represents a locality
    """
    name = models.CharField(max_length=64)
    region = models.CharField(max_length=2)
    county = models.CharField(max_length=2, blank=True, null=True)
    community = models.CharField(max_length=2, blank=True, null=True)
    community_type = models.CharField(max_length=1)
    location_type = models.CharField(max_length=2)

    symbol = models.CharField(max_length=8)
    symbol_podst = models.CharField(max_length=8)
    date = models.DateField()

    def __str__(self):
        return self.name
