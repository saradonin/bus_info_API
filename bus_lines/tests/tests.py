import pytest
import json
from django.urls import reverse
from bus_lines.models import Carrier, Organizer, Line
from utils import fake_line_data, create_fake_line


@pytest.mark.django_db
def test_organizer_get_list(client, set_up):
    response = client.get(reverse('organizer-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Organizer.objects.count()


@pytest.mark.django_db
def test_carrier_get_list(client, set_up):
    response = client.get(reverse('carrier-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Carrier.objects.count()


@pytest.mark.django_db
def test_line_get_list(client, set_up):
    response = client.get(reverse('line-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Line.objects.count()


@pytest.mark.django_db
def test_line_get_list_by_carrier(client, set_up):
    carrier_id = Carrier.objects.order_by('?')[0].id
    url = reverse('line-list-by-carrier', kwargs={'carrier_id': carrier_id})
    response = client.get(url, {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Line.objects.filter(
        carrier=carrier_id).count()


@pytest.mark.django_db
def test_line_get_list_by_organizer(client, set_up):
    organizer_id = Organizer.objects.order_by('?')[0].id
    url = reverse('line-list-by-organizer',
                  kwargs={'organizer_id': organizer_id})
    response = client.get(url, {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Line.objects.filter(
        organizer=organizer_id).count()


@pytest.mark.django_db
def test_line_get_details(client, set_up):
    line = Line.objects.first()
    url = reverse('line-details', kwargs={'pk': line.id})
    response = client.get(url, {}, format='json')

    assert response.status_code == 200
    for field in ("name", "number", "permit_number"):
        assert field in response.data


# TODO fix 400 error
@pytest.mark.django_db
def test_line_post(client, set_up):
    prev_line_count = Line.objects.count()

    new_line = fake_line_data()

    url = reverse('line-list')
    response = client.post(url, new_line, format='json')

    assert response.status_code == 201
    assert Line.objects.count() == prev_line_count + 1

    for key, value in new_line.items():
        assert key in response.data
        if key != "date_created":
            assert response.data[key] == value


@pytest.mark.django_db
def test_line_delete(client, set_up):
    prev_line_count = Line.objects.count()
    line = Line.objects.first()
    url = reverse('line-details', kwargs={'pk': line.id})
    response = client.delete(url, {}, format='json')

    assert response.status_code == 204
    assert Line.objects.count() == prev_line_count - 1
