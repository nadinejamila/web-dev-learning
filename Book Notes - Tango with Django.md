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
