import pytest
from django.urls import reverse
from bus_lines.models import Carrier, Organizer, Line


@pytest.mark.django_db
def test_get_organizer_list(client, set_up):
    response = client.get(reverse('organizer-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Organizer.objects.count()


@pytest.mark.django_db
def test_get_carrier_list(client, set_up):
    response = client.get(reverse('carrier-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Carrier.objects.count()


@pytest.mark.django_db
def test_get_line_list(client, set_up):
    response = client.get(reverse('line-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Line.objects.count()


@pytest.mark.django_db
def test_get_line_list_by_carrier(client, set_up):
    carrier_id = Carrier.objects.order_by('?')[0].id
    url = reverse('line-list-by-carrier', kwargs={'carrier_id': carrier_id})
    response = client.get(url, {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Line.objects.filter(
        carrier=carrier_id).count()


@pytest.mark.django_db
def test_get_line_list_by_organizer(client, set_up):
    organizer_id = Organizer.objects.order_by('?')[0].id
    url = reverse('line-list-by-organizer',
                  kwargs={'organizer_id': organizer_id})
    response = client.get(url, {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Line.objects.filter(
        organizer=organizer_id).count()
