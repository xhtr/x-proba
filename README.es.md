# Rennty

## Para Empezar

Estas instrucciones le brindarán una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba. Consulte la implementación para ver las notas sobre cómo implementar el proyecto online.

### Pre-requisitos

Qué necesita para instalar el software y cómo instalarlo

- Docker Community Edition (Docker Engine Community)

  *e.g: Docker Desktop (Mac), Docker Desktop (Windows)*

  [https://docs.docker.com/install/](https://docs.docker.com/install/)

  **Es posible que deba crear una cuenta dockerhub para descargar docker**

### Instalación

Una serie paso a paso de ejemplos que le indican cómo ejecutar un entorno de desarrollo.

1. Utilizar `nginx-proxy`. Permite tener un load-balancer  en su computador con el puerto 80 abierto. La aplicación estará en el nginx-proxy.

  ```
  git clone git@github.com:sovanna/nginx-proxy.git \
  && cd nginx-proxy \
  && docker network create nginx-proxy \
  && docker-compose up -d
  ```

2. Actualice su archivo host (Ejemplo para MacOS)

  ```
  sudo vi /etc/hosts
  ```
  and put: `127.0.0.1 rennty-test.local`

  **Es necesario para tener acceso al proyecto en [http://rennty-test.local](http://rennty-test.local)**

3. Clonar el proyecto

  ```
  git clone git@github.com:Rennty/x-proba.git rennty-test \
  && cd rennty-test
  ```

5. Comienzo

  ```
  docker-compose up -d
  ```

### Verificación

La aplicación debe estar disponible, para verificar, puedes:

- ir a [http://rennty-test.local](http://rennty-test.local) y deberías ver un 404 Not Found

- `docker-compose logs -f server` debería darle una línea como Listening en: `http://0.0.0.0:8077`

- ir a [http://rennty-test.local/ping](http://rennty-test.local/ping) y deberías ver un `pong`


### Base de datos (postgres)

Por ahora, solo tenemos pocos modelos de datos descritos en el paquete. `sxmodel`. Puedes verlos, está relacionado con `User`.


Primero, inicie la migración de la base de datos. (este proyecto utiliza `Flask-migrate`)

- `docker-compose exec server flask db init`
- `docker-compose exec server flask db migrate`
- `docker-compose exec server flask db upgrade`


Ahora, tablas `user`, `profile`, `contact` debe ser agregado a `Postgres`.


## Ejercicios

Nota: vamos a utilizar **Flask** [http://flask.pocoo.org/docs/1.0/](http://flask.pocoo.org/docs/1.0/)

También puedes encontrar ayuda aquí. [the flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

**Primero, eche un vistazo a cada carpeta, archivos en el repositorio para ver los paquetes etc.. que este proyecto contiene.**

### Puedes hacer ejercicios en el siguiente orden por ejemplo: 1 / 4 / 2 / 5 / 3 / 6

### Cuando termine o quiera compartir, simplemente haga una pull-request

---

### 1 - Implementa código que permite crear un usuario. (focused on backend)

#### Guía

- Crear un endpoint en **index page** en lugar de ver `Not Found`

	Puede ver el código del backend en server/app/main/routes.py

	```
	- Necesitas crear una función y devolver una plantilla `index.html`
	- Copiar desde la función ping, hacer el cambio necesario.
	- consulte la documentación si no sabe cómo renderizar una plantilla html
	```

	**Consulte la documentación de flask para obtener ayuda.** [http://flask.pocoo.org/docs/1.0/](http://flask.pocoo.org/docs/1.0/)

- En la plantilla index.html, Pon un enlace que redirecciona a una página. `/auth/register`

	```
	utilizar para la función automática `url_for` en la plantilla para generar la URL

	ejemplo: <a href="{{ url_for('auth.register') }}">registrarse</a>
	```

- Crear una página vacía de register.html

- Cree un formulario de registro con solo el campo de inicio de sesión y contraseña en el backend

	Ver en [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/quickstart.html)

- Muestra el formulario en la página register.html.

	Ver en `{{ wtf.quick_form(form) }}` desde [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/forms.html)

- Completa la parte del backend para agregar un usuario.


	ejemplo:

	```
	from sxmodel.Users import User

	user = User(login=xx, password=xxx)
	```


**Puede consultar el pgadmin para ver si el usuario está bien registrado**
[http://localhost:8008/](http://localhost:8008/)
**No te olvides de agregar un servidor de pgadmin para conectar** (usar el archivo .env para las credenciales)

---

### 2 - Implementa un código que permite iniciar sesión a un usuario (enfocado en el backend)

#### Guía

Ver en [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)


---

### 3 - Perfeccionamiento

Haz los cambios necesarios que creas buenos, importantes o lógicos.

**Tips: url prefix, form validation, password encrypted, etc...**

---

### 4 - Frecuencias parte 1 (de adventofcode 2018)

Si vas a [http://rennty-test.local/frequencies](http://rennty-test.local/frequencies)

Verás **0**

Si abres el archivo en `server/app/main/frequencies.txt` verás una serie de cifras (positivo/negativo). Son frecuencias. Empezando desde 0, cuando veas **+1** significa **aumentado por 1**, cuando veas **-4**, significa **disminuido por 4**.

ejemplo :

```
comenzando con la frecuencia de 0

+1,
-2,
+3,
+1
```
**La frecuencia final será 3**

Empezó desde 0, ¿Cuál será la frecuencia final con los valores en? `frequencies.txt`.

---

### 5 - Frecuencias parte 2 (de adventofcode 2018)

Encuentra la primera frecuencia que llega dos veces.

ejemplo :

```
comenzando con la frecuencia de 0

+1,
-2,
+3,
+1
```

```
0 + 1 = 1
1 - 2 = -1
-1 + 3 = 2
2 + 1 = 3
AQUÍ, seguimos desde el principio.
3 + 1 = 4
4 - 2 = 2 (2 ya fue visto)
```

**Así que la primera frecuencia que se ve dos veces es 2.**

--- 

### 6 - BONO

Haz una LINDA página de inicio de sesión o registro usando **React** directamente en el .html page.

Así, sin completar frontend stack, **SOLO React**.
sin webpack, etc.