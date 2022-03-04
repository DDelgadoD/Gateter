from django.contrib.auth.models import User
from django.db import models


# La clase auth_user nos la proporciona django en los modelos básicos, pero el texto que escriban los usuarios lo
# creamos con la clase Miau que será la que se llamará para crearlos.

class Miau(models.Model):
    # Creamos el retorno como unicode por si hay caracteres no ASCII
    def __unicode__(self):
        return self.contenido

    # EL maullido incluirá el usuario, la fecha y lo que el usuario quiera poner con un largo máximo de 140 caracteres
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    fecha = models.DateTimeField()
    contenido = models.CharField(max_length=140)

