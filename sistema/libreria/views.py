from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from .models import Libro
from .forms import LibroForm
# Create your views here.


def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/index.html", {'libros': libros})

def obtener_registros(request):
    registros = Libro.objects.all()
    data = []

    for registro in registros:
        data.append({
            'pk': registro.pk,
            'titulo': registro.titulo,
            'imagen': registro.imagen.url,
            'descripcion': registro.descripcion,
            'url_editar': reverse('editar', args=[registro.pk]),  # Reemplaza 'editar' con el nombre de tu vista de edición
            'url_eliminar': reverse('eliminar', args=[registro.pk]),  # Reemplaza 'eliminar' con el nombre de tu vista de eliminación
        })

    return JsonResponse(data, safe=False)


def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, "libros/crear.html", {'formulario': formulario})

def editar(request):
    return render(request, "libros/editar.html")

def form(request):
    return render(request, "libros/form.html")

# Tercera parte del curso de Django
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


# cuarta parte del curso de Django
def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, "libros/editar.html", {'formulario': formulario})

