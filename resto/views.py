from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from .models import Restaurante, Categoria, Plato, Imagen, ReviewRestaurante, ReviewPlato
from usuarios.models import Manager
from .forms import EditarForm
from django.db.models import Avg

def home(request):
    restaurantes = sorted(Restaurante.objects.all()[:4], key=lambda t: t.average_rating, reverse=True)
    platos = sorted(Plato.objects.all()[:4], key=lambda t: t.average, reverse=True)
    contexto = {'restaurantes': restaurantes, 'platos': platos}
    return render(request, 'resto/index.html', contexto)

def registrar_resto(request):
    salida = {}
    if request.method == 'POST' and request.is_ajax():

        nombre_ = request.POST.get('nombre')
        descripcion_ = request.POST.get('descripcion')
        direccion_ = request.POST.get('direccion')
        apertura_ = request.POST.get('apertura')
        cierre_ = request.POST.get('cierre')
        imagen_ = request.FILES.get('imagen')

        if nombre_ and descripcion_ and direccion_ and apertura_ and cierre_ and imagen_:
            resto = Restaurante.objects.create(nombre=nombre_, descripcion=descripcion_, direccion=direccion_, imagen_principal=imagen_, apertura=apertura_, cierre=cierre_)
            resto.save()
            try:
                manager = Manager.objects.get(user_id=request.user.id)
                manager.restaurante_id = resto.id
                manager.save()
                salida = {'success': True, 'msj': 'exito'}
            except Manager.DoesNotExist:
                salida = {'error': True, 'msj': 'Cuenta de manager inexistente'}
        else:
            salida = {'error': True, 'msj': 'Por favor llena los campos correctamente'}
    return HttpResponse(JsonResponse(salida))


def subir_img(request):
    imagenes = request.FILES.getlist('imagenes')
    if imagenes:
        try:
            manager = Manager.objects.get(user_id=request.user.id)
            restaurante_ = Restaurante.objects.get(id=manager.restaurante_id)
            for file_ in imagenes:
                resto_imagenes = Imagen.objects.create(restaurante=restaurante_, imagen=file_)
                resto_imagenes.save()
        except Manager.DoesNotExist:
            raise Http404('Cuenta de manager inexistente')
    return redirect('usuario:index_manager')


def subir_comida(request):
    salida = {}

    if request.method == 'POST' and request.is_ajax():
        nombre_ = request.POST.get('nombre')
        categoria_ = request.POST.get('categoria')
        descripcion_ = request.POST.get('texto')
        imagen_ = request.FILES.get('docfile')
        
        if nombre_ and categoria_ and imagen_ and descripcion_:
            cat_ = Categoria.objects.get(nombre=categoria_)
            comida = Plato.objects.create(nombre=nombre_, categoria_id=cat_.id, descripcion=descripcion_, imagen=imagen_)
            comida.save()
            try:
                manager = Manager.objects.get(user_id=request.user.id)
                restaurante = Restaurante.objects.get(id=manager.restaurante_id)
                restaurante.platos.add(comida)
                restaurante.save()
                salida = {'success': True, 'msj': 'Comida agregada exitosamente'}
            except Manager.DoesNotExist:
                salida = {'error': True, 'msj': 'Cuenta de manager no encontrada'}
        else:
            salida = {'error': True, 'msj': 'Por favor completa los campos correctamante'}
    return HttpResponse(JsonResponse(salida))

def eliminar_comida(request, id):
    salida = {}
    comida = Plato.objects.get(id=id)
    if request.method == 'POST':
        comida.delete()
        salida = {'success': True, 'msj': 'eliminado'}
    return HttpResponse(JsonResponse(salida))


def post_editar(request, id):
    if request.method == 'GET':
        objeto = get_object_or_404(Plato, id=id)
        form = EditarForm(instance=objeto)
        categorias = Categoria.objects.all()
        context = {'form': form, 'categorias': categorias, 'objeto': objeto}
    return render(request, 'resto/modal.html', context)

def editar_comida(request, id):
    comida = Plato.objects.get(id=id)
    if request.method == 'POST':
        form = EditarForm(request.POST, request.FILES, instance=comida)
        if form.is_valid():
            form.save()
    return redirect('usuario:index_manager')

