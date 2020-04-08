from django.urls import path
from usuarios import views
from .views import registrar, index, loguearse, manager_form, registrar_manager, loguear_manager, index_manager
from django.contrib.auth.decorators import login_required
from resto.decorators import manager_required
app_name = 'usuario'

urlpatterns = [
    path('index/', login_required(views.index), name='index'),
    path('registrar/', views.registrar, name='registrarse'),
    path('loguearse/', views.loguearse, name='loguearse'),
    path('manager/', views.manager_form, name='registrar_m_form'),
    path('registrarmanager/', views.registrar_manager, name='registrar_manager'),
    path('loguearmanager/', views.loguear_manager, name='loguear_manager'),
    path('manager_inicio/', manager_required(views.index_manager), name='index_manager'),
]
