from urllib import response
from django.test import Client
from django.urls import reverse
import pytest
from SFI.django_assertions import assert_contains
from base.views import ListaResumoAnfitriaoView

@pytest.fixture
def resp(client):
    resp = client.get(reverse(ListaResumoAnfitriaoView.as_view()))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200
    
def test_title(resp):
    assert_contains(resp, '<title>Sistema Famílias Igreja</title>')
    
def test_home_link(resp):
    assert_contains(resp, f'href="{reverse(ListaResumoAnfitriaoView.as_view())}">Sistema Famílias Igreja</a>')
    