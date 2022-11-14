from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base/home.html')

def cadastrar_familia_anfitriao(request):
    return render(request, 'form_cadastro_anfitrião')
