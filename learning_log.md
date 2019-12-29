# setting up docker

- in root directory, `touch Dockerfile`
- goto hub.docker.com for a list of preconfigured docker base confs. we'll use 3.7-alpine
- Dockerfile comments via #
- once our docker file and other code is ready, build via `sudo docker build .`

# set up requirements.txt

- goto pipy.org, check latest version of django (currently 3.0.1, but in course 2.1.3)

# docker-compose

- allows us to manage our image and services
- in root, touch docker-compose.yml
- once done, in root docker-compose build

# travis-ci

- sign into travis-ci.org, sync with github, enable the repo you're working on
- in root of project, add conf file .travis.yml

# flake8

- python linting tool
- within /app, create config file .flake

# unit testing

- django unit test framework looks for all files starting with tests\*
- all test procedures must start with the word "test"
- run tests using `docker-compose run app sh -c "python manage.py test`

# django

- creating an app: `python manage.py startapp [appname]` or in dockerized format `docker-compose run app sh -c "ython manage.py startapp [appname]"`
- for the core service, we can get rid of the tests and views files since we're moving tests to a dedicated spot, and we're not serving any views
- dont forget. after we create an app, go to app/settings.py and add the app (by name) to the installed apps list
- we're using the get_user_model functionality provided by django.app/settings.py provides the option to customize this function.
- implement user model in core/models.py
- migrations: in order to initiate migrations for an app, go `docker-compose run app sh-c "python manage.py makemigrations [appname]"`

* migrations are django's way of mapping our models to the db. Every time we change the model, we need to run migrations.
