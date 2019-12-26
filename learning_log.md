# setting up docker
* in root directory, ``` touch Dockerfile```
* goto hub.docker.com for a list of preconfigured docker base confs. we'll use 3.7-alpine
* Dockerfile comments via #
* once our docker file and other code is ready, build via ``` sudo docker build .```

# set up requirements.txt
* goto pipy.org, check latest version of django (currently 3.0.1, but in course 2.1.3)

# docker-compose
* allows us to manage our image and services
* in root, touch docker-compose.yml
* once done, in root docker-compose build