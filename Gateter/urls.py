"""Gateter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as av
# import de las vistas para las páginas que hemos creado
from Gateter.views import signup, home, users, maullido, logged, error404

# Definición de los paths de Django
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),                                             # url a sign up
    path('', home, name='home'),                                                        # url a home
    path('profile/<str:name>', users, name='user'),                                     # url a los perfiles de usuario
    path('maullido/', maullido, name="maullido"),                                       # url que salva maullidos
    path('login/', av.LoginView.as_view(template_name='login.html'), name='login'),     # url que lleva al login
    path('logout/', av.LogoutView.as_view(next_page='home'), name='logout'),            # url que lleva a logout
    path('logged/', logged, name='logged'),                                             # url que lleva a logout
    path('error404/', error404, name='error404'),                                       # url para la página de error
]
