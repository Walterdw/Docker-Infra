############################################################################################
####################################### base ###############################################
############################################################################################

# Se utiliza la imagen de python:3.10 como base para todos los contenedores que lo necesiten
# Ya que istea-api, istea-worker-redis y istea-worker-mongo tienen los mismos requisitos de
# instalación de paquetes, dependencias de python, etc.
# Esta es una mejora que aplique para ahorrar lineas de codigo en el Dockerfile.

# Selecionando la imagen de python:3.10 como base para estos contenedores
FROM python:3.10 as base

# Definiendo las variables de entorno correspondientes
ENV PYTHONUNBUFFERED=1
# Con la siguiente variable de entorno se evita que se abra una ventana de dialogo
ENV DEBIAN_FRONTEND=noninteractive

# Definiendo el directorio de trabajo de la aplicacion
WORKDIR /app
 
# Actualizando e instalando los paquetes necesarios
RUN apt-get update \
    && apt-get install -y python3-dev \
                            python3-urllib3 \
                            unrar-free

# Instalando las dependencias de python
RUN pip install --upgrade pip \
    && pip install --upgrade -r requirements.txt

#############################################################################################
###################################### istea-redis ##########################################
#############################################################################################

# IMPORTANTE:
# No se utliza esta imagen, se utiliza la imagen de redis:alpine en el docker-compose.yml
# Esta creada unicamente para cumplir con el requerimiento del examen.

FROM redis:latest as istea-redis