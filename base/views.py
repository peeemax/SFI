from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Anfitrião, Morador
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from base.forms import FamiliaForm, MoradorForm

class ListaResumoAnfitriaoView(ListView):
    model = Anfitrião
    queryset = Anfitrião.objects.all().order_by('nome_completo')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset
    
    
@login_required
def cadastrar_familia_anfitriao(request):
    if request.method == "GET":
        form = FamiliaForm()
        context = {
            'form': form
        }
        return render(request, 'base/anfitrião_form.html', context=context)
    else:
        form = FamiliaForm(request.POST)
        if form.is_valid():
            familia = form.save()
            form = FamiliaForm()
            
        context = {
        'form': form
        }
        return render(request, 'base/anfitrião_form.html', context=context)


   
class FamiliaUpdateView(UpdateView):
    model = Anfitrião
    form_class = FamiliaForm
    success_url = '/'


class FamiliaDeleteView(DeleteView):
    model = Anfitrião
    success_url = '/'

@login_required
def cadastrar_morador(request):
    if request.method == "GET":
        form = MoradorForm()
        context = {
            'form': form
        }
        return render(request, 'base/morador_form.html', context=context)
    else:
        form = MoradorForm(request.POST)
        if form.is_valid():
            familia = form.save()
            form = MoradorForm()
            
        context = {
        'form': form
        }
    return render(request, 'base/morador_form.html', context=context)

def moradores(request, anfitriao_id):
    moradores = Morador.objects.filter(anfitriao=anfitriao_id)
    return render(request, 'base/morador_list.html', {'moradores': moradores, 'anfitriao_id': anfitriao_id})

def morador_atualizar(request, anfitriao_id, id):
    morador = get_object_or_404(Morador, id=id)
    form = MoradorForm(instance=morador)
    if request.method == "POST":
        form = MoradorForm(request.POST, instance=morador)
        if form.is_valid():
            form.save()
            return redirect(reverse('anfitriao.moradores', args=[anfitriao_id]))
        
    return render(request, 'base/morador_form.html', {'form': form})

def morador_deletar(request, anfitriao_id, id):
    morador = get_object_or_404(Morador, id=id)
    morador.delete()
    return redirect(reverse('morador', args=[anfitriao_id]))