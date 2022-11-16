from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from base.forms import FamiliaForm

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
