from django.urls import path
from resto import views

app_name = 'resto'

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_resto/', views.registrar_resto, name='registrar_resto'),
    path('subirimg/', views.subir_img, name='subir_img'),
    path('subircomida/', views.subir_comida, name='subir_comida'),
    path('<int:id>/eliminar/', views.eliminar_comida, name='eliminar_comida'),
    path('<int:id>/editar_form/', views.post_editar, name='editar_comida_form'),
    path('<int:id>/editar/', views.editar_comida, name='editar'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('ordenarbusqueda/', views.ordenar_busqueda, name='ordenar_busqueda'),
    path('<int:id>/restaurante/', views.resto_detalles, name='resto_detalles'),
    path('<int:id>/comentar/', views.comentar, name='comentar'),
    path('detalles/<int:id>/', views.plato_detalles, name='plato_detalles'),
    path('<int:id>/comentar_plato/', views.comentar_plato, name='comentar_plato'),
]
