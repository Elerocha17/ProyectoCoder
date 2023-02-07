from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Entregables, Estudiantes
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EntregablesFormulario, EstudiantesFormulario

# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")
    
def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

 
def cursos(request):
 
      if request.method == "POST":
 
            miFormulario = CursoFormulario(request.POST) 
 
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  curso = Curso(nombre=info["curso"], camada=info["camada"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/cursos.html", {"form1": miFormulario})

def profesores(request):

    if request.method == "POST":
 
            miFormulario = ProfesorFormulario(request.POST)

            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
                  profesor.save()
                  return render(request, "AppCoder/inicio.html")
            
    else:
            miFormulario = ProfesorFormulario()
 
    return render(request, "AppCoder/profesores.html", {"form2": miFormulario})

def entregables(request):

    if request.method == "POST":
 
            miFormulario = EntregablesFormulario(request.POST)

            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  entregable = Entregables(nombre=info["nombre"], fecha=info["fecha"], entregado=info["entregado"])
                  entregable.save()
                  return render(request, "AppCoder/inicio.html")
            
    else:
            miFormulario = EntregablesFormulario()
 
    return render(request, "AppCoder/entregables.html", {"form3": miFormulario})

def estudiantes(request):

    if request.method == "POST":
 
            miFormulario = EstudiantesFormulario(request.POST)

            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  estudiante = Estudiantes(nombre=info["nombre"], apellido=info["apellido"])
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html")
            
    else:
            miFormulario = EstudiantesFormulario()

    return render(request, "AppCoder/estudiantes.html", {"form4": miFormulario})

def busquedaCamada(request):
        return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["camada"]:
        camada = request.GET["camada"]
        curso = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "Datos incorrectos."

    return HttpResponse(respuesta)
                