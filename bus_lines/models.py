from django.db import models
from territory.models import Location, TerritorialUnit


class Organizer(models.Model):
    """
    Represents local government unit
    """
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=32)
    postcode = models.CharField(max_length=32)
    address = models.CharField(max_length=255)

    territorial_unit = models.OneToOneField(
        TerritorialUnit, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Carrier(models.Model):
    """
    Represents carrier company
    """
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=32)
    postcode = models.CharField(max_length=32)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


TYPES = (
        ('regular', 'regularna'),
        ('special', 'regularna-specjalna'),
        ('public', 'użyteczności publicznej'),
)


class Line(models.Model):
    """
    Represents bus line
    """
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    permit_number = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=64, choices=TYPES, default=TYPES[0])
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    schedule = models.FileField(upload_to='shedules/', blank=True, null=True)
    pricing = models.FileField(upload_to='pricing/', blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_untill = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    locations = models.ManyToManyField(Location, blank=True)

    def __str__(self):
        return f"{self.number} {self.name}"
