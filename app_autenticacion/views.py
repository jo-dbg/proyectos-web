from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth.models import User


def autenticacion(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=usuario, password=password)

        if user:
            login(request, user)
            return redirect('inicio')

    return render(request, 'app_autenticacion/autenticacion.html')


@permission_required('auth.view_user', raise_exception=True)
def lista_usuarios(request):
    usuarios = User.objects.all().order_by('username')
    return render(request, 'app_autenticacion/usuarios.html', {'usuarios': usuarios})

def cerrar_sesion(request):
    logout(request)
    return redirect('autenticacion')

@login_required
def inicio(request):
    return render(request, 'app_autenticacion/inicio.html')