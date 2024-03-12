from django.db import models


class Organizer(models.Model):
    """
    Represents local government unit
    """
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=32)
    postcode = models.CharField(max_length=32)
    address = models.CharField(max_length=255)

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
        ('public', 'użyeczeności publicznej'),
)


class Line(models.Model):
    """
    Represents bus line
    """
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    permit_number = models.CharField(max_length=32)
    type = models.CharField(max_length=64, choices=TYPES, default=TYPES[0])
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    schedule = models.FileField(upload_to='shedules/')
    valid_from = models.DateField(null=True)
    valid_untill = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
