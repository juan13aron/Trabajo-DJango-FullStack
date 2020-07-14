from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from Empleado.models import Empleado, Pabellon, Evento, Artista, Diseñador, Desfile
from .forms import EmpleadoForm, PabellonForm, EventoForm, ArtistaForm, DiseñadorForm, DesfileForm
# Create your views here.
class ListEmpleados(generic.ListView):
    model=Empleado
    template_name="listar_empleados.html"
    context_object_name="emp"
class InsertarEmpleado(generic.CreateView):
    model=Empleado
    template_name="empleado_form.html"
    form_class=EmpleadoForm
    success_url=reverse_lazy("Empleado:listar_empleados")
class EditarEmpleado(generic.UpdateView):
    model=Empleado
    template_name="empleado_form.html"
    form_class=EmpleadoForm
    success_url=reverse_lazy("Empleado:listar_empleados")
class BorrarEmpleado(generic.DeleteView):
    model=Empleado
    template_name="borrar_empleado.html"
    context_object_name="emp"
    success_url=reverse_lazy("Empleado:listar_empleados")


class ListPabellones(generic.ListView):
    model=Pabellon
    template_name="listar_pabellones.html"
    context_object_name="pab"
class InsertarPabellon(generic.CreateView):
    model=Pabellon
    template_name="pabellon_form.html"
    form_class=PabellonForm
    success_url=reverse_lazy("Empleado:listar_pabellones")
class EditarPabellon(generic.UpdateView):
    model=Pabellon
    template_name="pabellon_form.html"
    form_class=PabellonForm
    success_url=reverse_lazy("Empleado:listar_pabellones")
class BorrarPabellon(generic.DeleteView):
    model=Pabellon
    template_name="borrar_pabellon.html"
    context_object_name="pab"
    success_url=reverse_lazy("Empleado:listar_pabellones")


class ListEventos(generic.ListView):
    model=Evento
    template_name="listar_eventos.html"
    context_object_name="eve"
class InsertarEvento(generic.CreateView):
    model=Evento
    template_name="evento_form.html"
    form_class=EventoForm
    success_url=reverse_lazy("Empleado:listar_eventos")
class EditarEvento(generic.UpdateView):
    model=Evento
    template_name="evento_form.html"
    form_class=EventoForm
    success_url=reverse_lazy("Empleado:listar_eventos")
class BorrarEvento(generic.DeleteView):
    model=Evento
    template_name="borrar_evento.html"
    context_object_name="eve"
    success_url=reverse_lazy("Empleado:listar_eventos")


class ListArtitas(generic.ListView):
    model=Artista
    template_name="listar_artistas.html"
    context_object_name="art"
class InsertarArtista(generic.CreateView):
    model=Artista
    template_name="artista_form.html"
    form_class=ArtistaForm
    success_url=reverse_lazy("Empleado:listar_artistas")
class EditarArtista(generic.UpdateView):
    model=Artista
    template_name="artista_form.html"
    form_class=ArtistaForm
    success_url=reverse_lazy("Empleado:listar_artistas")
class BorrarArtista(generic.DeleteView):
    model=Artista
    template_name="borrar_artista.html"
    context_object_name="art"
    success_url=reverse_lazy("Empleado:listar_artistas")


class ListDiseñadores(generic.ListView):
    model=Diseñador
    template_name="listar_diseñadores.html"
    context_object_name="dis"
class InsertarDiseñador(generic.CreateView):
    model=Diseñador
    template_name="diseñador_form.html"
    form_class=DiseñadorForm
    success_url=reverse_lazy("Empleado:listar_artistas")
class EditarDiseñador(generic.UpdateView):
    model=Diseñador
    template_name="diseñador_form.html"
    form_class=DiseñadorForm
    success_url=reverse_lazy("Empleado:listar_diseñadores")
class BorrarDiseñador(generic.DeleteView):
    model=Diseñador
    template_name="borrar_diseñador.html"
    context_object_name="dis"
    success_url=reverse_lazy("Empleado:listar_diseñadores")


class ListDesfiles(generic.ListView):
    model=Desfile
    template_name="listar_desfiles.html"
    context_object_name="des"
class InsertarDesfile(generic.CreateView):
    model=Desfile
    template_name="desfile_form.html"
    form_class=DesfileForm
    success_url=reverse_lazy("Empleado:listar_artistas")
class EditarDesfile(generic.UpdateView):
    model=Desfile
    template_name="desfile_form.html"
    form_class=DesfileForm
    success_url=reverse_lazy("Empleado:listar_desfiles")
class BorrarDesfile(generic.DeleteView):
    model=Desfile
    template_name="borrar_desfile.html"
    context_object_name="des"
    success_url=reverse_lazy("Empleado:listar_desfiles")