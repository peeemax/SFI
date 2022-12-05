from django.urls import include, path
from django.contrib.auth.decorators import login_required
from base.views import FamiliaDeleteView, FamiliaUpdateView, morador_list, cadastrar_familia_anfitriao, cadastrar_morador, ListaResumoAnfitriaoView
from . import views


app_name = 'base'
urlpatterns = [
    path('', login_required(ListaResumoAnfitriaoView.as_view()), name='anfitrião.list'),
    path('cadastro_família/', cadastrar_familia_anfitriao, name='cadastro_família'),
    path('<int:pk>/atualizar', login_required(FamiliaUpdateView.as_view()), name='família.atualizar'),
    path('<int:pk>/deletar', login_required(FamiliaDeleteView.as_view()), name='família.deletar'),
    path('cadastro_morador/', cadastrar_morador, name='cadastro_morador'),
    path('<int:pk_anfitriao>/resumo_moradores', 
         login_required(views.moradores), name='resumo_moradores'),
]