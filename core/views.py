from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from .forms import JuegoForm

# Create your views here.
def home(request):
    juegos = Juego.objects.all()
    data = {
        'juegos': juegos
    }
    return render(request, 'core/home.html', data)

def agregar_juego(request):
    data = {
        'form': JuegoForm() 
    }
    if request.method == 'POST':
        formulario_add = JuegoForm(data=request.POST, files=request.FILES)
        if formulario_add.is_valid:
            formulario_add.save()
            data['mensaje'] = "Juego Agregado Correctamente"
        else:
            data["form"] = formulario_add
    return render(request, 'core/agregar_juego.html', data)

def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)

    data = {
        'form': JuegoForm(instance=juego)
    }

    if request.method == 'POST':
        formulario = JuegoForm(data=request.POST, instance=juego, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'core/editar_juego.html', data)

def borrar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    return redirect(to="home")
