# Notes on Tango with Django

## [Intro](http://www.tangowithdjango.com/book17/chapters/overview.html)

#### Common Design Specifications
1. N-Tier Architecture & Technologies Used
2. Wireframes
3. Pages & URL-Mappings
4. Entity-Relationship Diagram

## [Set-up](http://www.tangowithdjango.com/book17/chapters/requirements.html)

######1. Know the Terminal 
- Be familiar with [Unix](http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html)
- Know the core commands

######2. Install Software
- Install python
- Set-up the PYTHONPATH
- Use setuptools & pip
- Install django
- Install pillow
- Install other packages
    
######3. Set-up the Development Environment
- Set-up a virtual environment
- Create a code repository

## Creating a Django project
Create the project folder, `tango_with_django_project`.
```
$ django-admin.py startproject tango_with_django_project
```
Run the project in your local server.
```
python manage.py runserver
```
## Creating a Django Application
Create the app folder for the `rango` app.
```
python manage.py startapp rango
```
Include the newly created app in the project's settings.
```
# settings.py

INSTALLED_APPS = (
    ...
    'rango`,
)
```

## Creating a View
The `views.py` is where you can store a series of functions that take a clients’s requests and return responses.
```python
# rango/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!")
```

## Mapping URLs
The contents of `urls.py` will allow you to map URLs for your application (e.g. http://www.tangowithdjango.com/rango/) to specific views.
```python
# rango/urls.py

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
```
Join rango app's urls to your project’s master `urls.py` file.
```python
# tango_with_django_project/urls.py

urlpatterns = patterns('',
    ...
    url(r'^rango/', include('rango.urls')),
)
```
## Adding Templates

Set the templates directory path in your project’s `settings.py` file.

```python
# settings.py

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
     TEMPLATE_PATH,
)
```

Create a `templates` directory in your project folder wherein you save the following template. You may use Django template variables (e.g. `{{ variable_name }}`) in your template.

```
# templates/rango/index.html
<!DOCTYPE html>

{% load static %}

<html>
	<head>
		<title>Rango</title>
	</head>
	<body>
		<h1>Rango says...</h1>
		hello world! <strong>{{ boldmessage }}</strong><br />
	</body>
</html>
```

Find or create a new view within an application’s `views.py` file. Add your view-specific logic to the view.

```python
# rango/views.py

def index(request):
	# Construct a dictionary object which you can pass to the template engine 
	# as part of the template’s context.
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Make use of the `render()` helper function to generate the rendered response. 
    # Ensure you reference the request, then the template file, followed by the context dictionary!
    return render(request, 'rango/index.html', context_dict)
```

Map the view to a URL by modifying your project’s `urls.py` file - and the application-specific `urls.py` file, if any.

## Using Static Media
Set the static directory path in your project’s `settings.py` file.
```python
# settings.py

STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)
```

Create a `static` directory in your project folder wherein you save your static files, the directory you specified in your project’s STATICFILES_DIRS tuple within settings.py.
```
static/
    images/
         rango.jpg
```

Add a reference to the static media file to a template. For example, an image would be inserted into an HTML page through the use of the <img /> tag. Remember to use the {% load static %} and {% static "filename" %} commands within the template to access the static files.
```python
# index.html

{% load static %}

...
<img src="{% static "images/rango.jpg" %}" alt="Picture of Rango" /><br />
...
```

## Database Setup

With a new Django project, you should first tell Django about the database you intend to use. 

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Working with Models
A **model** is a Python object that describes your data model/table. 

###### Adding models

First, create the new models in your application.
```python
# rango/models.py

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
```

*Model/Database Table Relations:*
- `ForeignKey`, a field type that allows us to create a **one-to-many** relationship.
- `OneToOneField`, a field type that allows us to define a strict **one-to-one** relationship.
- `ManyToManyField`, a field type which allows us to define a **many-to-many** relationship.

###### Admin Registration

Update `admin.py` to include and register your new model(s).

```python
from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)
```
###### Database Migration

Then perform the migration `$ python manage.py makemigrations`.

Apply the changes `$ python manage.py migrate`. This will create the necessary infrastructure within the database for your new model(s).

Create/Edit your population script for your new models, if any.

In which case you have to delete your database, run the `migrate` command, then `createsuperuser` command, followed by the `sqlmigrate` commands for each app, then you can populate the database.
