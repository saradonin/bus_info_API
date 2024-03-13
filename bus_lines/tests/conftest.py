import os
import sys
import random
import pytest
from rest_framework.test import APIClient

from bus_lines.models import Carrier, Organizer, Line, TYPES
from utils import create_fake_line

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for i in range(5):
        organizer_name = f"Organizer {i}"
        Organizer.objects.create(name=organizer_name)

        carrier_name = f"Company {i}"
        Carrier.objects.create(name=carrier_name)

    for _ in range(10):
        create_fake_line()
