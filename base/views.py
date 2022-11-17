from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from base.forms import FamiliaForm, MoradorForm

def home(request):
    return render(request, 'base/home.html')

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