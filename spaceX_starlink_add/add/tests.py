from django.test import TestCase
from rest_framework.test import RequestsClient

client = RequestsClient()


class SpaceXStarlinkTest(TestCase):
    # def setUp(self) -> None:
    # csrfResponse =

    def test_add(self):
        addJson = {
            "satelliteId": 1,
            "satelliteName": "one",
            "comments": "first",
            "xCoordinate": 2,
            "yCoordinate": 3
        }

        postResponse = client.post('http://127.0.0.1:8000/add/', json=addJson)
        assert postResponse.status_code == 200

        getResponse = client.get('http://127.0.0.1:8000/add/')
        assert getResponse.status_code == 200
        getData = getResponse
