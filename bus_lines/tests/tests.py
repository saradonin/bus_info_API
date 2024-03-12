import pytest

from bus_lines.models import Carrier, Organizer, Line


@pytest.mark.django_db
def test_get_organizer_list(client, set_up):
    response = client.get("/organizers/", {}, format='json')

    assert response.status_code == 200
    assert Organizer.objects.count() == len(response.data)
    
    
@pytest.mark.django_db
def test_get_carrier_list(client, set_up):
    response = client.get("/carriers/", {}, format='json')
    
    assert response.status_code == 200
    assert Carrier.objects.count() == len(response.data)
    
    
@pytest.mark.django_db
def test_get_line_list(client, set_up):
    response = client.get("/lines/", {}, format='json')
    
    assert response.status_code == 200
    assert Line.objects.count() == len(response.data)

