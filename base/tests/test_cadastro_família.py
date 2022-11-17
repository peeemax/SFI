from urllib import response
from django.test import Client
from django.urls import reverse
import pytest
# from SFI.django_assertions import assert_contains

@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:cadastro_família'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200


    