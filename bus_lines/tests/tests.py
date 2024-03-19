import pytest
import json
from django.urls import reverse
from bus_lines.models import Carrier, Organizer, Line
from utils import fake_line_data, fake_organizer_data, fake_carrier_data


@pytest.mark.django_db
def test_organizer_get_list(client, set_up):
    response = client.get(reverse('organizer-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Organizer.objects.count()


@pytest.mark.django_db
def test_organizer_post(user_logged_in, set_up):
    prev_organizer_count = Organizer.objects.count()
    new_organizer = fake_organizer_data()
    url = reverse('organizer-list')

    response = user_logged_in.post(url, new_organizer, format='json')
    invalid_response = user_logged_in.post(url, None, format='json')

    assert invalid_response.status_code == 400
    assert response.status_code == 201
    assert Organizer.objects.count() == prev_organizer_count + 1

    for key, value in new_organizer.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_organizer_post_unauthorized(client, set_up):
    prev_organizer_count = Organizer.objects.count()
    new_organizer = fake_organizer_data()
    url = reverse('organizer-list')

    response = client.post(url, new_organizer, format='json')
    assert response.status_code == 403
    assert Organizer.objects.count() == prev_organizer_count
    assert not Organizer.objects.filter(name=new_organizer["name"]).exists()


@pytest.mark.django_db
def test_organizer_update(user_logged_in, set_up):
    old_organizer = Organizer.objects.first()
    new_organizer = fake_organizer_data()
    url = reverse('organizer-details', kwargs={'pk': old_organizer.id})

    response = user_logged_in.patch(url, new_organizer, format='json')

    assert response.status_code == 200
    assert not Organizer.objects.filter(name=old_organizer.name).exists()
    for key, value in new_organizer.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_organizer_update_unauthorized(client, set_up):
    old_organizer = Organizer.objects.first()
    new_organizer = fake_organizer_data()
    url = reverse('organizer-details', kwargs={'pk': old_organizer.id})

    response = client.patch(url, new_organizer, format='json')

    assert response.status_code == 403
    assert Organizer.objects.filter(name=old_organizer.name).exists()
    assert not Organizer.objects.filter(name=new_organizer["name"]).exists()


@pytest.mark.django_db
def test_organizer_delete(user_logged_in, set_up):
    prev_organizer_count = Organizer.objects.count()
    organizer = Organizer.objects.first()
    url = reverse('organizer-details', kwargs={'pk': organizer.id})
    response = user_logged_in.delete(url, {}, format='json')

    assert response.status_code == 204
    assert Organizer.objects.count() == prev_organizer_count - 1
    assert not Organizer.objects.filter(id=organizer.id).exists()


@pytest.mark.django_db
def test_organizer_delete_unauthorized(client, set_up):
    prev_organizer_count = Organizer.objects.count()
    organizer = Organizer.objects.first()
    url = reverse('organizer-details', kwargs={'pk': organizer.id})
    response = client.delete(url, {}, format='json')

    assert response.status_code == 403
    assert Organizer.objects.count() == prev_organizer_count
    assert Organizer.objects.filter(id=organizer.id).exists()


@pytest.mark.django_db
def test_carrier_get_list(client, set_up):
    response = client.get(reverse('carrier-list'), {}, format='json')

    assert response.status_code == 200
    assert len(response.data) == Carrier.objects.count()


@pytest.mark.django_db
def test_carrier_post(user_logged_in, set_up):
    prev_carrier_count = Carrier.objects.count()
    new_carrier = fake_carrier_data()

    url = reverse('carrier-list')
    response = user_logged_in.post(url, new_carrier, format='json')
    invalid_response = user_logged_in.post(url, None, format='json')

    assert invalid_response.status_code == 400
    assert response.status_code == 201
    assert Carrier.objects.count() == prev_carrier_count + 1

    for key, value in new_carrier.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_carrier_post_unauthorized(client, set_up):
    prev_carrier_count = Carrier.objects.count()
    new_carrier = fake_carrier_data()

    url = reverse('carrier-list')
    response = client.post(url, new_carrier, format='json')
    assert response.status_code == 403
    assert Carrier.objects.count() == prev_carrier_count
    assert not Carrier.objects.filter(name=new_carrier["name"]).exists()


@pytest.mark.django_db
def test_carrier_update(user_logged_in, set_up):
    old_carrier = Carrier.objects.first()
    new_carrier = fake_carrier_data()
    url = reverse('carrier-details', kwargs={'pk': old_carrier.id})

    response = user_logged_in.patch(url, new_carrier, format='json')

    assert response.status_code == 200
    assert not Carrier.objects.filter(name=old_carrier.name).exists()
    for key, value in new_carrier.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_carrier_update_unauthorozed(client, set_up):
    old_carrier = Carrier.objects.first()
    new_carrier = fake_carrier_data()
    url = reverse('carrier-details', kwargs={'pk': old_carrier.id})

    response = client.patch(url, new_carrier, format='json')

    assert response.status_code == 403
    assert Carrier.objects.filter(name=old_carrier.name).exists()
    assert not Carrier.objects.filter(name=new_carrier["name"]).exists()


@pytest.mark.django_db
def test_carrier_delete(user_logged_in, set_up):
    prev_carrier_count = Carrier.objects.count()
    carrier_to_delete = Carrier.objects.first()
    url = reverse('carrier-details', kwargs={'pk': carrier_to_delete.id})
    response = user_logged_in.delete(url, {}, format='json')

    assert response.status_code == 204
    assert Carrier.objects.count() == prev_carrier_count - 1
    assert not Carrier.objects.filter(id=carrier_to_delete.id).exists()


@pytest.mark.django_db
def test_carrier_delete_unauthorized(client, set_up):
    prev_carrier_count = Carrier.objects.count()
    carrier_to_delete = Carrier.objects.first()
    url = reverse('carrier-details', kwargs={'pk': carrier_to_delete.id})
    response = client.delete(url, {}, format='json')

    assert response.status_code == 403
    assert Carrier.objects.count() == prev_carrier_count
    assert Carrier.objects.filter(id=carrier_to_delete.id).exists()


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


@pytest.mark.django_db
def test_line_post(user_logged_in, set_up):
    prev_line_count = Line.objects.count()

    new_line = fake_line_data()

    url = reverse('line-list')
    response = user_logged_in.post(url, new_line, format='json')
    invalid_response = user_logged_in.post(url, None, format='json')

    assert invalid_response.status_code == 400
    assert response.status_code == 201
    assert Line.objects.count() == prev_line_count + 1

    for key, value in new_line.items():
        assert key in response.data
        if key != "date_created":
            assert response.data[key] == value


@pytest.mark.django_db
def test_line_post_unauthorized(client, set_up):
    prev_line_count = Line.objects.count()

    new_line = fake_line_data()

    url = reverse('line-list')
    response = client.post(url, new_line, format='json')
    assert response.status_code == 403
    assert Line.objects.count() == prev_line_count
    assert not Line.objects.filter(
        name=new_line["name"], number=new_line["number"], organizer=new_line["organizer"], carrier=new_line["carrier"]).exists()


@pytest.mark.django_db
def test_line_update(user_logged_in, set_up):
    old_line = Line.objects.first()
    new_line = fake_line_data()
    url = reverse('line-details', kwargs={'pk': old_line.id})

    response = user_logged_in.patch(url, new_line, format='json')

    assert response.status_code == 200
    assert not Line.objects.filter(
        name=old_line.name, number=old_line.number, organizer=old_line.organizer).exists()
    for key, value in new_line.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_line_update_unauthorized(client, set_up):
    old_line = Line.objects.first()
    new_line = fake_line_data()
    url = reverse('line-details', kwargs={'pk': old_line.id})

    response = client.patch(url, new_line, format='json')

    assert response.status_code == 403
    assert Line.objects.filter(
        name=old_line.name, number=old_line.number, organizer=old_line.organizer, carrier=old_line.carrier).exists()
    assert not Line.objects.filter(
        name=new_line["name"], number=new_line["number"], organizer=new_line["organizer"], carrier=new_line["carrier"]).exists()


@pytest.mark.django_db
def test_line_delete(user_logged_in, set_up):
    prev_line_count = Line.objects.count()
    line = Line.objects.first()
    url = reverse('line-details', kwargs={'pk': line.id})
    response = user_logged_in.delete(url, {}, format='json')

    assert response.status_code == 204
    assert Line.objects.count() == prev_line_count - 1
    assert not Line.objects.filter(id=line.id).exists()


@pytest.mark.django_db
def test_line_delete_unauthorized(client, set_up):
    prev_line_count = Line.objects.count()
    line = Line.objects.first()
    url = reverse('line-details', kwargs={'pk': line.id})
    response = client.delete(url, {}, format='json')

    assert response.status_code == 403
    assert Line.objects.count() == prev_line_count
    assert Line.objects.filter(id=line.id).exists()
