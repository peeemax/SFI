from django.urls import path

from base.views import home, cadastrar_familia_anfitriao

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('cadastro_família/', cadastrar_familia_anfitriao, name='cadastro_família')
]