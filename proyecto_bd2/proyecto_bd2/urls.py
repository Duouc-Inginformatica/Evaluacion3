"""proyecto_bd2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_gestion2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('footer/', views.footer),
    path('navbar/', views.navbar),
    path('formulario/', views.formulario),
    path('calendario/', views.calendario),
    path('eliminarpersona/', views.eliminarpersona),
    path('buscar/', views.buscar),
    path('eliminar_persona/', views.eliminar_persona),
    path('ingreso_persona/', views.ingresoformulario),
    path('listar_todo_persona/', views.listar_todo_persona ),
    path('listar_todo/', views.listar_todo),
    path('buscarpersona/', views.buscar_persona),

]
