from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario



class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)