from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Albums

from .forms import AlbumForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def albums(request):
    albums = Albums.objects.all()
    print(albums)
    return render(request,'albums/index.html', {'albums': albums})

def crear(request):
    formulario = AlbumForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('albums')
    return render(request,'albums/crear.html', {'formulario': formulario})

def editar(request, id):
    albums = Albums.objects.get(id=id)
    formulario = AlbumForm(request.POST or None, request.FILES or None , instance=albums)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('albums')
    return render(request,'albums/editar.html', {'formulario': formulario})

def eliminar(request, id):
    albums = Albums.objects.get(id=id)
    albums.delete()
    return redirect('albums')





