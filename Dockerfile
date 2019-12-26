# this is the base image
FROM python:3.7-alpine
# maintainer is optional
MAINTAINER Arkady Futerman

# some juju about best practices when running python in a docker image
ENV PYTHONUNBUFFERED 1

# get requirements from repo over to the docker image
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# security stuff: set up a user with permission to only run our app
# if this isnt set up, docker will run as root, which isnt safe
RUN adduser -D user
# switch to user we just created
USER user
