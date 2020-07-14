from django.urls import include,path
from home.views import Home
from Empleado.views import ListEmpleados, InsertarEmpleado
from Empleado.views import EditarEmpleado, BorrarEmpleado, InsertarPabellon
from .views import ListPabellones, EditarPabellon, BorrarPabellon
from .views import InsertarEvento, ListEventos, EditarEvento, BorrarEvento, InsertarArtista, ListArtitas
from .views import EditarArtista, BorrarArtista, InsertarDiseñador, ListDiseñadores, EditarDiseñador, BorrarDiseñador
from .views import InsertarDesfile, ListDesfiles, EditarDesfile, BorrarDesfile
urlpatterns=[
    #Empleados
    path('empleados',ListEmpleados.as_view(),name='listar_empleados'),
    path('empleados/new',InsertarEmpleado.as_view(),name='insertar_empleados'),
    path('empleados/edit/<int:pk>',EditarEmpleado.as_view(),name='editar_empleados'),
    path('empleados/delete/<int:pk>',BorrarEmpleado.as_view(),name='eliminar_empleados'),

    #Pabellones
    path('pabellones',ListPabellones.as_view(),name='listar_pabellones'),
    path('pabellones/new',InsertarPabellon.as_view(),name='insertar_pabellones'),
    path('pabellones/edit/<int:pk>',EditarPabellon.as_view(),name='editar_pabellones'),
    path('pabellones/delete/<int:pk>',BorrarPabellon.as_view(),name='eliminar_pabellones'),

    #Eventos
    path('eventos',ListEventos.as_view(),name='listar_eventos'),
    path('eventos/new',InsertarEvento.as_view(),name='insertar_eventos'),
    path('eventos/edit/<int:pk>',EditarEvento.as_view(),name='editar_eventos'),
    path('eventos/delete/<int:pk>',BorrarEvento.as_view(),name='eliminar_eventos'),

    #Artistas
    path('artistas',ListArtitas.as_view(),name='listar_artistas'),
    path('artistas/new',InsertarArtista.as_view(),name='insertar_artistas'),
    path('artistas/edit/<int:pk>',EditarArtista.as_view(),name='editar_artistas'),
    path('artistas/delete/<int:pk>',BorrarArtista.as_view(),name='eliminar_artistas'),

    #Diseñadores
    path('diseñadores',ListDiseñadores.as_view(),name='listar_diseñadores'),
    path('diseñadores/new',InsertarDiseñador.as_view(),name='insertar_diseñadores'),
    path('diseñadores/edit/<int:pk>',EditarDiseñador.as_view(),name='editar_diseñadores'),
    path('diseñadores/delete/<int:pk>',BorrarDiseñador.as_view(),name='eliminar_diseñadores'),

    #Desfiles
    path('desfiles',ListDesfiles.as_view(),name='listar_desfiles'),
    path('desfiles/new',InsertarDesfile.as_view(),name='insertar_desfiles'),
    path('desfiles/edit/<int:pk>',EditarDesfile.as_view(),name='editar_desfiles'),
    path('desfiles/delete/<int:pk>',BorrarDesfile.as_view(),name='eliminar_desfiles'),
]