from django.urls import include, path

from base.views import morador_list, cadastrar_familia_anfitriao, cadastrar_morador, ListaResumoAnfitriaoView

app_name = 'base'
urlpatterns = [
    path('', ListaResumoAnfitriaoView.as_view(), name='anfitrião.list'),
    path('cadastro_família/', cadastrar_familia_anfitriao, name='cadastro_família'),
    path('cadastro_morador/', cadastrar_morador, name='cadastro_morador'),
    path('resumo_moradores/', morador_list, name='resumo_moradores'),
]