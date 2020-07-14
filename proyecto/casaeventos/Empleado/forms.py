from django import forms
from .models import Empleado, Pabellon, Evento, Artista, Diseñador, Desfile
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=['nombre','apellido','correo','universidad','celular']
        labels={'nombre':'Ingese su nombre',
        'apellido':'Ingese su apellido',
        'correo':'Ingese su correo',
        'universidad':'Ingese su Univesidad engresada',
        'celular':'Ingese su numero celular', 
        }
        widget={
            'nombre':forms.TextInput(),
            'apellido':forms.TextInput(),
            'correo':forms.TextInput(),
            'universidad':forms.TextInput(),
            'nombre':forms.NumberInput(),
        }
        def __init__(self,*args,**kgwards):
            super().__init__(*args,**kgwards)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
class PabellonForm(forms.ModelForm):
    class Meta:
        model=Pabellon
        fields=['nombre','telefono','Empleado']
        labels={'nombre':'Ingrese el nombre',
        'telefono':'Ingrese el numero telefonico',
        'Empleado':'Selecione al Empleado',
        }
        widget={
            'nombre':forms.TextInput(),
            'telefono':forms.NumberInput(),
        }
        def __init__(self,*args,**kgwards):
            super().__init__(*args,**kgwards)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
class EventoForm(forms.ModelForm):
    class Meta:
        model=Evento
        fields=['nombre','fechaInicio','fechaFin','Empleado','presupuesto']
        labels={'nombre':'Ingrese el nombre',
        'fechaInicio':'Ingrese La fecha de inicio',
        'fechaFin':'Ingrese la fecha de finalizacion',
        'Empleado':'Selecione el Empleado',
        'presupuesto':'Ingrese el presupuesto',
        }
        widget={
            'nombre':forms.TextInput(),
            'fechaInicio':forms.DateInput(),
            'fechaFin':forms.DateInput(),
            'presupuesto':forms.NumberInput(),

        }
        def __init__(self,*args,**kgwards):
            super().__init__(*args,**kgwards)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
class ArtistaForm(forms.ModelForm):
    class Meta:
        model=Artista
        fields=['nombre','generoMusical','rol']
        labels={'nombre':'Ingrese el nombre',
        'generoMusical':'Ingrese el Genero Musical',
        'rol':'Ingrese el rol del Artista',
        }
        widget={
            'nombre':forms.TextInput(),
            'generoMusical':forms.TextInput(),
            'rol':forms.TextInput(),
        }
class DiseñadorForm(forms.ModelForm):
    class Meta:
        model=Diseñador
        fields=['nombre','pasaporte','paisOrigen']
        labels={'nombre':'Ingrese el nombre',
        'pasaporte':'Ingrese el numero de pasaporte',
        'paisOrigen':'Ingrese el pais de origen',
        }
        widget={
            'nombre':forms.TextInput(),
            'pasaporte':forms.NumberInput(),
            'paisOrigen':forms.TextInput(),
        }
class DesfileForm(forms.ModelForm):
    class Meta:
        model=Desfile
        fields=['nombre','fecha','coleccion','Artista','Diseñador']
        labels={'nombre':'Ingrese el nombre',
        'fecha':'Ingrese la fecha',
        'coleccion':'Ingrese el nombre de la coleccion',
        'Artista':'Selecione al artista',
        'Diseñador':'Selecione al diseñador',
        }
        widget={
            'nombre':forms.TextInput(),
            'fecha':forms.DateInput(),
            'coleccion':forms.TextInput(),
        }
        def __init__(self,*args,**kgwards):
            super().__init__(*args,**kgwards)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

