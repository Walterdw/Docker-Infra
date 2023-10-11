# Examen Docker & Docker Compose

## Parámetros de corrección
### Examen Práctico 
~~~
1) Premisa: Armar contenedor funcional de Istea-Api
   Puntaje: 0.75
2) Premisa: Armar contenedor funcional para Istea Worker-Redis e Istea-Worker-Mongo
   Puntaje: 1.50
3) Premisa: Armar contenedor funcional de Istea-Redis
   Puntaje: 0.75
4) Premisa: Armar docker-compose integrando todos los servicios
   Puntaje: 2

Total Práctica: 5 puntos
~~~
### Adicional
~~~
5) Premisa: Documentación de los pasos a seguir y posibles mejoras
   Puntaje: 0.5 a 2 puntos
~~~
### Examen Teórico
~~~

Premisa: 3 preguntas a responder, pueden ser consultas sobre mejoras, troubleshooting o una explicación sobre algún comando/flag utilizado
Puntaje: 1 por pregunta

Total Teoría: 3 puntos
~~~
# Ejercicios:

### 1) Istea-api

~~~
a) Usar la imagen python:3.10
b) Se necesita agregar la variable de entorno PYTHONUNBUFFERED=1 para enviar el stdout a la terminal
c) El directorio de trabajo debe ser /app
d) Los siguientes paquetes tienen que ser instalados utilizando apt-get: - python3-dev
                                                                         - python3-urllib3
                                                                         - unrar-free
e) Se debe agregar el contenido entero de la carpeta src en el directorio de trabajo /app
f) Se debe ejecutar el comando "pip install --upgrade pip && pip install --upgrade -r requirements.txt" para instalar las dependencias necesarias de python
g) El contenedor debe ejecutar en su inicio "flask run --host 0.0.0.0 --port 80 --debug"
~~~

#### b) Se tienen que agregar los archivos de configuración en las siguientes rutas:

~~~
Carpeta Local: AppCode/api/src
Carpeta en contenedor: /app
~~~

#### c) El workdir debe ser la ruta donde se encuentra la aplicación de python


### 2) Istea-worker-redis:

~~~
a) Usar la imagen python:3.10
b) Se necesita agregar la variable de entorno PYTHONUNBUFFERED=1 para enviar el stdout a la terminal
c) El directorio de trabajo debe ser /app
d) Los siguientes paquetes tienen que ser instalados utilizando apt-get: - python3-dev
                                                                         - python3-urllib3
                                                                         - unrar-free
e) Se debe agregar el contenido entero de la carpeta src en el directorio de trabajo /app
f) Se debe ejecutar el comando "pip install --upgrade pip && pip install --upgrade -r requirements.txt" para instalar las dependencias necesarias de python
g) El contenedor debe ejecutar en su inicio "python3 __init__.py initRedis"
~~~


#### b) Se tienen que agregar los archivos de configuración en las siguientes rutas:

~~~
Carpeta Local: AppCode/worker/src
Carpeta en contenedor: /app
~~~

#### c) El workdir debe ser la ruta donde se encuentra la aplicación de python

### 2) Istea-worker-mongo:

~~~
a) Usar la imagen python:3.10
b) Se necesita agregar la variable de entorno PYTHONUNBUFFERED=1 para enviar el stdout a la terminal
c) El directorio de trabajo debe ser /app
d) Los siguientes paquetes tienen que ser instalados utilizando apt-get: - python3-dev
                                                                         - python3-urllib3
                                                                         - unrar-free
e) Se debe agregar el contenido entero de la carpeta src en el directorio de trabajo /app
f) Se debe ejecutar el comando "pip install --upgrade pip && pip install --upgrade -r requirements.txt" para instalar las dependencias necesarias de python
g) El contenedor debe ejecutar en su inicio "python3 __init__.py initMongo"
~~~


#### b) Se tienen que agregar los archivos de configuración en las siguientes rutas:

~~~
Carpeta Local: AppCode/worker/src
Carpeta en contenedor: /app
~~~

#### c) El workdir debe ser la ruta donde se encuentra la aplicación de python

