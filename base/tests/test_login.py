import pytest
from django.urls import reverse
from model_mommy import mommy

from SFI.django_assertions import assert_not_contains, assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))

def test_login_form_page(resp):
    assert resp.status_code == 200

@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = mommy.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo

@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})

def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('base:anfitrião.list')

@pytest.fixture
def resp_com_usuario_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('base:anfitrião.list'))    
    
def test_botao_menu_indisponivel(resp_com_usuario_logado):
    assert_not_contains(resp_com_usuario_logado, 'Menu')
    
def test_link_de_login_indisponivel(resp_com_usuario_logado):
    assert_not_contains(resp_com_usuario_logado, reverse('login'))
    
def test_botao_saida_disponivel(resp_com_usuario_logado):
    assert_contains(resp_com_usuario_logado, 'Sair')
    
def test_nome_usuario_logado_disponivel(resp_com_usuario_logado, usuario_logado):
    assert_contains(resp_com_usuario_logado, usuario_logado.first_name)
    
def test_link_logout_disponivel(resp_com_usuario_logado):
    assert_contains(resp_com_usuario_logado, reverse('logout'))