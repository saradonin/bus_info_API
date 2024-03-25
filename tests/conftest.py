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
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpassword',
        'password2': 'testpassword',
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    }


@pytest.fixture
def user_logged_in():
    user = User.objects.create_user(
        username='testuser', password='testpassword', email='test@example.com')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    client.login(username='testuser', password='testpassword')
    user.client = client
    return client


@pytest.fixture
def set_up():
    for i in range(5):
        create_fake_organizer()
        create_fake_carrier()

    for _ in range(10):
        create_fake_line()
