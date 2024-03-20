import pytest
from rest_framework.test import APIClient


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
