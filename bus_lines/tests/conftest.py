import os
import sys

import pytest
from rest_framework.test import APIClient

from bus_lines.models import Organizer

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for i in range(5):
        name = "Organizer " + str(i)
        Organizer.objects.create(name=name)
