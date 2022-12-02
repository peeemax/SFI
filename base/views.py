from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Anfitrião, Morador
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from base.forms import FamiliaForm, MoradorForm

class ListaResumoAnfitriaoView(ListView):
    model = Anfitrião
    queryset = Anfitrião.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset
    
    # def get_number_morador(self, **kwargs):


@login_required  
def morador_list(request):
    moradores = Morador.objects.all().order_by('nome_completo')
    return render(request, 'base/resumo_morador_list.html', {'moradores': moradores})

    
@login_required
def cadastrar_familia_anfitriao(request):
    if request.method == "GET":
        form = FamiliaForm()
        context = {
            'form': form
        }
        return render(request, 'base/form_cadastro_anfitrião.html', context=context)
    else:
        form = FamiliaForm(request.POST)
        if form.is_valid():
            familia = form.save()
            form = FamiliaForm()
            
        context = {
        'form': form
        }
        return render(request, 'base/form_cadastro_anfitrião.html', context=context)

@login_required
def cadastrar_morador(request):
    if request.method == "GET":
        form = MoradorForm()
        context = {
            'form': form
        }
        return render(request, 'base/form_cadastro_morador.html', context=context)
    else:
        form = MoradorForm(request.POST)
        if form.is_valid():
            familia = form.save()
            form = MoradorForm()
            
        context = {
        'form': form
        }
    return render(request, 'base/form_cadastro_morador.html', context=context)

