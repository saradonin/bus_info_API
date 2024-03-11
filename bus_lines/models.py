from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Carrier(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=255)