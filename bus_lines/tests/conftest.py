import os
import sys
import random
import pytest
from rest_framework.test import APIClient

from bus_lines.models import Carrier, Organizer, Line, TYPES
from utils import create_fake_organizer, create_fake_carrier, create_fake_line

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for i in range(5):
        create_fake_organizer()
        create_fake_carrier()

    for _ in range(10):
        create_fake_line()
