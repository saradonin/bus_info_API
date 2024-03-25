import pytest
import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_client_register(client, user_data):
    url = reverse('register')
    response = client.post(url, user_data, format='json')
    assert response.status_code == 201
    assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_client_obtain_token(client, user_data):

    User.objects.create_user(
        username=user_data['username'],
        password=user_data['password'],
        email=user_data['email']
    )

    data = {
        'username': user_data['username'],
        'password': user_data['password']
    }
    url = reverse('token-obtain-pair')
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
