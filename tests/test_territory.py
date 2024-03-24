import pytest
import json
from django.urls import reverse
from territory.models import TerritorialUnits, Location


@pytest.mark.django_db
def test_territorial_units_get_list(client, set_up):
    response = client.get(reverse('territorial-units'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == TerritorialUnits.objects.count()


@pytest.mark.django_db
def test_location_get_list(client, set_up):
    response = client.get(reverse('location-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Location.objects.count()