### 3) Istea-Redis:

#### a) Se debe usar la imagen redis:latest

#### b) Se tienen que agregar los archivos de configuración en las siguientes rutas:
~~~
Archivo en local: AppCode/redis/redis.conf
Archivo en contenedor: /usr/local/etc/redis/redis.conf
~~~

### 4) Docker-compose:

#### a) Tiene que haber 6 servicios creados:

~~~
Istea-api: 
    imagen: se debe buildear
    puertos: tiene que exponer el puerto 80 del contenedor en un puerto a elección del host
    variables_generales: Tiene que utilizar las variables definidas abajo
    healthcheck: definir el siguiente comando: ["CMD", "wget", "--tries=1", "--spider", "http://localhost:80/tech"]
    Servicios a conectar: redis, mongo
    Depende de: istea-worker-redis (Sin conditions)
~~~
~~~
Istea-worker-redis: 
    imagen: se debe buildear
    variables_generales: Tiene que utilizar las variables definidas abajo
    healthcheck: No posee
    Restart: no
    Servicios a conectar: redis
    Depende de: istea-redis
~~~
~~~
Istea-worker-mongo: 
    imagen: se debe buildear
    variables_generales: Tiene que utilizar las variables definidas abajo
    Restart: no
    healthcheck: No posee
    Servicios a conectar: mongo
    Depende de: istea-mongodb
~~~
~~~    
Istea-redis: 
    imagen: utilizar imagen redis:alpine
    variables_generales: Tiene que utilizar las variables definidas abajo
    healthcheck: definir el siguiente comando: "CMD-SHELL", "redis-cli -a ${REDIS_PASSWORD} ping"
~~~
~~~    
Istea-mongodb: 
    imagen: utilizar imagen mongo
    variables_generales: Tiene que utilizar las variables definidas abajo
    healthcheck: definir el siguiente comando: ["CMD","mongosh", "--eval", "db.adminCommand('ping')"]
~~~
~~~    
Istea-mongoui: 
    imagen: utilizar imagen mongo-express
    variables_generales: Tiene que utilizar las variables definidas abajo
    Servicios a conectar: mongo
    Depende de: mongo
    healthcheck: No posee
~~~

#### b) Generar una red que interconecte todos los servicios

##### Variables generales a definir
~~~
MONGO_USER=root
MONGO_PASS=example
MONGO_HOST=istea-mongodb
MONGO_DB=istea
MONGO_COLLECTION=examen
REDIS_PASS=YjtfdLD6arl3rL3h
REDIS_HOST=istea-redis
~~~

##### Variables para istea-redis
~~~
REDIS_REPLICATION_MODE: master
REDIS_PASSWORD: YjtfdLD6arl3rL3h
~~~

##### Variables para istea-mongodb
~~~
MONGO_INITDB_ROOT_USERNAME: root
MONGO_INITDB_ROOT_PASSWORD: example
~~~

##### Variables para istea-mongoui
~~~
ME_CONFIG_MONGODB_ADMINUSERNAME: root
ME_CONFIG_MONGODB_ADMINPASSWORD: example
ME_CONFIG_MONGODB_SERVER: istea-mongodb
ME_CONFIG_MONGODB_URL: mongodb://root:example@istea-mongodb:27017/
ME_CONFIG_BASICAUTH_USERNAME: "admin"
ME_CONFIG_BASICAUTH_PASSWORD: "password"
~~~

### Datos importantes:

##### a) Se puede probar el servicio de api ingresando en localhost:80/tech y debería mostrar un mensaje diciendo "Ok"

##### b) Se puede probar la conexión de api con redis ingresando en localhost:80/tech/redis y debería mostrar un mensaje diciendo las credenciales de mongodb

##### c) Se puede probar la conexión de api con mongo ingresando en localhost:80/tech/mongo y debería mostrar los resultados de la tabla istea.examen de documentdb

##### d) Se puede utilizar el contenedor Istea-mongogui para conectarse a traves de localhost:8081 y de esta manera ver si se crearon las bases de datos y los documentos correspondientes en mongodb