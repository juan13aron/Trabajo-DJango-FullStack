from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(
        max_length=40,
    )
    apellido=models.CharField(
        max_length=40,
    )
    correo=models.CharField(
        max_length=50,
    )
    universidad=models.CharField(
        max_length=50,
    )
    celular=models.IntegerField(

    )
    def __str__(self):
        return self.apellido + " " +self.nombre
    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.universidad = self.universidad.upper()
        super(Empleado,self).save()
    class Meta:
        verbose_name_plural="Empleados"

class Pabellon(models.Model):
    nombre=models.CharField(
        max_length=50,
    )
    telefono=models.IntegerField(

    )
    Empleado=models.ForeignKey(
        Empleado, 
        on_delete=models.CASCADE
    )
    def __str__(self):
        return '{}:{}'.format(Pabellon, self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(Pabellon,self).save()
    class Meta:
        verbose_name_plural="Pabellones"

class Evento(models.Model):
    nombre=models.CharField(
        max_length=50,
    )
    fechaInicio=models.DateTimeField(

    )
    fechaFin=models.DateTimeField(

    )
    Empleado=models.ForeignKey(
        Empleado, 
        on_delete=models.CASCADE
    )
    presupuesto=models.IntegerField(

    )
    def __str__(self):
        return '{}:{}'.format(Evento, self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(Evento,self).save()
    class Meta:
        verbose_name_plural="Eventos"

class Artista(models.Model):
    nombre=models.CharField(
        max_length=50,
    )
    generoMusical=models.CharField(
        max_length=30,
    )
    rol=models.CharField(
        max_length=10,
    )
    def __str__(self):
        return '{}:{}'.format(Artista, self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(Artista,self).save()
    class Meta:
        verbose_name_plural="Artistas"

class Diseñador(models.Model):
    nombre=models.CharField(
        max_length=50,
    )
    pasaporte=models.IntegerField(
        
    )
    paisOrigen=models.CharField(
        max_length=50,
    )
    def __str__(self):
        return '{}:{}'.format(Diseñador, self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(Diseñador,self).save()
    class Meta:
        verbose_name_plural="Diseñadores"

class Desfile(models.Model):
    nombre=models.CharField(
        max_length=50,
    )
    fecha=models.DateTimeField(

    )
    coleccion=models.CharField(
        max_length=50,
    )
    Artista=models.ForeignKey(
        Artista, 
        on_delete=models.CASCADE
    )
    Diseñador=models.ForeignKey(
        Diseñador, 
        on_delete=models.CASCADE
    )
    def __str__(self):
        return '{}:{}'.format(Desfile, self.nombre)
    def save(self):
        self.nombre = self.nombre.upper()
        super(Desfile,self).save()
    class Meta:
        verbose_name_plural="Desfiles"