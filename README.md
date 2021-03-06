# List Builder Backend
# Overview
The listbuilder app REACT frontend will integrate with this Django REST-api backend connected to a postgresql database.

## Data Models
Link to [ERD](https://dbdiagram.io/d/5e924af039d18f5553fd74eb)

## Installation Requirements
```
$ pip3 install --upgrade pip
$ pip3 install virtualenv
$ python3 -m venv .env
$ source .env/bin/activate
$ pip3 install django
$ pip3 install psycopg2-binary
$ pip install python-dotenv
$ pip3 install djangorestframework
$ pip3 install djangorestframework-jwt
$ pip3 install django-extensions
$ python -m pip install django-cors-headers
```

NOTE: eventually we will need Cors as described in this [GA rest-django lesson](https://git.generalassemb.ly/jdr-0127/django-rest-framework) excerpt:
We need to configure CORS in order for other applications to use the API we just created.

This is outside of the scope of today's lesson, but it's super simple!

The [Django Rest Documentation page on AJAX](https://www.django-rest-framework.org/topics/ajax-csrf-cors/) is a great place to get started. It endorses the [Django Cors Headers](https://github.com/ottoyiu/django-cors-headers/) middleware, which can be installed like any other dependency with pipenv and is configured in the Project's settings.py

Also referenced in lesson: [Django REST framwork JWT (JSON Web Token)](https://jpadilla.github.io/django-rest-framework-jwt/) (already installed djangorestframework-jwt)
