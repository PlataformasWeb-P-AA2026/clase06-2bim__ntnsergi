from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.correo)

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)

class TipoDireccion(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.tipo)

class Direccion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="direcciones")
    tipo_direccion = models.ForeignKey(TipoDireccion, on_delete=models.CASCADE, related_name="direcciones")
    direccion = models.TextField()

    def __str__(self):
        return "%s %s %s" % (self.estudiante, self.tipo_direccion, self.direccion)