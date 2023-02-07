from django import forms
 
class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudiantesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)

class ProfesorFormulario(forms.Form):
    nombre= forms. CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class EntregablesFormulario(forms.Form): 
    nombre= forms.CharField(max_length=30)
    fecha = forms.DateField()
    entregado = forms.BooleanField()