from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cursos
from datetime import datetime
# Create your views here.
def acessar_curso(request):
    return render(request, 'cursos/acessar_curso.html')

def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'cursos/criar_curso.html', {'status':status})
    elif request.method == "POST":
        nome = request.POST.get('nome')# Retorna um dict com o que o usuário digitou
        carga_horaria = request.POST.get('carga')# Retorna um dict com o que o usuário digitou
        curso = Cursos(
            nome = nome,
            carga_horaria = carga_horaria,
            data_criacao = datetime.now()
        )
        curso.save()

        return redirect('/cursos/criar_curso/?status=1')