import random
from faker import Faker

from bus_lines.models import Carrier, Organizer, Line, TYPES

faker = Faker("pl_PL")

# TODO fix
def fake_line_data():
    line_data = {
        "name": f"{faker.city()} - {faker.city()} - {faker.city()}",
        "number": random.randint(1000, 9999),
        "organizer": Organizer.objects.order_by('?').first().id,
        "carrier": Carrier.objects.order_by('?').first().id,
        "type": random.choice(TYPES)[0],
        "active": True,
    }
    return line_data


def create_fake_line():
    line_data = fake_line_data()
    line_data["carrier"] = Carrier.objects.get(id=line_data["carrier"])
    line_data["organizer"] = Organizer.objects.get(id=line_data["organizer"])
    new_line = Line.objects.create(**line_data)
