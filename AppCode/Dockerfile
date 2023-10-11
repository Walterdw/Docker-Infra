############################################################################################
###################################### istea-api ###########################################
############################################################################################

FROM python:3.10 as istea-api

# Defining Environment Variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Defining Work Directory
WORKDIR /app
 
# Update Repositories
RUN apt-get update \
    && apt-get install -y python3-dev \
                            python3-urllib3 \
                            unrar-free

# Copying Files
COPY /api/src /app

# Installing Python Dependencies
RUN pip install --upgrade pip \
    && pip install --upgrade -r requirements.txt


############################################################################################
#################################### istea-worker-redis ####################################
############################################################################################

FROM python:3.10 as istea-worker-redis

# Defining Environment Variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Defining Work Directory
WORKDIR /app

# Update Repositories
RUN apt-get update \
    && apt-get install -y python3-dev \
                            python3-urllib3 \
                            unrar-free

#Copying Files
COPY /worker/src /app

# Installing Python Dependencies
RUN pip install --upgrade pip \
    && pip install --upgrade -r requirements.txt

############################################################################################
#################################### istea-worker-mongo ####################################
############################################################################################

FROM python:3.10 as istea-worker-mongo

# Defining Environment Variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Defining Work Directory
WORKDIR /app

# Update Repositories
RUN apt-get update \
    && apt-get install -y python3-dev \
                            python3-urllib3 \
                            unrar-free

# Copying Files
COPY /worker/src /app

# Installing Python Dependencies
RUN pip install --upgrade pip \
    && pip install --upgrade -r requirements.txt

#############################################################################################
###################################### istea-redis ##########################################
#############################################################################################

FROM redis:latest as istea-redis

# Copying Files
COPY /redis/redis.conf /usr/local/etc/redis/redis.conf