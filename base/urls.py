from django.urls import include, path
from django.contrib.auth.decorators import login_required
from base.views import FamiliaDeleteView, FamiliaUpdateView, morador_list, cadastrar_familia_anfitriao, cadastrar_morador, ListaResumoAnfitriaoView

app_name = 'base'
urlpatterns = [
    path('', login_required(ListaResumoAnfitriaoView.as_view()), name='anfitrião.list'),
    path('cadastro_família/', cadastrar_familia_anfitriao, name='cadastro_família'),
    path('<int:pk>/atualizar', login_required(FamiliaUpdateView.as_view()), name='família.atualizar'),
    path('<int:pk>/deletar', login_required(FamiliaDeleteView.as_view()), name='família.deletar'),
    path('cadastro_morador/', cadastrar_morador, name='cadastro_morador'),
    path('resumo_moradores/', morador_list, name='resumo_moradores'),
]