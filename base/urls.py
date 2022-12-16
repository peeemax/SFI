from django.urls import path
from django.contrib.auth.decorators import login_required
from base.views import FamiliaDeleteView, FamiliaUpdateView, morador_atualizar, morador_deletar, moradores, cadastrar_familia_anfitriao, cadastrar_morador, ListaResumoAnfitriaoView
app_name = 'base'

urlpatterns = [
    path('', login_required(ListaResumoAnfitriaoView.as_view()), name='anfitrião.list'),
    path('cadastro_familia/', cadastrar_familia_anfitriao, name='cadastro.família'),
    path('<int:pk>/atualizar', login_required(FamiliaUpdateView.as_view()), name='família.atualizar'),
    path('<int:pk>/deletar', login_required(FamiliaDeleteView.as_view()), name='família.deletar'),
    path('cadastro_morador/', cadastrar_morador, name='cadastro.morador'),
    path('<int:anfitriao_id>/moradores', 
         login_required(moradores), name='anfitriao.moradores'),
    path('<int:anfitriao_id>/morador/<int:id>/atualizar', 
         login_required(morador_atualizar), name='morador.atualizar'),
    path('<int:anfitriao_id>/morador/<int:id>/deletar', 
         login_required(morador_deletar), name='morador.deletar')    
]