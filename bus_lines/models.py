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


class Line(models.Model):
    """
    Represents bus line
    """
    PERMIT_TYPES = (
        ('zezwolenie', 'zezwolenie'),
        ('zaświadczenie', 'zaświadczenie'),
        ('zgłoszenie', 'zgłoszenie'),
    )
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    permit_number = models.CharField(max_length=32)
    permit_type = models.CharField(max_length=64, choices=PERMIT_TYPES)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    schedule = models.FileField(upload_to='shedules/')
    valid_from = models.DateField()
    valid_untill = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
