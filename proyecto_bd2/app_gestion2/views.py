from django.shortcuts import render
from django.http import HttpResponse
from app_gestion2.models import Persona

# Create your views here.

def index(request):
    return render(request,"index.html")

def footer(request):
    return render(request,"footer.html")

def navbar(request):
    return render(request,"navbar.html")

def formulario(request):
    return render(request,"formulario.html")

def calendario(request):
    return render(request,"calendario.html")

def listar_todo(request):
    return render(request,"listar_todo.html")

def ingreso_persona(request):
    return render(request,"ingreso_persona.html")

def buscar(request):
    return render(request,"buscar.html")

def eliminar_persona(request):
    return render(request,"eliminar_persona.html")


# Funciones

def listar_todo_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listar_todo.html",{'personas':datos})
    
def ingresoformulario(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    
    if len(rut)>0 and len(nombre)>0 and len(appaterno)>0 and len(apmaterno)>0 and len(edad)>0 and len(vacuna)>0 and len(fecha)>0:
        per=Persona(rut=rut,nombre=nombre,appaterno=appaterno,apmaterno=apmaterno,edad=edad,vacuna=vacuna,fecha=fecha)  
        per.save()
        mensaje="Persona ingresada"
    else:
        mensaje="Persona no ingresada o faltan datos"
    return HttpResponse(mensaje)



def buscar_persona(request):
    if request.GET["txt_rut"]:
        identificacion = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut__icontains=identificacion)
        return render(request,"listar.html",{"personas":personas,"query":identificacion})
    else:
        mensaje = "Debe ingresar un nombre de persona"
        return HttpResponse(mensaje)


def eliminarpersona(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.delete()
            mensaje = "Persona eliminada"
        else:
            mensaje = "Persona no eliminada. No existe persona con ese rut"
    else:
        mensaje = "Debe ingresar un rut para eliminación"
    return HttpResponse(mensaje)