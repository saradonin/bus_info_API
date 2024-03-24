import pytest
import json
from django.urls import reverse
from territory.models import TerritorialUnit, Location


@pytest.mark.django_db
def test_territorial_units_get_list(client, set_up):
    response = client.get(reverse('territorial-unit-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == TerritorialUnit.objects.count()


@pytest.mark.django_db
def test_location_get_list(client, set_up):
    response = client.get(reverse('location-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Location.objects.count()