def busqueda(request):
    filtrado = request.GET.get('filtrado')
    opciones = request.GET.get('opciones')
    resto = False
    if request.method == 'GET':
        if opciones == '1':
            platos = Plato.objects.filter(nombre__icontains=filtrado)
            contexto = {'objetos': platos, 'filtrar': filtrado, 'opcion': opciones}
        elif opciones == '2':
            restaurantes = Restaurante.objects.filter(nombre__icontains=filtrado)
            resto = True
            contexto = {'objetos': restaurantes, 'resto': resto, 'filtrar': filtrado, 'opcion': opciones}
    return render(request, 'resto/resultados.html', contexto)

def ordenar_busqueda(request):
    filtrado = request.GET.get('filtrado2')
    opciones = request.GET.get('opciones2')
    resto = False

    if request.method == 'GET':
        if opciones == '1':
            platos = sorted(Plato.objects.filter(nombre__icontains=filtrado), reverse=True, key=lambda t: t.average)
            contexto = {'objetos': platos}
        elif opciones == '2':
            restaurantes = sorted(Restaurante.objects.filter(nombre__icontains=filtrado), reverse=True, key=lambda t: t.average_rating)
            resto = True
            contexto = {'objetos': restaurantes, 'resto': resto}
    return render(request, 'resto/resultados.html', contexto)


def resto_detalles(request, id):
    try:
        resto = Restaurante.objects.get(pk=id)
        imagenes = Imagen.objects.filter(restaurante=resto.id)
        comentarios = ReviewRestaurante.objects.filter(restaurante=resto.id)
        promedio = comentarios.aggregate(average_rating=(Avg('calificacion')))
        contexto = {
            'resto': resto,
            'imagenes': imagenes,
            'comentarios': comentarios,
            'promedio': promedio
        }
        return render(request, 'resto/restaurante.html', contexto)
    except Restaurante.DoesNotExist:
        raise Http404('El restaurante no existe')


def comentar(request, id):
    salida = {}
    if request.method == 'POST' and request.is_ajax():
        texto = request.POST.get('texto')
        calificacion = request.POST.get('rating_value')
        if texto and calificacion:
            try:
                resto = Restaurante.objects.get(id=id)
                date = timezone.now()
                comentario = ReviewRestaurante.objects.create(user=request.user, restaurante=resto, fecha=date, texto=texto, calificacion=calificacion)
                comentario.save()
                comentario_user = []
                datos = {}
                name = request.user.username
                datos['user'] = name
                datos['texto'] = comentario.texto
                datos['calificacion'] = comentario.calificacion
                datos['fecha'] = date
                comentario_user.append(datos)
                salida = {'success': True, 'objeto': comentario_user}
            except Restaurante.DoesNotExist:
                salida = {'error': True, 'msj': 'Hubo un error, intenta mas tarde'}
        else:
            salida = {'error': True, 'msj': 'Por favor llena los campos correctamente'}
    return HttpResponse(JsonResponse(salida))

def plato_detalles(request, id):
    try:
        plato = Plato.objects.get(pk=id)
        comentarios = ReviewPlato.objects.filter(plato=plato.id)
        promedio = comentarios.aggregate(average_rating=(Avg('calificacion')))
        contexto = {
            'plato': plato,
            'comentarios': comentarios,
            'promedio': promedio
        }
        return render(request, 'resto/plato.html', contexto)
    except Plato.DoesNotExist:
        raise Http404('El plato no existe')

def comentar_plato(request, id):
    salida = {}
    if request.method == 'POST' and request.is_ajax():
        texto = request.POST.get('texto2')
        calificacion = request.POST.get('rating_value2')
        if texto and calificacion:
            try:
                plato = Plato.objects.get(id=id)
                date = timezone.now()
                comentario = ReviewPlato.objects.create(user=request.user, plato=plato, fecha=date, texto=texto, calificacion=calificacion)
                comentario.save()
                comentario_user = []
                datos = {}
                name = request.user.username
                datos['user'] = name
                datos['texto'] = comentario.texto
                datos['calificacion'] = comentario.calificacion
                datos['fecha'] = date
                comentario_user.append(datos)
                salida = {'success': True, 'objeto': comentario_user}
            except Plato.DoesNotExist:
                salida = {'error': True, 'msj': 'Hubo un error, intenta mas tarde'}
        else:
            salida = {'error': True, 'msj': 'Por favor llena los campos correctamente'}
    return HttpResponse(JsonResponse(salida))

