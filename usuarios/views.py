from .models import User, Manager
from resto.models import Imagen, Restaurante, Categoria
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'usuarios/index.html')

def index_manager(request):
    manager = Manager.objects.get(user_id=request.user.id)
    categorias = Categoria.objects.all()
    try:
        restaurante_ = Restaurante.objects.get(id=manager.restaurante_id)
        if Imagen.objects.filter(restaurante_id=restaurante_.id).exists():
            imagen = Imagen.objects.filter(restaurante_id=restaurante_.id)
            no_imagen = False
            contexto = {'manager': manager, 'imagen': imagen, 'categorias': categorias, 'no_imagen': no_imagen, 'restaurante': restaurante_}
        else:
            no_imagen = True
            contexto = {'manager': manager, 'no_imagen': no_imagen, 'categorias': categorias}
    except Restaurante.DoesNotExist:
        contexto = {'manager': manager, 'categorias': categorias}
    return render(request, 'usuarios/manager_index.html', contexto)


def manager_form(request):
    return render(request, 'usuarios/manager_form.html')

def registrar(request):
    salida = {}
    if request.method == 'POST' and request.is_ajax():

        username1 = request.POST.get('username')
        first_name1 = request.POST.get('first_name')
        last_name1 = request.POST.get('last_name')
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if username1 and first_name1 and last_name1 and email1 and password1 and password2:
            ex_reg = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
            if re.match(ex_reg, email1):
                if len(password1) > 6:
                    if password1 == password2:
                        if not(User.objects.filter(username=username1).exists()):
                            if not(User.objects.filter(username=username1).exists()):
                                user = User.objects.create(username=username1, first_name=first_name1, last_name=last_name1, email=email1, password=password1)
                                user.set_password(request.POST.get('password'))
                                user.save()
                                user = authenticate(username=username1, password=password1)
                                login(request, user)
                                salida = {'success': True, 'msj': 'exito'}
                            else:
                                salida = {'error': True, 'msj': 'Ese email ya esta registrado, intenta con otro'}
                        else:
                            salida = {'error': True, 'msj': 'Ese nombre de usuario ya esta registrado, intenta con otro'}
                    else:
                        salida = {'error': True, 'msj': 'Las contraseñas no coinciden'}
                else:
                    salida = {'error': True, 'msj': 'Por favor imgresauna conraseña mas larga'}
            else:
                salida = {'error': True, 'msj': 'Por favor ingresa un email valido'}
        else:
            salida = {'error': True, 'msj': 'Por favor llena los campos correctamente'}
    return HttpResponse(JsonResponse(salida))


def loguearse(request):
    salida = {}
    if request.method == 'POST' and request.is_ajax():
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        if username1 and password1:
            try:
                get_user = User.objects.get(username=username1)
                get_password = get_user.password
                if check_password(password1, get_password):
                    user = authenticate(username=username1, password=password1)
                    if user is not None:
                        login(request, user)
                        salida = {'success': True, 'msj': 'exito'}
                else:
                    salida = {'error': True, 'msj': 'Contraseña incorrecta'}
            except  User.DoesNotExist:
                salida = {'error': True, 'msj': 'Ese usuario no existe en nuestra base de datos'}
        else:
            salida = {'error': True, 'msj': 'Por favor completa los campos correctamente'}
    return HttpResponse(JsonResponse(salida))


def registrar_manager(request):
    salida = {}
    if request.method == 'POST' and request.is_ajax():

        username1 = request.POST.get('username')
        first_name1 = request.POST.get('first_name')
        last_name1 = request.POST.get('last_name')
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if username1 and first_name1 and last_name1 and email1 and password1 and password2:
            ex_reg = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
            if re.match(ex_reg, email1):
                if len(password1) > 6:
                    if password1 == password2:
                        if not(User.objects.filter(username=username1).exists()):
                            if not(User.objects.filter(username=username1).exists()):
                                new_user = User.objects.create(username=username1, first_name=first_name1, last_name=last_name1, email=email1, password=password1)
                                new_user.set_password(request.POST.get('password'))
                                new_user.is_owner = True
                                new_user.save()
                                manager = Manager.objects.create(user=new_user)
                                manager.save()
                                user = authenticate(username=username1, password=password1)
                                login(request, user)
                                salida = {'success': True, 'msj': 'exito'}
                            else:
                                salida = {'error': True, 'msj': 'Ese email ya esta registrado, intenta con otro'}
                        else:
                            salida = {'error': True, 'msj': 'Ese nombre de usuario ya esta registrado, intenta con otro'}
                    else:
                        salida = {'error': True, 'msj': 'Las contraseñas no coinciden'}
                else:
                    salida = {'error': True, 'msj': 'Por favor ingresa una contraseña mas larga'}
            else:
                salida = {'error': True, 'msj': 'Por favor ingresa un email valido'}
        else:
            salida = {'error': True, 'msj': 'Por favor llena los campos correctamente'}
    return HttpResponse(JsonResponse(salida))


def loguear_manager(request):
    salida = {}
    if request.method == 'POST' and request.is_ajax():
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        if username1 and password1:
            try:
                get_user = User.objects.get(username=username1)
                get_password = get_user.password
                if check_password(password1, get_password):
                    if Manager.objects.filter(user_id=get_user.id).exists():
                        user = authenticate(username=username1, password=password1)
                        login(request, user)
                        salida = {'success': True, 'msj': 'exito'}
                    else:
                        salida = {'error': True, 'msj': 'La cuenta con la que quieres ingresar no esta registrada como manager'}
                else:
                    salida = {'error': True, 'msj': 'Contraseña incorrecta'}
            except  User.DoesNotExist:
                salida = {'error': True, 'msj': 'Ese usuario no existe en nuestra base de datos'}
        else:
            salida = {'error': True, 'msj': 'Por favor completa los campos correctamente'}
    return HttpResponse(JsonResponse(salida))
