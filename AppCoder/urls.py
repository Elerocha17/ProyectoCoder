from django.urls import path
from AppCoder import views
from AppCoder.views import resultados, busquedaCamada


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path("cursoFormulario/", views.cursoFormulario, name="CursoFormulario"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
]
