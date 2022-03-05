# Imports necesarios para hacer login, autentificarse, Crear un Formulario de registro.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Imports para presentar la plantilla y para redirigir a otra página en caso necesario
from django.shortcuts import render, redirect
from Gateter.models import Miau
from django.contrib.auth.models import User
# Import para usar fechas en concreto para darle a los miaus la fecha actual
import datetime


# Primera view según viene en el documento: Registro. Contiene las cajas para introducir Usuario y contraseña con
# confirmación de usuario.
def signup(request):
    # Si ya hemos rellenado el formulario
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Comprobamos que el formulario es válido
        if form.is_valid():
            # Salvamos
            form.save()
            # Obtenemos los datos del formulario
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Autentificamos
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Enviamos al usuario a la página principal
            response = redirect('/profile/' + request.user.username)
        else:
            # Si no es valido devolvemos los errores
            response = render(request, 'signup.html', {'form': form})
    else:
        # Si es la primera vez que estamos en la web
        form = UserCreationForm()
        response = render(request, 'signup.html', {'form': form})
    # Devolvemos la plantilla signup.html donde le pasamos los valores creados por UserCreationForm() ya sea vacío o con
    # los errores que haya encontrado el registro
    return response


# Segunda página que solicita el documento: página principal. Debera mostrar los 10 últimos mensajes ordenados de más
# nuevo a más antiguo
def home(request):
    # Para la página principal solo necesitamos rellenar la plantilla con los últimos diez maullidos
    context = {
        'miaus': Miau.objects.order_by('-fecha')[:10]
    }

    return render(request, 'home.html', context)


# Tercera página que solicita el documento: página de usuarios. Debe mostrar el listado de maullidos del usuario de
# más nuevo a más antiguo, si el usuario es el mismo que está identificado una caja para escribir maullidos y si el
# usuario no existe debe mostrar una página de error
def users(request, name=None):
    # Comprobamos si el usuario que hace la petición es el mismo que pide su perfil
    if name is None:
        user = request.user
    else:
        # Probamos si el usuario pasado por parámetro existe o tenemos que enseñar una página de error
        try:
            user = User.objects.get(username=name)
        except User.DoesNotExist:
            return error404(request)

    # Creamos el contexto para enviarlo a la plantilla que procesará los maullidos del usuario ordenados por fecha
    # del más nuevo al más antiguo
    context = {
        'name': user.username,
        'miaus': user.miau_set.all().order_by('-fecha')
    } 

    return render(request, 'user.html', context)


# En la tercera página se solicita que si el usuario es el mismo que está identificado haya una caja para escribir
# maullidos esta función salva el maullido en la base de datos y recarga la página del usuario
def maullido(request):
    # Miramos si hay contenido y si no lo hay volvemos sin hacer nada
    try:
        content = request.POST['content']
    except KeyError:
        return redirect('/profile/' + request.user.username)
    # Si hay maullido creamos la petición para guardarla en la base de datos
    m = Miau.objects.create(
        user=request.user,
        fecha=datetime.datetime.now(),
        contenido=content,
    )
    # Y una vez formateada la guardamos
    m.save()

    # Y volvemos a la página de perfil actualizada con el nuevo maullido
    return redirect('/profile/' + request.user.username)


# Redirección para que una vez ingrese el usuario vaya a su propia página
def logged(request):
    return redirect('/profile/' + request.user.username)


# Redirección para que se informe al no existir el usuario
def error404(request):
    response = render(request, 'error404.html')
    response.status_code = 404
    return response
