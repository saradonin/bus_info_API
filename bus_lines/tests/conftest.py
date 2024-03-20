import os
import sys
import random
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from bus_lines.models import Carrier, Organizer, Line, TYPES
from utils import create_fake_organizer, create_fake_carrier, create_fake_line

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def user_logged_in():
    user = User.objects.create_user(
        username='test_user', password='test_password', email='test@email.com')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    client.login(username='test_user', password='test_password')
    user.client = client
    return client


@pytest.fixture
def set_up():
    for i in range(5):
        create_fake_organizer()
        create_fake_carrier()

    for _ in range(10):
        create_fake_line()
