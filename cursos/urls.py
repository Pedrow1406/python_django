from django.urls import path, include
from . import views
urlpatterns = [
    path('acessar_curso/', views.acessar_curso),
    path('criar_curso/', views.criar_curso)
]