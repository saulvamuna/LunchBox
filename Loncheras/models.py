from django.db import models


class Usuario(models.Model):
    Usuario = models.CharField(max_length=20)
    Clave = models.IntegerField()
    FotoUsuario = models.CharField(max_length=255)
    Rol = models.IntegerField()

    class Meta:
        db_table = "Usuario"


class Estudiante(models.Model):
    N_identidad = models.AutoField(primary_key=True)
    T_identidad = models.CharField(max_length=21)
    Nombres = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=30)
    Fecha_nacimiento = models.DateField()
    Edad = models.IntegerField()
    Grado = models.CharField(max_length=10)
    Estado = models.CharField(max_length=10)
    F_ingreso = models.TimeField()
    FotoEstudiante = models.CharField(max_length=255)
    Usuario_Id = models.IntegerField()

    class Meta:
        db_table = "Estudiante"
