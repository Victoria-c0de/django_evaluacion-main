from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
#importar modelo de reservas
from .models import Reserva
#importar formulario de reservas
from .forms import ReservasForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

#listar reservas
def listarReservas(request):
    #obtener todas las reservas
    reservas = Reserva.objects.all()
    data = {'referencia_r' : reservas}
    #retornar contexto
    return render(request, 'reservas.html', data)

#agregar reservas
def agregarReservas(request):
    form = ReservasForm()

    if (request.method == 'POST'):
        form = ReservasForm(request.POST)
        if (form.is_valid()):
            form.save()
            return index(request)
    

    data = {'form' : form}
    return render(request, 'agregar.html' , data)

#editar reservas
def editarReservas(request, id):
    referencia_r = Reserva.objects.get(id=id)
    form = ReservasForm(instance=referencia_r)

    if (request.method == 'POST'):
        form = ReservasForm(request.POST, instance=referencia_r)
        if (form.is_valid()):
            form.save()
            return index(request)

    data = {'form' : form}
    return render(request, 'agregar.html' , data)

#eliminar reservas
def eliminarReservas(request, id):
    referencia_r = Reserva.objects.get(id=id)
    referencia_r.delete()
    return redirect('/reservas')