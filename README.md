# README #

Una pequeña documentación de los que hemos hecho:

He programado en Pycharm Community edition con un intérprete con Python 3.7 y para las pruebas he usado un entorno 
con python 3.9 y Django 3.2.3 en la página Pythonanywhere. 

La instalación de Django la he hecho para ver como se hace sin las automatizaciones de la página, pero a la hora de hacer 
las pruebas me resultaba más fácil usar la web para poder programar desde cualquier ordenador.

No creo que la instalación deba dar problemas en una version más actual de Django, pero en vez de hacer la instalación 
en local se puede usar la página: [Gateter](https://abaco.eu.pythonanywhere.com/)

En cuanto a la persistencia, he optado por sqlite3 que es el motor de base de datos por defecto de django, seguramente
por mi parte me hubiese sentido más cómodo con MySQL/MariaSQL que también es más potente, pero dado el tamaño de la
aplicación es poco relevante que motor lleve la base de datos.

He usado la parte CSS de bootstrap para dar formato a las plantillas, hago uso del CDN sin bajarlo por costumbre, pero
he visto que lo habitual es bajarlo para no tener problemas de conexión. No hago uso del JavaScript porque he querido 
hacer uso extensivo de las posibilidades de Django y no reinventar la rueda, aunque soy consciente que alguna cosa de 
las que he hecho no serán canónicas por el desconocimiento de todas las posibilidades del framework por la falta de 
tiempo para ahondar más en él.

Sobre los test, los he hecho a mano porque la aplicación no es demasiado complicada. He visto que Django tiene la 
capacidad de realizar test automatizados con la opción test, pero no me ha dado tiempo de profundizar en esta función.
Para los test, he creado tres usuarios User1, User2, User3 todos con contraseña "abaco2022" con los que he realizado la 
navegación y los maullidos para comprobar que todo funcionaba correctamente.
He querido que a la página de usuario se acceda a través de ".../profile/<Usuario>" por eso he tenido que escribir una 
redirección tras el logging.


## En views:
Simplemente he añadido una función para que se cargue dinámicamente cada una de las páginas que 
requiere el documento:

- signup(): función para la página de registro
- home(): función para la página principal 
- users(): función para la página de cada usuario
- maullidos(): función para salvar los maullidos de los usuarios
- logged(): función que redirecciona a la página del usuario al ingresar
- error404(): función que redirecciona a la página de usuario no encontrado

## En urls:
Simplemente he añadido el import de las funciones de view y he indicado el path. Aparte, he usado las views 
preexistentes de login y logout de las vistas incluidas en la biblioteca auth de django. 

## En plantillas:
He creado las siguientes plantillas:

- base.html: donde encontramos el header y el footer de la página
- error404.html: donde muestro una página 404 personalizada para indicar que un usuario no existe
- home.html: donde encontramos el contenido de la página principal
- login.html: donde se encuentra la página para el login.
- signup.html: donde encontramos el contenido de la página de registro
- user.html: donde se encuentra la página que se carga al pedir el perfil de usuario

## En media:
He creado esta carpeta para guardar las pocas imágenes que he añadido.

## En models:
He creado un único modelo: los Maullidos. La tabla será tal que así y podremos consultar como Gateter_miau:

| id  | user_id | fecha                      | contenido        |
|-----|---------|----------------------------|------------------|
| 1   | 8       | 2022-03-03 16:09:15.564754 | Primer Maullido  |
| 2   | 8       | 2022-03-03 16:09:30.612861 | Segundo Maullido |
| 3   | 8       | 2022-03-03 16:17:03.303415 | Tercer Maullido  |


## El texto Original de la Petición:
¡Buenas!

Somos Gateter. Tenemos un proyecto revolucionario, dinámico y totalmente
paradigmático que consiste en permitir a nuestros usuarios escribir mensajes
cortos en nuestra página, de 140 caracteres máximo, para que otros usuarios o
personas que nos visiten puedan ver los mensajes que ha escrito ese usuario,
listados de más reciente a más antiguo.

La página de registro deberá ser muy sencilla, el nuevo usuario deberá poner
su usuario y la contraseña que desee. Si el registro tiene éxito, este usuario
aparecerá automáticamente logueado en el sistema, con lo que podrá empezar
a compartir sus “maullidos”.

En la página principal o raíz se mostrarán los últimos 10 mensajes que se han
publicado en el sistema, sin diferenciar por usuario.

La página de un usuario mostrará el listado de sus maullidos, de más reciente a
más antiguo. En caso de que el usuario actual esté visitando su propia página,
se le mostrará en la parte superior la opción de añadir un nuevo mensaje.

Cualquier página de usuario puede ser consultada por cualquier usuario, no
hay páginas privadas. De forma que al acceder a cualquier página debería
mostrar los maullidos de ese usuario, o bien un mensaje de error comunicando
que no existe tal usuario.

### Requisitos:

- La aplicación ha de estar escrita en Python y Django como lenguaje de
servidor. Se puede utilizar cualquier librería tanto de Python como de
Django.
- El código de la aplicación debe ser original.
- En la parte de front-end se puede utilizar html, css y JavaScript. Se puede
utilizar cualquier librería de CSS y de JavaScript (Bootstrap, JQuery, etc.)
pero no frameworks.
- La aplicación debe tener persistencia. No hay requisito de qué motor
utilizar.
- La prueba está enfocada a valorar los conocimientos de backend. La
experiencia visual es siempre bien recibida, pero no es el objetivo final.
- No es necesario utilizar AJAX ni para el registro de usuario ni para postear
un nuevo “maullido”.

### A entregar:

- Código fuente completo.
- Un README.md con todas las instrucciones para ejecutar la aplicación.
- Dentro del README puedes incluir cualquier consideración o explicación
de decisión que hayas tomado.
- Cualquier otro fichero que consideres necesario agregar.