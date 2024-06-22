from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from Loncheras.models import Usuario, Estudiante
from django.contrib import messages
from django.db import connection
from django.core.files.storage import FileSystemStorage


def inicio(request):
    return render(request, "inicio.html")


# region Usuario


def listadousuario(request):
    usuario = Usuario.objects.all()
    return render(request, "Usuario/ListadoUsuario.html", {"usuario": usuario})


def registrarse(request):
    if request.method == "POST":
        if (
            request.POST.get("Usuario")
            and request.POST.get("Clave")
            and request.FILES["FotoUsuario"]
            and request.POST.get("Rol")
        ):
            User = Usuario()
            User.Usuario = request.POST.get("Usuario")
            User.Clave = request.POST.get("Clave")
            User.FotoUsuario = request.FILES["FotoUsuario"]
            User.Rol = request.POST.get("Rol")
            imagen = FileSystemStorage()
            imagen.save(User.FotoUsuario.name, User.FotoUsuario)
            insertar = connection.cursor()
            insertar.execute(
                "call Registrarse('"
                + User.Usuario
                + "','"
                + User.Clave
                + "','"
                + User.FotoUsuario.name
                + "','"
                + User.Rol
                + "')"
            )
        messages.success(
            request, "El usuario: " + User.Usuario + " fue guardado con exito "
        )
        return render(request, "Estudiante/TablaEstudiante.html")
    else:
        return render(request, "Accounts/registro.html")


def borrarusuario(request, Id):
    # ORM Django estamos consultano la variale que deseo
    usuario = Usuario.objects.get(Id=Id)
    usuario.delete()
    return redirect("/Usuario")


# endregion


# region Estudiante


def tblestudiante(request):
    estudiante = Estudiante.objects.all()
    return render(
        request, "Estudiante/TablaEstudiante.html", {"estudiante": estudiante}
    )


def registroestudiante(request):
    if request.method == "POST":
        if (
            request.POST.get("Nombres")
            and request.POST.get("Apellidos")
            and request.POST.get("Grado")
            and request.POST.get("Fecha_nacimiento")
            and request.POST.get("N_identidad")
            and request.POST.get("T_identidad")
            and request.POST.get("Usuario_Id")
        ):
            estudiante = Estudiante()
            estudiante.Nombres = request.POST.get("Nombres")
            estudiante.Apellidos = request.POST.get("Apellidos")
            estudiante.Grado = request.POST.get("Grado")
            estudiante.Fecha_nacimiento = request.POST.get("Fecha_nacimiento")
            estudiante.N_identidad = request.POST.get("N_identidad")
            estudiante.T_identidad = request.POST.get("T_identidad")
            estudiante.Usuario_Id = request.POST.get("Usuario_Id")
            insertar = connection.cursor()
            insertar.execute(
                "call InsertarEstudiante('"
                + estudiante.Nombres
                + "','"
                + estudiante.Apellidos
                + "','"
                + estudiante.Grado
                + "','"
                + estudiante.Fecha_nacimiento
                + "','"
                + estudiante.N_identidad
                + "','"
                + estudiante.T_identidad
                + "','"
                + estudiante.Usuario_Id
                + "')"
            )
        messages.success(
            request, "El estudiante: " + estudiante.Nombres + " fue guardado con exito "
        )
        return render(request, "Estudiante/InsertarEstudiantes.html")
    else:
        return render(request, "Estudiante/InsertarEstudiantes.html")


def borrarestudiantes(request, N_identidad):
    # ORM Django estamos consultano la variale que deseo
    estudiante = Estudiante.objects.get(N_identidad=N_identidad)
    estudiante.delete()
    return redirect("/Estudiante")


# endregion
