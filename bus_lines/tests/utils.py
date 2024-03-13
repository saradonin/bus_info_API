import random
import pytz
from faker import Faker
from datetime import datetime

from bus_lines.models import Carrier, Organizer, Line, TYPES

faker = Faker("pl_PL")


def fake_organizer_data():
    city = faker.city()
    office_list = ["Urząd Gminy", "Urząd Miasta", "Starostwo Powiatowe"]
    return {
        "name": f"{random.choice(office_list)} {city}",
        "city": city,
        "postcode": faker.postcode(),
        "address": faker.address()
    }


def create_fake_organizer():
    organizer_data = fake_carrier_data()
    new_organizer = Organizer.objects.create(**organizer_data)
    return new_organizer


def fake_carrier_data():
    return {
        "name": faker.company(),
        "city": faker.city(),
        "postcode": faker.postcode(),
        "address": faker.address()
    }


def create_fake_carrier():
    carrier_data = fake_carrier_data()
    new_carrier = Carrier.objects.create(**carrier_data)
    return new_carrier


def fake_line_data():
    date = faker.date()

    return {
        "name": f"{faker.city()} - {faker.city()} - {faker.city()}",
        "number": str(random.randint(1000, 9999)),
        "active": True,
        "permit_number": str(random.randint(1, 100)),
        "type": random.choice(TYPES)[0],
        "carrier": Carrier.objects.order_by('?')[0].id,
        "organizer": Organizer.objects.order_by('?')[0].id,
        "schedule": None,
        "valid_from": date,
        "valid_untill": date,
    }


def create_fake_line():
    line_data = fake_line_data()
    line_data["carrier"] = Carrier.objects.get(id=line_data["carrier"])
    line_data["organizer"] = Organizer.objects.get(id=line_data["organizer"])
    new_line = Line.objects.create(**line_data)
    return new_line
