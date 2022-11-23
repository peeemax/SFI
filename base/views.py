from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Anfitrião, Morador
from django.contrib.auth import authenticate, login

from base.forms import FamiliaForm, MoradorForm

class ListaResumoAnfitriaoView(ListView):
    model = Anfitrião
    queryset = Anfitrião.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset
    
    # def get_number_morador(self, **kwargs):
        

    

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
    return render('request', 'base/form_cadastro_membro.html', context=context)

    
def login(request):
    return render(request, 'registration/login.html')

    
def processo_login(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('')
    else: 
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'registration/login.html', data)