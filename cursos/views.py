from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cursos
from datetime import datetime
# Create your views here.

def listar_curso(request):
    nome_filtrar = request.GET.get('nome_filtrado')
    carga_filtrar = request.GET.get('carga_filtrada')
    estado_ativo = request.GET.get('estado_ativo')
    estado_desativo = request.GET.get('estado_desativo')
    cursos = Cursos.objects.all()

    if estado_ativo and estado_desativo: 
        cursos = Cursos.objects.all()
    elif estado_ativo:
        estado_ativo = True
        cursos = cursos.filter(ativo=estado_ativo)
    elif estado_desativo:
        estado_desativo = False
        cursos = cursos.filter(ativo=estado_desativo)
        
    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)
    if carga_filtrar:
       cursos = cursos.filter(carga_horaria__gte=carga_filtrar) # gte == greater than equal
        

    return render(request, 'cursos/listar_curso.html', {'cursos':cursos})



def ver_curso(request, id):
    curso = Cursos.objects.get(id=id)
    print(curso)
    return render(request, 'cursos/ver_curso.html', {'curso': curso})


def desativar_curso(request, id):
    curso = Cursos.objects.get(id=id)
    curso.ativo = False
    curso.save()
    return redirect('/cursos/listar_curso/')


def ativar_curso(request, id):
    curso = Cursos.objects.get(id=id)
    curso.ativo = True
    curso.save()
    return redirect('/cursos/listar_curso/')


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