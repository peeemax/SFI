from django.urls import include, path
from django.contrib.auth.decorators import login_required
from base.views import FamiliaDeleteView, FamiliaUpdateView, morador_atualizar, morador_deletar, moradores, cadastrar_familia_anfitriao, cadastrar_morador, ListaResumoAnfitriaoView



app_name = 'base'
urlpatterns = [
    path('', login_required(ListaResumoAnfitriaoView.as_view()), name='anfitrião.list'),
    path('cadastro_família/', cadastrar_familia_anfitriao, name='cadastro_família'),
    path('atualizar/<int:pk>/', login_required(FamiliaUpdateView.as_view()), name='família.atualizar'),
    path('deletar/<int:pk>/', login_required(FamiliaDeleteView.as_view()), name='família.deletar'),
    path('cadastro_morador/', cadastrar_morador, name='cadastro_morador'),
    path('resumo_moradores/<int:anfitriao_id>/', 
         login_required(moradores), name='resumo_moradores'),
    path('resumo_morador/<int:anfitriao_id>/<int:id>/atualizar', 
         login_required(morador_atualizar), name='morador.atualizar'),
    path('resumo_morador/<int:anfitriao_id>/<int:id>/deletar', 
         login_required(morador_deletar), name='morador.deletar')    
]