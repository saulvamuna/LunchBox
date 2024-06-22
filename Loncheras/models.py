from django.db import models


class Rol(models.Model):
    Id_rol = models.IntegerField(primary_key=True)
    Nombre_rol = models.CharField(max_length=20)

    class Meta:
        db_table = "Rol"


class Usuario(models.Model):
    Usuario = models.CharField(max_length=20)
    Clave = models.IntegerField()
    FotoUsuario = models.CharField(max_length=255)
    Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

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


class Reconocimiento(models.Model):
    Id_reconocimiento = models.IntegerField(primary_key=True)
    Fecha = models.TimeField()
    Biometria = models.CharField(max_length=40)

    class Meta:
        db_table = "Reconocimiento"


class Estu_Reco(models.Model):
    N_identidad = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Id_reconocimiento = models.ForeignKey(Reconocimiento, on_delete=models.CASCADE)

    class Meta:
        db_table = "Estu_Reco"


class Dieta(models.Model):
    Id_dieta = models.IntegerField(primary_key=True)
    Dieta = models.CharField(max_length=255)
    Especificaciones = models.CharField(max_length=60)
    Feche_entrega = models.TimeField()

    class Meta:
        db_table = "Dieta"


class Restaurante(models.Model):
    Id_sede = models.IntegerField(primary_key=True)
    Nombre_encargado = models.CharField(max_length=30)
    N_encargado = models.IntegerField()

    class Meta:
        db_table = "Restaurante"


class Producto(models.Model):
    Id_producto = models.IntegerField(primary_key=True)
    Nombre_producto = models.CharField(max_length=20)
    Cantidad_p = models.IntegerField()
    Fecha_compra = models.TimeField()
    Fecha_caducidad = models.DateField()
    Tipo_p = models.CharField(max_length=40)
    Id_sede = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    class Meta:
        db_table = "Producto"


class Pro_Dieta(models.Model):
    Id_dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)
    Id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        db_table = "Pro_Dieta"
