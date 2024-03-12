import pytest

from bus_lines.models import Organizer


@pytest.mark.django_db
def test_get_organizer_list(client, set_up):
    response = client.get("/organizers/", {}, format='json')

    assert response.status_code == 200
    assert Organizer.objects.count() == len(response.data)
