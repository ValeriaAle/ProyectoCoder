from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso
def curso(self):
    curso = Curso(nombre = "Desarrollo web", camada = "19881")
    curso.save()
    documentoDeTexto = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
    return HttpResponse(documentoDeTexto)

from AppCoder.forms import CursoFormulario

def cursoFormulario(request):

      if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()

      return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})
