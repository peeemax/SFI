from django.urls import include, path

from base.views import login, processo_login, cadastrar_familia_anfitriao, cadastrar_membro, ListaResumoAnfitriaoView

app_name = 'base'
urlpatterns = [
    path('', ListaResumoAnfitriaoView.as_view(), name='anfitrião.list'),
    path('cadastro_família/', cadastrar_familia_anfitriao, name='cadastro_família'),
    path('cadastro_membro/', cadastrar_membro, name='cadastro_membro'),
    path('login/', login),
    path('processo_login/', processo_login),
]