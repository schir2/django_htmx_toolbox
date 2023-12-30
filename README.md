# Django HTMX Toolbox
A curated set of Django apps and utilities, HTMX PowerPack accelerates web development with interactive widgets. Featuring Dropzone for easy uploads, Autocompletion for seamless input, and Inline Editing for quick data manipulation. Simplify Django projects with HTMX dynamism.

## Setup
Install django-htmx
~~~shell
pip install django-htmx
~~~

Add the following to settings.py
~~~python
INSTALLED_APPS = [
    ...,
    'django_htmx',
]

MIDDLEWARE = [
    ...,
    "django_htmx.middleware.HtmxMiddleware",
]
~~~

