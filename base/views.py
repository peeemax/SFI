from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Anfitrião

from base.forms import FamiliaForm, MoradorForm

class ListaResumoAnfitriaoView(ListView):
    model = Anfitrião
    queryset = Anfitrião.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset
    

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


def cadastrar_membro(request):
    if request.method == "GET":
        form = MoradorForm()
        context = {
            'form': form
        }
        return render(request, 'base/form_cadastro_membro.html', context=context)
    else:
        form = MoradorForm(request.POST)
        if form.is_valid():
            familia = form.save()
            form = MoradorForm()
            
        context = {
        'form': form
        }
        return render(request, 'base/form_cadastro_membro.html', context=context)